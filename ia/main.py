from fastapi import FastAPI
import torch # type: ignore
import torch_directml # type: ignore
import uvicorn
from dotenv import load_dotenv
import os


#initialisation de l'API

app = FastAPI()


device = torch_directml.device()


@app.get("/")
def home():
    return {"message":" Bienvenue sur l'API LAMPIXIA"}

## crée les port pour le lancement de l'API
if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")  
    port = int(os.getenv("PORT", 8000))    
    uvicorn.run(app, host=host, port=port)

    