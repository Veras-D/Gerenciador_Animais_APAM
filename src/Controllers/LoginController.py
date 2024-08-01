from dotenv import load_dotenv
import os


def password_verification(page, name: str, password: str):
    # Carrega as variáveis do arquivo .env
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    load_dotenv(dotenv_path)


    # Acesando usuario e senha
    username_ = str(os.getenv("USER_NAME"))
    password_ = str(os.getenv("PASSWORD"))

    if name == username_ and password == password_:
        return True
    return False
