Sequência para uso do programa
1. > .venv\Scripts\activate
2. Criar arquivo .env na pasta project_manager com as credenciais pro banco
3. > flask run

Sobre a estrutura: O que define um pacote é a existência de um __init__.py, mesmo que vazio
- Pasta app é o programa
- Pacote db: possui a conexão para o db e cada classe dentro dele é o equivalente a um Repository ou DAO
- Pacote home: é o pacote para o path inicial do programa (páginas com "/") #Acho que vou renomear ou reorganizar para ficar mais legivel
- Pacote projeto: é o pacote para o path de projeto ("páginas com "/projeto") #Acho que vou renomear ou reorganizar para ficar mais legivel
- Pacote model: os models das classes
- Pacote service: os services
- __init__py: Inicializa o app com as configurações corretas
- routes.py: exemplo de rotas
