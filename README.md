# Django eCommerce Project

This is a Django-based eCommerce project that allows users to like a product and admin to perform CRUD operation on product.

## Features

- User authentication: Allow users to create accounts, log in, and manage their profiles.
- Product catalog: Display a list of products with details such as name, price, and description.
- Admin panel: Provide an admin interface to manage products, and user accounts.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:SaugatMgr/eCommerce.git
    or
    git clone https://github.com/SaugatMgr/eCommerce.git
    ```

2. Navigate to the project directory:

    ```bash
    cd the-project-directory
    ```

3. Create a virtual environment:
    Note: Since I have used poetry for dependency management it is important that we name our virtual env file .venv otherwise poetry will install packages in it's own venv which we don't want.

    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```

5. Install Poetry:

    ```bash
    pip install poetry
    ```

6. Install project dependencies:

    ```bash
    poetry install
    ```

7. Set up environment variables:

    Set up environment variables in a `.env` file. (like DEBUG, SECRET_KEY, DATABASE_URL, ALLOWED_HOSTS)

8. Apply migrations:

    ```bash
    python manage.py migrate
    ```

9. Run the project:

    You might have to install make if it is not already installed in your system.
    Go to website [https://gnuwin32.sourceforge.net/packages/make.htm](https://gnuwin32.sourceforge.net/packages/make.htm) for windows users and add it to environment variables.
    For linux/ubuntu users: sudo apt install make

    ```bash
    make runserver
    ```

10. Access the project:

    Open a web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the project.

