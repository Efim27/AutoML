import os
import uuid

from app.catboost.MLTask.regression import RegressionModel
from fastapi import APIRouter, Form, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse

controller = APIRouter(prefix='/api/v1')

files_directory = f'{os.getcwd()}/app/catboost'
projects_dir_name = "projects"


def create_model(project_path: str, file_name: str) -> str:
    reg_model = RegressionModel(project_path, file_name, 'Age')
    reg_model.train()
    reg_model.evaluate()
    return reg_model.save()


def create_file(file: UploadFile) -> list[str]:
    projects_dir_path = f'{files_directory}/{projects_dir_name}'

    if not os.path.isdir(projects_dir_path):
        os.makedirs(projects_dir_path)

    uniq_proj_name = uuid.uuid4().hex
    uniq_proj_path = f'{projects_dir_path}/{uniq_proj_name}'

    os.mkdir(uniq_proj_path)

    file_name = file.filename
    file_path = f'{uniq_proj_path}/{file_name}'

    with open(file_path, "wb") as new_file:
        new_file.write(file.file.read())

    model_file_name = create_model(uniq_proj_path, file_name)

    return [uniq_proj_name, model_file_name]


@controller.post("/upload/")
def upload_file(file: UploadFile = File(...), regression_column_name: str = Form(...)) -> dict:
    print(regression_column_name)
    file_names = create_file(file)
    return {
        "projectname": file_names[0],
        "filename": file_names[1]
    }


@controller.get("/download", response_class=FileResponse)
async def download_file(project_name: str = '', file_name: str = ''):
    if project_name == '':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The project name should not be empty."
        )

    if file_name == '':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The file name should not be empty."
        )

    path = f'{files_directory}/{projects_dir_name}/{project_name}/{file_name}'
    if not os.path.isfile(path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"A file with this name [{file_name}] in project [{project_name}] was not found."
        )

    return path
