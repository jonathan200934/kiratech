## Installation

Create a virtual environment using venv or conda, then activate your environment

After activated run command below

```sh
pip install -r requirements.txt
python manage.py runserver
```

You can test api endpoint with postman or browser
http://127.0.0.1:8000/inventory
http://127.0.0.1:8000/api/inventory
http://127.0.0.1:8000/inventory/1

## Test

```sh
python manage.py test
```