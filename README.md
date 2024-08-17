# Projeto Escuta

Este é um projeto Django que utiliza várias APIs externas para fornecer funcionalidades avançadas.

Projeto deployado: https://karolinefarias23.pythonanywhere.com/

## Requisitos

- Python 3.10
- Django
- requests
- assemblyai
- python-decouple
- google-generativeai

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/projeto-escuta.git
    cd projeto-escuta
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # No Windows
    # source venv/bin/activate  # No Linux/Mac
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente:
    Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
    ```env
    AA_API_KEY=your_assemblyai_api_key
    GEMINI_KEY=your_gemini_api_key
    # EMAIL_HUGCHAT=your_email_for_hugchat
    # PASSWD_HUGCHAT=your_password_for_hugchat
    ```

## Uso

1. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

2. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

3. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Funcionalidades

- Integração com AssemblyAI para processamento de áudio.
- Integração com Google Generative AI.
- (Comentado) Integração com HuggingChat.

## Estrutura do Projeto

- [`views.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fkdemo%2FDocuments%2FDoutorado%2Fdisciplinas%2FEngenharia%20de%20Software%2Fprojeto-escuta%2Fescuta%2Fpacientes%2Fviews.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\kdemo\Documents\Doutorado\disciplinas\Engenharia de Software\projeto-escuta\escuta\pacientes\views.py"): Contém as views da aplicação.
- [`forms.py`](command:_github.copilot.openSymbolFromReferences?%5B%22forms.py%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ckdemo%5C%5CDocuments%5C%5CDoutorado%5C%5Cdisciplinas%5C%5CEngenharia%20de%20Software%5C%5Cprojeto-escuta%5C%5Cescuta%5C%5Cpacientes%5C%5Cviews.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fkdemo%2FDocuments%2FDoutorado%2Fdisciplinas%2FEngenharia%2520de%2520Software%2Fprojeto-escuta%2Fescuta%2Fpacientes%2Fviews.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fkdemo%2FDocuments%2FDoutorado%2Fdisciplinas%2FEngenharia%20de%20Software%2Fprojeto-escuta%2Fescuta%2Fpacientes%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition"): Contém os formulários utilizados na aplicação.
- [`settings.py`](command:_github.copilot.openSymbolFromReferences?%5B%22settings.py%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ckdemo%5C%5CDocuments%5C%5CDoutorado%5C%5Cdisciplinas%5C%5CEngenharia%20de%20Software%5C%5Cprojeto-escuta%5C%5Cescuta%5C%5Cpacientes%5C%5Cviews.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fkdemo%2FDocuments%2FDoutorado%2Fdisciplinas%2FEngenharia%2520de%2520Software%2Fprojeto-escuta%2Fescuta%2Fpacientes%2Fviews.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fkdemo%2FDocuments%2FDoutorado%2Fdisciplinas%2FEngenharia%20de%20Software%2Fprojeto-escuta%2Fescuta%2Fpacientes%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A17%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Configurações do Django.
- `urls.py`: Rotas da aplicação.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.