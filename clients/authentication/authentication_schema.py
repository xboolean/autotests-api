from pydantic import BaseModel, Field, ConfigDict


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

    model_config = ConfigDict(populate_by_name=True)

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema
    

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str