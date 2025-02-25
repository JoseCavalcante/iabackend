from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv


router = APIRouter()
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) 



@router.post('/api/vision/imggeneration')
async def image_generation(prompt_image: str):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_image,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    return response.data[0].url












