# car_rental
 # Car Rental Django REST Framework Project

This is a Django-based RESTful API project for a car rental service. It allows users to view available cars, make reservations, and manage car listings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Yeghishe-Arakelyan/car_rental.git
Change to the project directory:
bash
Copy code
cd car-rental-drf
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the project dependencies:
bash
Copy code
pip install -r requirements.txt
Apply database migrations:
bash
Copy code
python manage.py migrate
Create a superuser account to access the Django admin panel:
bash
Copy code
python manage.py createsuperuser
Start the development server:
bash
Copy code
python manage.py runserver
The API will be available at http://localhost:8000/.

Usage
Visit http://localhost:8000/admin/ and log in with the superuser credentials to manage car listings and reservations.
To interact with the API programmatically, you can use tools like curl or Postman.
API Endpoints
List and create cars: /cars/
Retrieve, update, and delete cars: /cars/{car_id}/
List and create reservations: /reservations/
Retrieve, update, and delete reservations: /reservations/{reservation_id}/
Authentication
Authentication is required to access certain API endpoints. Users can register for an account to get an API token. Include the token in the Authorization header of your API requests:

http
Copy code
Authorization: Token your-api-token-here
Documentation
Interactive API documentation is available using drf-yasg. You can access the documentation at http://localhost:8000/swagger/ or http://localhost:8000/redoc/ after starting the development server.

Contributing
Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name
Make your changes and commit them: git commit -m "Your message here"
Push your changes to your fork: git push origin feature-name
Create a pull request against the main branch of the original repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.
