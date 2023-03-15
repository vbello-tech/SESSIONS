SESSIONS- A SESSION SCHEDULING API (ONGOING PROJECT).
========

SESSIONS is a RESTful API that enables users to schedule sessions with business owners that has registered their business on our database.
SESSIONS allows users who are business owners to create business with us with details such as location, opening time, closing time, business type etc.
Users can schedule session with any registered business by sending a request of when (day and time) they would want the session to hold. SESSIONS as been configured to ensure that a business can not have more than one session at a particular time.

- URL - not yet available
- Documentaion - not yet available


Project Stack
------------------

-   Django
-   Django RestFramework
-   PostgreSQL Database 


Installation
------------

Here are the steps to install and set up the Homemix real estate API project locally:

1. Clone the repository: First, you will need to clone the Homemix repository to your local machine. This can be done using the following command in your terminal or command prompt:
    ```bash
    git clone https://github.com/[your-username]/sessions.git
    ```
2. Create a virtual environment: It is recommended to work with a virtual environment to keep the dependencies for this project separate from other projects on your system. To create a virtual environment, run the following command:
    ```bash
    python -m venv homemix-env
    ```
    Activate the virtual environment by running the following command:
    ```bash
    source homemix-env/bin/activate (for Mac or Linux)
    ```

    ```bash
    source homemix-env\Scripts\activate (for Windows)
    ```
3. Install dependencies: Next, you will need to install the dependencies required for the project. These dependencies are listed in the requirements.txt file. To install them, run the following command:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database: The Homemix API uses the Django ORM to interact with a database. By default, the project uses PostgreSQL as the database or you could use any database of your choice. Run these commands to make migrations:
     ```bash
    python manage.py makemigrations
    ```
  
    ```bash
    python manage.py migrate
    ```
5. Create a superuser: To access the Django admin interface, you will need to create a superuser. You can do this by running the following command:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server: Once the installation and setup are complete, you can start the development server by running the following command:
    ```bash
    python manage.py runserver
    ```
  
  The port for  running the project is  http://localhost:8000/.
  
  

