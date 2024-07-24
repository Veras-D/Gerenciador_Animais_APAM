import requests

def consulta_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  response = requests.get(url)

  if response.status_cod == 200:
    return response.json()
  else:
    return None
