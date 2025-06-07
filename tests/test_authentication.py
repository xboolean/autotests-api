from http import HTTPStatus

import pytest

from tools.fakers import get_random_email
from clients.users.public_users_client import PublicUsersClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.assertions.authentication import assert_login_response
from clients.authentication.authentication_client import AuthenticationClient
from .conftest import UserFixture
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema(
        email=get_random_email(),
        password="string",
        last_name="string",
        first_name="string",
        middle_name="string"
    )
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.regression
@pytest.mark.authentication
def test_login(
        function_user: UserFixture,
        authentication_client: AuthenticationClient
):
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.regression
@pytest.mark.authentication
def test_get_user_me(function_user: UserFixture, private_users_client):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema(user=response.json()["user"])
    
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(function_user.response, response_data)
    
    validate_json_schema(response.json(), response_data.model_json_schema())
