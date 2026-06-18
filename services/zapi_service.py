import requests

from config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_CLIENT_TOKEN
)


def send_message(phone: str, message: str):
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/send-text"
    )

    payload = {
        "phone": phone,
        "message": message
    }

    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response