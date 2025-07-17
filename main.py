from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import uuid
import os
from rembg import remove

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    # Save the uploaded file
    file_id = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{file_id}.png"
    output_path = f"{OUTPUT_DIR}/{file_id}.png"
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Remove background
    with open(input_path, "rb") as inp_file:
        input_data = inp_file.read()
        output_data = remove(input_data)

    with open(output_path, "wb") as out_file:
        out_file.write(output_data)

    return FileResponse(output_path, media_type="image/png", filename="output.png")