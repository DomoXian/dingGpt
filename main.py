from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import requests
import json

app = FastAPI()


class Message(BaseModel):
    msg: str


@app.post('/api/sendMsg')
async def send_message(message: Message):
    print("输入内容", message)
    # 在此处添加发送消息的代码
    if not message:
        return "请输入内容"

    url = 'https://www.yubadev.com/api/stream'
    data = {
        "messages": [{
            "role": "user",
            "content": message.msg
        }],
        "key": "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",
        "temperature": 0.6
    }
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'origin': 'https://www.yubadev.com',
        'referer': 'https://www.yubadev.com/'
    }
    print("开始请求", data)
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return 'gpt开小差了，请稍后再试'
