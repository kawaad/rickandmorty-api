# rickandmorty-api
API for data extracted from the Rick and Morty API (https://rickandmortyapi.com/)

## Prerequisites

- Python 3.10
- Pip
- Git
- MySQL

## rickandmorty API installation

### Clone the repository
- `$ git clone git@github.com:kawaad/rickandmorty-api.git `
- `$ cd rickandmorty-api `

### Virtual Environment

- `$ pip install virtualenv `
- `$ virtualenv venv `
- `$ source venv/bin/activate`

### Install dependencies
`$ pip install -r requirements.txt `


## Run rickandmorty API

### Config database
`$ python manage.py migrate `

### Run server
`$ python manage.py runserver`

### Access the API at `http://127.0.0.1:8000/`.


## Licence

This project is licensed under the MIT License.