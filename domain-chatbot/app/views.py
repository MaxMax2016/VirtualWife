from django.shortcuts import render
import asyncio
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .core.aili_anchor_chat_robot import Aili
from .translation.translation_client import TranslationClient
import logging
logging.basicConfig(level=logging.INFO)

@api_view(['POST'])
def chat(request):
    '''
      聊天
    :param request:
    :return:
    '''
    data = json.loads(request.body.decode('utf-8'))
    chat = None
    try:
        chat = Aili.chat(query=data["query"])
    except Exception as e:
        print("chat error: %s" % str(e))
        chat = '发生系统错误，请稍后重试'
    return Response({"response": chat, "code": "200"})

@api_view(['POST'])
def translation(request):
    '''
      翻译，中文 -> 日语
    :param request:
    :return:
    '''
    data = json.loads(request.body.decode('utf-8'))
    translation = None
    try:
        translation = TranslationClient.translation(query=data["query"])["translation"][0]
    except Exception as e:
        print("translation error: %s" % str(e))
        translation = '发生系统错误，请稍后重试'
    return Response({"response": translation, "code": "200"})