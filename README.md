# payments_backend

Este é um backend de pagamento construído usando Python e Django. Ele fornece uma API para gerenciar pagamentos e usuários.

## Recursos

- **Gerenciamento de Pagamentos:** Criação, atualização e listagem de pagamentos.
- **Autenticação:** Usa o modelo de autenticação embutido do Django.
- **Administração:** Interface de administração para gerenciar pagamentos.

## Como Configurar

1. **Clonar o Repositório:**

   ```bash
   git clone <URL-do-repositório>
   ```

2. **Criar e Ativar Ambiente Virtual:**

    ```bash
    python -m venv venv
    No Windows: .\venv\Scripts\activate
    ```

3. **Instalar as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Executar Migrações:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Criar um Superusuário:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Executar o Servidor de Desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

# Uso

- **Administração:** Acesse <http://127.0.0.1:8000/admin> para gerenciar pagamentos e usuários.
- **API:** Use <http://127.0.0.1:8000/api/payments/> para acessar os endpoints de pagamento.

# Contribuição

Contribuições são bem-vindas! Por favor, abra um issue ou envie um _pull request_.

___

# payments_backend

This is a payment backend built using Python and Django. It provides an API for managing payments and users.

## Features

- **Payment Management:** Create, update, and list payments.
- **Authentication:** Uses Django's built-in authentication model.
- **Administration:** Admin interface for managing payments.

## How to Set Up

1. **Clone the Repository:**

   ```bash
   git clone <repository-URL>
   ```

2. **Create and Activate Virtual Environment:**

    ```bash
    python -m venv venv
    No Windows: .\venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

# Usage

- **Administration:** Go to <http://127.0.0.1:8000/admin> to manage payments and users.
- **API:** Use <http://127.0.0.1:8000/api/payments/> to access payment endpoints.

# Contribution

Contributions are welcome! Please open an issue or submit a _pull request_.
