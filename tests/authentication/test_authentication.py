from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from tools.allure.stories import AllureStory
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from clients.users.private_users_client import PrivateUsersClient
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:

    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_login(
            self,
            function_user: UserFixture,
            public_users_client: PublicUsersClient,
            authentication_client: AuthenticationClient
    ):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_user(self, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())



    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        
        validate_json_schema(response.json(), response_data.model_json_schema())
