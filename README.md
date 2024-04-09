# Django eCommerce Project

This Django-based eCommerce project allows users to like products and administrators to manage products effortlessly.

## Features

- **User Authentication:** Users can create accounts, log in, and manage their profiles.
- **Product Catalog:** Display a list of products with details such as name, price, and description.
- **Admin Panel:** Provides an admin interface to manage products and user accounts.

## Project Structure

The main Django project is managed inside the `core/project_name` directory. The `manage.py` file also resides in the `core/` directory. To run commands, use `python -m core.manage <command_name>` or `make command_name` instead of `python manage.py <command_name>`. The `command_name` for make is inside `Makefile`. This structure is designed to organize project files effectively and improve maintainability.

## Purpose of Using Makefile

To streamline project development and management, a Makefile is included with custom command names. This simplifies executing commands related to Django management, such as running the development server, applying migrations, and installing dependencies.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SaugatMgr/eCommerce.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd the-project-directory
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

4. **Activate the virtual environment:**

    On Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```

5. **Install Poetry:**

    ```bash
    pip install poetry
    ```

6. **Install project dependencies:**

    ```bash
    poetry install
    ```

7. **Set up environment variables:**

    Create a `.env` file in the project root directory and add the following variables:

    ```
    DEBUG=True
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=your_database_url_here
    ALLOWED_HOSTS="localhost,127.0.0.1" or "*"
    ```

8. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

9. **Run the project:**

    Ensure Makefile is installed:
    - For Windows users, download and add Make to environment variables [here](https://gnuwin32.sourceforge.net/packages/make.htm).
    - For Linux/Ubuntu users:

    ```bash
    sudo apt install make
    ```

    Now, run the project:

    ```bash
    make runserver
    ```

10. **Access the project:**

    Open a web browser and go to [http://localhost:8000](http://localhost:8000) to view the project.
