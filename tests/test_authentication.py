from http import HTTPStatus
import pytest

from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.fakers import get_random_email
from clients.authentication.authentication_client import get_authentication_client
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    create_user_request = CreateUserRequestSchema(
        email=get_random_email(),
        password="string",
        last_name="string",
        first_name="string",
        middle_name="string"
    )
    create_user_response = public_users_client.create_user(create_user_request)
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
