from fastapi import APIRouter, File, UploadFile

from app.schemas.upload import UploadResponse
from app.services.s3_service import S3Service


router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

s3_service = S3Service()


@router.post(
    "/image",
    response_model=UploadResponse,
)
def upload_image(
    file: UploadFile = File(...),
):

    url = s3_service.upload_image(file)

    return {
        "url": url,
    }