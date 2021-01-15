# vet-dashboard
A dashboard for managing Veterinary Officer records.

## Functionality
- Login page.
- View list of veterinary officers.
- Onboard a veterinary officer.
- Update a veterinary officer's information.
- Deactivate a veterinary officer.
### Local Setup

1. Clone the repo and configure the virtual environment

```
 $ git clone https://github.com/nickmwangemi/vet-dashboard.git
 $ cd vet-dashboard
 $ pip3 install -r requirements.txt
 $ python3 -m venv env
 $ source env/bin/activate
```

2. Build the database, setup superuser account and run local development server instance.

```
 $ python3 manage.py migrate
 $ python3 manage.py createsuperuser
 $ python3 manage.py runserver
```

Crack open the Browsable API available at [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)

Also, Swagger UI documentation is available at [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## Endpoints

| Endpoint                          | HTTP Verb |
| --------------------------------- | --------- |
| /vets                             | GET       |
| /vets/new                         | POST      |
| /vets/new                         | GET       |
| /vets/new                         | POST      |
| /vets/:pk                         | GET       |
| /vets/:pk                         | PUT       |
| /vets/:pk                         | PATCH     |
| /vets/:pk                         | DELETE    |


#

A live version of this project is available at [https://vets-dashboard.herokuapp.com/](https://vets-dashboard.herokuapp.com/). 🚀
