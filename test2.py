from typing import Literal
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv('.env')

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": os.environ.get('API_KEY'), "client_secret": os.environ.get('SECRET_KEY')}
    return str(requests.post(url, params=params).json().get("access_token"))

# 修改成自己的api key和secret key

TOKEN = get_access_token()
url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + TOKEN

def body():
    payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": s
                }
            ]
    })
    headers = {
            'Content-Type': 'application/json'
        }

    res = requests.request("POST", url, headers=headers, data=payload).json()

def translate(s: str):
    """AI翻译"""
    body()
    source=res['result']
    a='你是一个点评大师，请点评这句翻译的不足，要求简介明了。文字是：'+source+'原文是'+s
    body()
    advice = res['result']

    a = '你是个翻译大师，请根据以下的建议' + advice + '翻译这句句子：'+s
    body()
    return res['result']
