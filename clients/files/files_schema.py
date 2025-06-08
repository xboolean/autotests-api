from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

    
class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.jpg")
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema
