import datetime
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.request import Request
from api import models
from rest_framework import serializers


class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()  # 只看这里

    title = serializers.CharField()

    order = serializers.IntegerField()


class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields = "__all__"


class DepartView(APIView):
    def get(self, request, *args, **kwargs):
        # 1.数据库中获取数据  obj.title   obj.order  obj.count
        #   [obj,obj,obj,]
        queryset = models.Depart.objects.all()

        # 2.序列化器转换JSON格式：int/str/list/dict/     datetime/decimal   序列化器
        ser = DepartSerializer(instance=queryset, many=True)
        # print(ser.data)  # {'title': '技术部', 'count': 10}

        # 3.返回给用户
        context = {"status": True, "data": ser.data}
        return Response(context)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="get_gender_display")  # 只看这里
    title = serializers.CharField(source="depart.title")  # ["depart","depart"]
    order = serializers.IntegerField(source="order")

    class Meta:
        model = models.UserInfo
        fields = ["name", "age", "xx"]
        list_serializer_class = serializers.ListSerializer


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        # 1.获取数据
        queryset = models.UserInfo.objects.all()
        # 2.序列化
        ser = UserSerializer(instance=queryset, many=True)

        # 3.返回给用户
        context = {"status": True, "data": ser.data}

        return Response(context)


class HomeView(APIView):
    # 所有的解析器
    # parser_classes = [JSONParser, FormParser]

    # 根据请求，匹配对应的解析器 ;  寻找渲染器
    # content_negotiation_class = DefaultContentNegotiation

    def get(self, request, *args, **kwargs):
        print(request.version)
        print(request.versioning_scheme)
        # 反向生成URL: http://127.0.0.1:8000/api/v1/home/
        # url = request.versioning_scheme.reverse("hh", request=request)
        # print(url)
        return Response("...")

    def post(self, request, *args, **kwargs):
        # 当调用request.data时就会触发解析的动作。
        print(request.data)  # {}
        print(request.data)  # QueryDict
        return Response("OK")


class ImgView(APIView):
    parser_classes = []

    def post(self, request, *args, **kwargs):
        # 当调用request.data时就会触发解析的动作。
        print(request.data)  # {}
        print(request.data)  # QueryDict
        return Response("OK")
