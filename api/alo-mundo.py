from fastapi import FastAPI

app = FastAPI()

@app.get("/alo-mundo")
async def alo_mundo():
    return "Alou...é por mim que voce procura?"


@app.get("/")
async def home():
    return "Alou...Esta é a minha HOME!"
