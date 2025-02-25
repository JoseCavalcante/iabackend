from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv
import openai


#instance - object

load_dotenv()

router = APIRouter()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



@router.post('/api/text/chat')
async def chatinput(message: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content":"You are a helpful assistant."},
            {"role":"user", "content":message}
        ]
    )
    return completion.choices[0].message.content


@router.post('/api/text/moderations')
async def moderation(textmoderation: str):
    response = client.moderations.create(
    model="omni-moderation-latest",
    input=textmoderation,
)
    return response














