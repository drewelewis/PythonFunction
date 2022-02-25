import azure.functions
from cryptography.fernet import Fernet
# https://pypi.org/project/cryptography/


def main(req: azure.functions.HttpRequest) -> str:
    user = req.params.get('user')

    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"A really secret message. Not for prying eyes.")

    secret = f.decrypt(token)
    return f' token=={token} secret=={secret}'
