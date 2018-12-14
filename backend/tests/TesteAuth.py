import requests
import json

auth_data = {'email': 'teste@teste.com', 'password': 'teste123'}
response = requests.post('http://127.0.0.1:8000/api/auth/login/', data=auth_data)

if response.status_code == 200:
    print("Login realizado com sucesso")

    response_json = json.loads(response.content)
    token = response_json['data']['token']
    headers = {'Authorization': 'Token ' + token}

    print("Testando logout... ", end='')
    response_logout = requests.delete('http://127.0.0.1:8000/api/auth/logout/', headers=headers)
    if response_logout.status_code == 204:
        print("Logout realizado com sucesso")
else:
    print("Erro no login")