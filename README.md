# django-rest-api
A REST api written in Django for people with deadlines

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/gitgik/django-rest-api.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd task
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ pyton -m virtualenv venv
            $ cd venv/scripts
            $./activate.ps1
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ cd ..
            $ cd ..
            $ cd task
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the Banks api service on your browser by using
    ```
        http://localhost:8000/Bank/
    ```
    **Below**: *Screenshot from the browsable API*
      ![Screenshot][]
  
    You can now access the Branch with branch details using bank ifsc code with api service on your browser by using
    ```
        http://localhost:8000/Branch/?ifsc={bank ifsc code}
    ```
