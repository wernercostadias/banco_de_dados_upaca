# Sistema de Gestão de Atividades Diárias para Unidades Prisionais 🚔📋

Este é um sistema desenvolvido para gerenciar as atividades diárias dentro de unidades prisionais. Ele permite a administração de tarefas, registros de atividades e visualização de relatórios.

## 📚 Tabela de Conteúdos
- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

## 🛠️ Tecnologias Utilizadas
- **Django**: Framework Python para desenvolvimento web.
- **SQLite**: Banco de dados utilizado para persistência de dados.
- **Bootstrap**: Framework CSS para criação de interfaces responsivas.

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/wernercostadias/banco_de_dados_upaca.git
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

---

## 📂 Estrutura de Diretórios do Projeto

```bash
banco_de_dados_upaca/
├── manage.py              
├── banco_de_dados_upaca/  
│    ├── __init__.py        
│    ├── settings.py        
│    ├── urls.py            
│    ├── wsgi.py            
│    ├── asgi.py
├── accounts/               # Contém as views e templates relacionados ao sistema de contas
├── media/                  # Diretório para arquivos de mídia
├── painel/                 # Contém as views e templates do painel administrativo
├── static/                 # Arquivos estáticos como CSS e JS
├── staticfiles/            # Arquivos estáticos compilados
├── templates/              # Templates HTML
│    ├── accounts/
│    │    ├── configuracoes_pessoais.html
│    │    ├── create_user.html
│    │    ├── login.html
│    │    ├── logout.html
│    │    ├── user_logged_out.html
│    │    ├── users_online.html
│    ├── bases/
│    │    ├── base.html
│    │    ├── base2.html
│    ├── painel/
│    │    ├── adicionar_pessoa.html
│    │    ├── arquivos.html
│    │    ├── index.html
│    │    ├── informacao.html
│    │    ├── tabela_eletronico.html
│    │    ├── tabela_pdi.html
│    │    ├── tabela_sancao_disciplinar.html
│    │    ├── ver_tabela.html
├── requirements.txt       
└── README.md               # Este arquivo!
