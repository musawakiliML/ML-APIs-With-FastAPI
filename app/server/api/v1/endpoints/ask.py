from fastapi import APIRouter, Form, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import io
from PIL import Image

from app.server.utils.model import model_pipeline

router = APIRouter()

@router.post("/", response_description="Ask AI about Visual Things")
def ask(image: UploadFile, text: str = Form(...)):
    try:
        image_content = image.file.read()
        image = Image.open(io.BytesIO(image_content))

        result = model_pipeline(text, image)

        return JSONResponse(content={"answer":result}, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)