from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from .base import assert_equal


def assert_user(actual, expected):
    assert_equal(actual, expected)


def assert_get_user_response(response: CreateUserResponseSchema, request: GetUserResponseSchema):
    assert_equal(response.user.id, request.user.id)
    assert_equal(response.user.email, request.user.email)
    assert_equal(response.user.last_name, request.user.last_name)
    assert_equal(response.user.first_name, request.user.first_name)
    assert_equal(response.user.middle_name, request.user.middle_name)


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")