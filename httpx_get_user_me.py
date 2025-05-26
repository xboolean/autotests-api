import httpx

from tools import fakers


payload = {
    "email": "user@example.com",
    "password": "string",
}

login_response = httpx.post("http://localhost:8001/api/v1/authentication/login", json=payload)

assert login_response.status_code == 200
print(login_response.status_code)
print(login_response.json())


get_user_headers = {
    "Authorization": f"Bearer {login_response.json()["token"]["accessToken"]}"
}

update_user_response = httpx.get(f"http://localhost:8001/api/v1/users/me", headers=get_user_headers)

assert update_user_response.status_code == 200
print(update_user_response.status_code)
print(update_user_response.json())
