# Estudo sobre Bancos de Dados Relacionais :clipboard:

## Objetivos :dart:

Este repositório começou a ser escrito como um estudo simples sobre manipulação de dados utilizando o SGBD MySQL conforme proposto pelo LAB "MySql - Como modelar um banco de controle de séries assistidas" proposto pela [Digital Innovation One](https://dio.me/). Entretanto, achei interessante expandir um pouco o escopo dos estudos e aplicar meus conhecimentos e expandir utilizando a seguinte stack:

* Python
    * Extract: Requests
    * Transform: Pandas
    * Load(ORM): SQLAlchemy / SQL RAW / CSV
* Bancos de Dados
    * SQLite
    * PostgreSQL
    * MySQL
* Arquitetura
    * Microsserviços: Docker e Docker Compose
    * Design Pattern: MV(Model/View) e Unit of Work(SQLAlchemy)
* Dataset
    * Dados da conta da Netflix da família armazenados no Google Drive

## Utilização :arrow_forward:

Para testar essa aplicação, é necessário a instalação prévia das seguintes ferramentas:

* :snake: [Python3.9](https://www.python.org/) ou [Anaconda](https://www.anaconda.com/);
* :whale: [Docker](https://www.docker.com/).

Após o término das instalações, basta executar os seguintes comandos:

```console
wall@kalingth:~$ pip install -r requirements.txt
Installing
a
lot
of
libraries
wall@kalingth:~$ docker compose up -d
Inserting
Two
Containers
On
Docker Whale
wall@kalingth:~$ python main.py
Running
The
Application
wall@kalingth:~$
```

That's all folks! :pig: