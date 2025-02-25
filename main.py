from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv



from api.customerRouter import router as api_customer_router
from api.employeeRouter import router as api_employee_router
from api.salesRouter import router as api_sales_router
from api.textRouter import router as api_openai_text
from api.visionRouter import router as api_openai_vision
from api.audioRouter import router as api_opeanai_audio


load_dotenv()

app = FastAPI()

# Configurações de CORS
def get_cors_origins():
        origins = os.getenv('CORS_ORIGINS')
        if origins:
            return [origin.strip() for origin in origins.split(',')]
        return []

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)










app.include_router(api_customer_router)
app.include_router(api_employee_router)
app.include_router(api_sales_router)
app.include_router(api_openai_text)
app.include_router(api_openai_vision)
app.include_router(api_opeanai_audio)







