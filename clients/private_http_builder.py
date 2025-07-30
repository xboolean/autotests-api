from functools import lru_cache

from pydantic import BaseModel
from httpx import Client

from .authentication.authentication_client import get_authentication_client, LoginRequestSchema


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_response = authentication_client.login(user)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
