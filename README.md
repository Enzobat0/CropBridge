# CropBridge

CropBridge is a web application designed to be a multivendor marketplace for farmers. This repository contains the codebase for the application.

## Prerequisites

Before you can run this application locally, you need to have the following installed:

- Python 3.10 or later
- pip (Python package installer)
- virtualenv (for creating a virtual environment)

## Setting Up the Project

### Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/CropBridge.git
cd CropBridge```

### Create a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Dependencies

Install the project dependencies using pip:

```bash
pip install -r requirements.txt

### Configure Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```makefile
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

### Apply Migrations

Run the following command to apply the database migrations:

```bash
python manage.py migrate


### Create a Superuser (Optional)

If you want to access the Django admin interface, create a superuser account:

```bash
python manage.py createsuperuser

### Collect Static Files

Collect static files to be served by Django:

```bash
python manage.py collectstatic
### Run the Development Server

Start the development server:

```bash
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/ in your web browser.
