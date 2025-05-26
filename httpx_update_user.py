import httpx

from tools import fakers


payload = {
    "email": "user_7@example.com",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8001/api/v1/users", json=payload)

assert create_user_response.status_code == 200
print(create_user_response.status_code)
print(create_user_response.json())

user_id = create_user_response.json()["user"]["id"]

payload = {
    "email": "user@example.com",
    "password": "string",
}

login_response = httpx.post("http://localhost:8001/api/v1/authentication/login", json=payload)

assert login_response.status_code == 200
print(login_response.status_code)
print(login_response.json())


update_payload = {
  "email": fakers.get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

get_user_headers = {
    "Authorization": f"Bearer {login_response.json()["token"]["accessToken"]}"
}

update_user_response = httpx.patch(f"http://localhost:8001/api/v1/users/{user_id}", headers=get_user_headers, json=update_payload)

assert update_user_response.status_code == 200
print(update_user_response.status_code)
print(update_user_response.json())
