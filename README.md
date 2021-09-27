# Criação de um app de analise de imagens.


## Ferramentas

- Django
- Postgres
- Docker
- Django restframework

## Roda o projeto localmente:
**Obs.: Para rodar o projeto é necessario ter Docker e Docker Compose**

1. Clone o repositório.
2. Entre na pasta.
3. Rode o comando docker compose


```
- git clone git@github.com:ffabiorj/analise_image.git
- cd analise_image
- docker-compose build
- docker-compose up

```

### Endpoints da api

- http://127.0.0.1:8000/api/v1/images/ # retorna todas as imagens
- http://127.0.0.1:8000/api/v1/empresas/id/ # retorna uma imagem pelo id
- http://127.0.0.1:8000/api/v1/analises/ # retorna todas as analises
- http://127.0.0.1:8000/api/v1/analises/id/ # retorna uma analise pelo id

### Exemplos de entrada para os endpoints

```
Dados para cadastrar empresa na api
{

}

```

### Rodar os testes

```

pytest

```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Postgres](https://www.postgresql.org/)

[Docker] https://www.docker.com/

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)