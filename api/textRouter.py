from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/api/text/chat")
async def chatcompletion(msg: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "you are a helpful assistant."},
            {
                "role": "user",
                "content": msg
            }
        ]
    )
    return completion.choices[0].message.content

@router.post("/api/text/moderation")
async def chatmoderation(msg: str):
    response = client.moderations.create(
        model="omni-moderation-latest",
        input=msg,
    )

    return response