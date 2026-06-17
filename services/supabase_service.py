from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def get_contacts(limit=3):
    response = (
        supabase
        .table("contatos")
        .select("*")
        .limit(limit)
        .execute()
    )

    return response.data