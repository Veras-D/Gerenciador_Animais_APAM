from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)


# Acesando usuario e senha
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

print(f"Usuario: {username}")
print(f"Senha: {password}")

