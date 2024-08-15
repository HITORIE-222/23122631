from typing import Literal

import requests
import json

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

# 修改成自己的api key和secret key
API_KEY = "FDkU3RFP6CF8KPmxcajdEWr1"
SECRET_KEY = "fPceiB6bUdhUOHoZr0szDdTgtNGEd95s"
TOKEN = get_access_token()
url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + TOKEN



with open('source.txt', 'r') as file:
    query = file.read().strip()

#tokens计算、chunk_size计算、分割chunks
token_count = token_count(query)
chunk_size = calculate_chunk_size(token_count, 800)
chunks = get_text_chunks(query,chunk_size)

results = []
for index in range(len(chunks)):
    tagged_text = chunks[index]
    """
    如果需要增加上下文，采用如下方式；注意需要提示词配合
    tagged_text = (
            "".join(chunks[0:index])
            + "<TRANSLATE_THIS>"
            + chunks[index]
            + "</TRANSLATE_THIS>"
            + "".join(chunks[index + 1 :])
    )
    """
    result = call_coze_api(tagged_text)
    result_dict =json.loads(result)
    results.append(result_dict.get('output'))

output = " ".join(results)
with open('target.txt', 'w') as file:
    file.write(output)