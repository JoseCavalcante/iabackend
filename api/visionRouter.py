from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/api/text/imagegenaration")
async def image_generation(msg: str):
    response = client.images.generate(
        model="dall-e-3",
        prompt=msg,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url

