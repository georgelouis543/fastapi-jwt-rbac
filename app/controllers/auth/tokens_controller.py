import datetime
import os

import jwt
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(
        user_id: int,
        user_name: str,
        user_role: str
):
    try:
        user_id = user_id
        user_name = user_name
        user_role = user_role

        payload = {
            'user_id': user_id,
            'username': user_name,
            'user_role': user_role,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)  # Token expiration time
        }
        access_token = jwt.encode(
            payload,
            ACCESS_TOKEN_SECRET,
            algorithm=ALGORITHM
        )
        return access_token

    except Exception as e:
        print(f'Exited with Exception: {e}')
        return None