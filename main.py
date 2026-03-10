from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend")
async def recommend(
    gender: str = Form(...),
    occasion: str = Form(...),
    color: str = Form(...),
    image: UploadFile = File(...)
):

    # Only MALE outfit images
    male_outfits = [
        "https://images.pexels.com/photos/1043474/pexels-photo-1043474.jpeg",
        "https://images.pexels.com/photos/428338/pexels-photo-428338.jpeg",
        "https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg"
    ]

    # Only FEMALE outfit images
    female_outfits = [
        "https://images.pexels.com/photos/1536619/pexels-photo-1536619.jpeg",
        "https://images.pexels.com/photos/6311475/pexels-photo-6311475.jpeg",
        "https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg"
    ]

    gender = gender.lower().strip()

    if gender == "male":
        outfits = male_outfits
    else:
        outfits = female_outfits

    return {"outfits": outfits}