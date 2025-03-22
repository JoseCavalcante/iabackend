from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from openai import OpenAI
import io
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

router = APIRouter()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/api/audio/tts_memory")
async def tts_memory_generation(texto: str):

    if not texto.strip():
        return {"error": "O texto fornecido está vazio."}

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=texto,
    )

    if not response.content or len(response.content) == 0:
        return {"error": "A resposta da API está vazia ou inválida."}    

    audio_bytes = io.BytesIO(response.content)
    
    X = StreamingResponse(audio_bytes, media_type="audio/mp3")
    
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    
    #return {"Áudio salvo como 'output.mp3'. Verifique se ele contém som."}

    return X



#audio gerado no HD da maquina 
@router.post("/api/audio/tts")
async def tts_generation(texto: str):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=texto,
    )
    
    return response.stream_to_file(speech_file_path)

#audio gerado no HD da maquina 
@router.post("/api/audio/stt_whisper")
async def stt_generation(file_upload: UploadFile = File(...)):

    audio_read = await file_upload.read()
    audio_byte = io.BytesIO(audio_read)
    audio_byte.name = "transcription.mp3"

    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_byte
    )
    
    return transcript.text