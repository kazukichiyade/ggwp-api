from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers


# 新規ユーザー作成に特化した汎用APIView
class CreateUserView(generics.CreateAPIView):
    # シリアライザー指定
    serializer_class = serializers.UserSerializer

    # 現在permission_classesはjwtを使用する事になっているが、
    # 新規ユーザー作成の場合認証されていないユーザーも触るのでAllowAnyで誰でもアクセスできるように認証を上書き
    permission_classes = (AllowAny,)