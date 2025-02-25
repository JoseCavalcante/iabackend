from fastapi import FastAPI

app = FastAPI()



@app.get("/firstrouter")

async def hello():
    return "Hello World"




@app.get("/")

async def homepage():
    return "This is the home page"





