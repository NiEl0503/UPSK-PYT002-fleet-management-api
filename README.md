# Software de Gestão de Frota API

## Índice

* [1. Resumo do projeto](#2-resumo-do-projeto)
* [2. Critérios de aceitação do projeto](#5-critérios-de-aceitação-do-projeto)
* [3. Tecnologias Utilizadas](#6-tecnologias-utilizadas)
  
***

## 1. Resumo do projeto

Projeto desenvolvido para Laboratoria Python Upskilling, que consistiu na criação de uma API REST para um software de gestão de frotas para verificar a localização dos veículos de uma empresa de táxi em Pequim, China.

## 2. Critérios de aceitação do projeto

Nossa cliente instalou dispositivos GPS em seus táxis. Esses dispositivos usam sinais de satélite para determinar com precisão as coordenadas geográficas do táxi.

Nossa cliente requer:

1. Carregar as informações dos arquivos SQL para um banco de dados
PostgreSQL.
2. Desenvolver uma API REST que permita consultar, por meio de requisições
HTTP, as informações armazenadas no banco de dados.


#### [História do usuário 1] Carregar informações no banco de dados

Eu, como desenvolvedora, quero carregar as informações armazenadas até agora em [arquivos SQL](https://drive.google.com/file/d/1T5m6Vzl9hbD75E9fGnjbOiG2UYINSmLx/view?usp=drive_link) em um banco de dados PostgreSQL, para facilitar sua consulta e análise.

##### Critérios de aceitação

* Deve-se considerar o seguinte diagrama para a implementação das
relações entre as tabelas

![mer](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fsql-diagram.png?alt=media)

* A tabela de _trajectories_ deve ser criada com o "id" que aumenta
automaticamente (SERIAL) para poder inserir os valores sem a necessidade de
especificar um identificador.

##### Definição de pronto

* O banco de dados tem a tabela de táxis criada.
* A tabela de táxis tem os dados dos táxis carregados.
* O banco de dados tem a tabela de trajetórias criada.
* A tabela de trajetórias tem os dados das trajetórias dos táxis carregados.

***

##### [História do usuário 2] Endpoint de listagem de táxis

Eu, como cliente da API REST, necessito de um _endpoint_ para listar todos os táxis.

##### Critérios de aceitação

* O _endpoint_ responde para cada táxi: id e placa.
* O _endpoint_ paginamos os resultados para garantir que as respostas
sejam mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_ desenvolvido, especificando [método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), url, parâmetros,
[cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), [códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

#### [História do usuário 3] Endpoint de histórico de localizações

Eu, como cliente da API REST, necessito de um _endpoint_ para consultar todas as localizações de um táxi dado o id do táxi e uma data.

##### Critérios de aceitação

* O _endpoint_ responde para o id do táxi e uma data consultado as   seguintes informações: latitude, longitude e timestamp (data e hora).
* O _endpoint_ paginamos os resultados para garantir que as respostas sejam mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_ desenvolvido, especificando [método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), url, parâmetros,
[cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), [códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

#### [História do usuário 4] Endpoint de última localização

Eu, como cliente da API REST, necessito de um _endpoint_ para consultar a última localização reportada por cada táxi.

##### Critérios de aceitação

* O _endpoint_ responde para cada táxi as seguintes informações: id, placa, latitude, longitude e timestamp (data e hora).
* O _endpoint_ paginamos os resultados para garantir que as respostas sejam mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_ desenvolvido, especificando [método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parâmetros, [cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), [códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

## 3. Tecnologias Utilizadas
<div align="center">
  <a href="https://git-scm.com/">
  <img src="https://skillicons.dev/icons?i=git"/>
    Git
  <a href="https://github.com/">
  <img src="https://skillicons.dev/icons?i=github"/>
    Github
   <a href="https://nodejs.org/en">
  <img src="https://skillicons.dev/icons?i=nodejs"/>
     NodeJs
   <a href="https://www.python.org/">
  <img src="https://skillicons.dev/icons?i=python"/>
  Python
   <a href="https://www.djangoproject.com/">
  <img src="https://skillicons.dev/icons?i=django"/>
  Django
   <a href="https://www.postgresql.org/">
  <img src="https://skillicons.dev/icons?i=postgres"/>
  Postgresq
 </div>

