from services.zapi_service import send_message


def main():
    send_message(
        "5555997211544",
        "Teste da integração Z-API"
    )


if __name__ == "__main__":
    main()