from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

#from api.customerRouter import router as api_customer
#from api.employerRouter import router as api_employer
#from api.saleRouter import router as api_sales

from api.textRouter import router as api_chat
from api.visionRouter import router as api_image
from api.audioRouter import router as api_audio

load_dotenv()

app = FastAPI()

# configuracao do CORS
def get_cors_origins():

    origins = os.getenv("CORS_ORIGINS")

    if origins:
        return[origin.strip() for origin in origins.split(",")]
    return []

app.add_middleware(
    CORSMiddleware,
    allow_origins = get_cors_origins(),
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#app.include_router(api_customer)
#app.include_router(api_employer)
#app.include_router(api_sales)
app.include_router(api_chat)
app.include_router(api_image)
app.include_router(api_audio)