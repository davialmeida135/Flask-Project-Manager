Sequência para uso do programa
1. > .venv\Scripts\activate
2. Criar arquivo .env na pasta project_manager com as credenciais pro banco
3. > flask run

Sobre a estrutura: O que define um pacote é a existência de um __init__.py, mesmo que vazio
- Pasta app é o programa
- Pacote db: possui a conexão para o db e cada classe dentro dele é o equivalente a um Repository ou DAO
- Pacote routes: define as rotas e visões
- Pacote model: os models das classes
- Pacote service: os services
- __init__py: Inicializa o app com as configurações corretas
- rotas.py: exemplo de rotas
