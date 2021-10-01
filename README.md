# Criação de um app de analise de imagens.

**Obs: Configurei o projeto sem o docker porque estava quebrando meus testes e meu tempo de entrega estava no final**

## Ferramentas

- Django
- Django restframework


## Roda o projeto localmente:

1. Clone o repositório.
2. Entre na pasta.
3. Crie um ambiente de desenvolvimento com python 3.7.
4. Ative o ambiente.
5. Instale as dependências.
6. Crie um arquivo .env
7. Rode as migrações
8. Rode o projeto
9. Acesse o link

```
- git clone git@github.com:ffabiorj/analise_image.git
- cd analise_image
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- python contrib/env_gen.py
- python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/api/v1

```

### Endpoints da api

- http://127.0.0.1/api/v1/imagens/ # retorna todas as imagens
- http://127.0.0.1:8000/api/v1/imagens/id/ # retorna uma imagem pelo id
- http://127.0.0.1:8000/api/v1/analises/ # retorna todas as analises
- http://127.0.0.1:8000/api/v1/analises/id/ # retorna uma analise pelo id

### Exemplos de entrada para os endpoints

```
Dados para cadastrar uma imagem.
{
    "nome": "teste",
    "imagem": "imagem.jpg"
}

Dados para cadastrar uma analise. 
{
    "nome": "teste",
    "tipo": "oleo",
    "status": "A",
    "imagem": "pk_da_imagem"
}

```

### Rodar os testes

```

pytest

```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)