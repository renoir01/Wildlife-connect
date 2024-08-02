WildlifeConnect
WildlifeConnect is a web application designed to facilitate wildlife conservation by providing a centralized platform for users to report sightings, engage with the community, and manage conservation efforts.

Table of Contents
Features
Requirements
Installation
Configuration
Usage
Contributing


Features
User authentication and role management (volunteer, researcher, tourist)
Report uploads and management
Community forums
Event creation and management
Requirements
Python 3.10 or later
Django 4.0 or later
PostgreSQL or SQLite
Git
Installation
1. Clone the Repository

git clone https://github.com/yourusername/WildlifeConnect.git
cd WildlifeConnect
2. Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
3. Install Dependencies

pip install -r requirements.txt
4. Set Up the Database
Using PostgreSQL
Install PostgreSQL and create a new database and user.
Update the DATABASES setting in wildlifeconnect/settings.py to match your database configuration.
Using SQLite (default)
No additional configuration is needed. The project is set up to use SQLite by default.

5. Apply Migrations

python manage.py migrate
6. Create a Superuser

python manage.py createsuperuser
7. Collect Static Files

python manage.py collectstatic
8. Run the Development Server

python manage.py runserver
Visit http://127.0.0.1:8000 in your web browser to see the application running.

Configuration
Environment Variables
Create a .env file in the root directory of your project and add the following environment variables:

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost
Settings
You can customize additional settings in wildlifeconnect/settings.py as needed.

Usage
Creating and Managing Users
Sign up for a new account at http://127.0.0.1:8000/signup.
Log in with your account at http://127.0.0.1:8000/login.
Navigate the site using the navigation menu to upload reports, participate in forums, and manage events.
Admin Interface
Access the admin interface at http://127.0.0.1:8000/admin with the superuser credentials you created earlier. Here you can manage users, reports, and other data.

Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push your branch to your fork.
Create a pull request detailing your changes.
