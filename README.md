Listar Materiais (GET /materials):

Método: GET
URL: http://localhost:5000/materials
Essa requisição retornará a lista de materiais cadastrados no formato JSON.

Criar Material (POST /materials):

Método: POST
URL: http://localhost:5000/materials
Body (application/json):
json

{
  "material": {
    "name": "folha A4",
    "qtde": 100
  }
}

Essa requisição criará um novo material com o nome "folha A4" e quantidade 100.

Buscar Material por ID (GET /materials/<id>):

Método: GET
URL: http://localhost:5000/materials/1
Essa requisição buscará o material com ID 1 e retornará os dados do material no formato JSON.

Alterar Material por ID (PUT /materials/<id>):

Método: PUT
URL: http://localhost:5000/materials/1
Body (application/json):
json
  
{
  "material": {
    "name": "folha A3",
    "qtde": 50
  }
}
  
Essa requisição alterará o material com ID 1 para o nome "folha A3" e quantidade 50.

Remover Material por ID (DELETE /materials/<id>):

Método: DELETE
URL: http://localhost:5000/materials/1
Essa requisição removerá o material com ID 1.

Lembre-se de substituir "localhost:5000" pela URL correta do seu servidor Flask, se estiver usando uma URL diferente.

Agora você pode realizar essas requisições no Postman e verificar as respostas do servidor. Certifique-se de que o servidor Flask esteja em execução enquanto você faz os testes.
