from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionMixin,
)
from django.conf import settings


# BaseUserManagerをオーバーライド(username認証からemail認証に変更)
class UserManager(BaseUserManager):

    # ユーザー作成関数
    def create_user(self, email, password=None):

        # emailが無い場合、raiseで例外を発生させる
        if not email:
            raise ValueError("email is must")

        # インスタンス作成及びemail格納(取得したemailが大文字も小文字になるように設定)
        user = self.model(email=self.normalize_email(email))

        # 引数で取得したパスワードをハッシュ化
        user.set_password(password)

        # DB保存
        user.save(using=self._db)

        return user
