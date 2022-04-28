import os
import uuid

from fastapi import APIRouter, Form, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse

controller = APIRouter(prefix='/api/v1')

files_directory = "user-files"


def create_file(file: UploadFile) -> str:
    if not os.path.isdir(files_directory):
        os.mkdir(files_directory)
    os.chdir(files_directory)

    uniq_file_name = uuid.uuid4().hex + file.filename

    with open(uniq_file_name, "wb") as new_file:
        new_file.write(file.file.read())

    os.chdir('..')
    return uniq_file_name


@controller.post("/upload/")
def upload_file(file: UploadFile = File(...), regression_column_name: str = Form(...)) -> dict:
    print(regression_column_name)
    file_name = create_file(file)
    return {"filename": file_name}


@controller.get("/download", response_class=FileResponse)
async def download_file(file_name: str = ''):
    if file_name == '':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The file name should not be empty."
        )
    path = f'{files_directory}/{file_name}'
    if not os.path.isfile(path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"A file with this name [{file_name}] was not found."
        )

    return path
