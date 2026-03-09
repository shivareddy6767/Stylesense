from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OutfitRequest(BaseModel):
    gender: str
    occasion: str
    color: str


@app.post("/recommend")
def recommend(data: OutfitRequest):

    outfit = f"For a {data.occasion} occasion, a {data.color} outfit is perfect for {data.gender}"

    return {"suggestion": outfit}