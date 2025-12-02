# db/queries.py
from db.connection import get_connection

def authenticate_user(username, password):
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, username, name, user_type FROM users WHERE username=%s AND password=%s AND status='Active'",
        (username, password)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user