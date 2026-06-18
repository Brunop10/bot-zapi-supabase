from services.supabase_service import get_contacts
from services.zapi_service import send_message


def main():
    contacts = get_contacts(limit=3)

    print(f"Found {len(contacts)} contacts")

    for contact in contacts:
        name = contact["nome_contato"]
        phone = contact["numero_contato"]

        message = (
            f"Olá, {name} tudo bem com você?"
        )

        print(
            f"Sending message to {name}"
        )

        send_message(
            phone=phone,
            message=message
        )


if __name__ == "__main__":
    main()