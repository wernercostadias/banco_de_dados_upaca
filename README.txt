# Sistema de Gestão de Atividades Diárias para Unidades Prisionais

Este é um sistema desenvolvido para gerenciar as atividades diárias dentro de unidades prisionais. Ele permite a administração de tarefas, registros de atividades e visualização de relatórios.

## Tabela de Conteúdos
1- [Descrição](#descrição)
2- [Tecnologias Utilizadas](#tecnologias-utilizadas)
3- [Como Rodar o Projeto](#como-rodar-o-projeto)
4- [Estrutura de Diretórios](#estrutura-de-diretórios)
5- [Como Contribuir](#como-contribuir)
6- [Licença](#licença)

## Tecnologias Utilizadas
- **Django**: Framework Python para desenvolvimento web.
- **SQLite**: Banco de dados utilizado para persistência de dados.
- **Bootstrap**: Framework CSS para criação de interfaces responsivas.

## Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/nome-do-repositorio.git
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Linux/Mac
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Rode as migrações para configurar o banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

6. Acesse o projeto no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura de Diretórios
banco_de_dados_upaca/
├── manage.py              
├── banco_de_dados_upaca/  
│   ├── __init__.py        
│   ├── settings.py        
│   ├── urls.py            
│   ├── wsgi.py            
│   ├── asgi.py            
├── requirements.txt       
└── README.md              
