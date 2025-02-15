import os
from dotenv import load_dotenv

def authenticator():
    load_dotenv()
    user_email = os.getenv("USER_EMAIL")
    user_password = os.getenv("USER_PWD")

    return user_email, user_password