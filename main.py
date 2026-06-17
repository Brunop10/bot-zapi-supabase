from services.supabase_service import get_contacts


def main():
    contacts = get_contacts()

    print(f"Found {len(contacts)} contacts\n")

    for contact in contacts:
        print(
            f"{contact['nome_contato']} - "
            f"{contact['numero_contato']}"
        )


if __name__ == "__main__":
    main()