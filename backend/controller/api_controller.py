from fastapi import APIRouter, UploadFile

controller = APIRouter(prefix='/api')


@controller.get("/hello/")
def read_root():
    return {"Hello": "World"}


@controller.post("/uploadfile/")
def upload_file(file: UploadFile):
    print(file.filename)
    return {"filename": file.filename}
