# Django-Rest-API


#### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd Django_API 
        ```

    2. Select the API Folder:
        ```bash
            $ cd <API!>
        ```
        
    3. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate 
        ```
    4. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    5. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
