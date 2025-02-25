from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from openai import OpenAI
from pathlib import Path
import os
import io
from dotenv import load_dotenv


router = APIRouter()
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



@router.post('/api/audio/tts')
async def tts(text: str):
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    audio_byte = io.BytesIO(response.content)

    return  StreamingResponse(audio_byte, media_type="audio/mp3")


@router.post('/api/audio/whisper')
async def gettranscription(file_upload: UploadFile = File(...)):

    audio_read = await file_upload.read()
    audio_byte = io.BytesIO(audio_read)
    audio_byte.name = 'transcription.mp3' 

    transcript = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_byte
    )

    return transcript.text



















