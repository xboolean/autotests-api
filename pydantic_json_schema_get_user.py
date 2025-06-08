from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema


create_user_request = CreateUserRequestSchema()
create_user_response = get_public_users_client().create_user(create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
get_user_response = get_private_users_client(authentication_user).get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
