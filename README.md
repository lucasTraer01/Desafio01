ste projeto implementa uma API RESTful para scraping assíncrono de dados públicos (como o Sintegra Goiás), utilizando filas de mensagens, workers e cache. A solução é completamente containerizada com Docker e projetada para escalabilidade.

Tecnologias Utilizadas
FastAPI: Framework moderno e rápido para construção de APIs com Python

RabbitMQ: Sistema de filas de mensagens para execução assíncrona de tarefas

Redis: Armazenamento temporário de status e resultados das operações

Docker & Docker Compose: Orquestração e containerização dos serviços

BeautifulSoup + Requests: Bibliotecas para scraping de conteúdo HTML

Arquitetura do Sistema
O fluxo do sistema segue a seguinte estrutura:

Requisição Inicial:

O usuário faz uma requisição para o endpoint /scrape da API FastAPI

A API recebe a requisição e envia uma mensagem para a fila no RabbitMQ

Processamento Assíncrono:

Um worker consome a mensagem da fila RabbitMQ

O worker executa o scraping dos dados solicitados

Armazenamento de Resultados:

O worker armazena o status e os resultados no Redis

Consulta de Resultados:

O usuário consulta o endpoint /results/{task_id} na API FastAPI

A API recupera os dados do Redis e retorna para o usuário

Benefícios da Arquitetura
Escalabilidade: Workers podem ser adicionados conforme a demanda

Resiliência: Tarefas não são perdidas mesmo em falhas

Performance: Usuário não precisa aguardar conclusão do scraping

Rastreabilidade: Status das tarefas pode ser monitorado

