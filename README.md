Tech Stack:
Front-end : html,css,bootstrap
Back-end : Django

Types of Users:
User
Admin

User Use cases:
- login
- signup
- search for Vaccination centre
- apply for vaccination 
- logout

Admin Use Cases
- login (for admin use separate UI)
- Add Vaccination centres
- Get dosage details (group by centres)
- Remove vaccination centres


To create a web application for COVID vaccination, you can follow the steps below:

->>> Create a Django project and app:
Install Django using:
"pip install django"
Create a new Django project using: 
"django-admin startproject myproject"
Change into the project directory:
"cd myproject"
Create a new Django app using:
"python manage.py startapp vaccination"

->>> Designing the database:
In the models.py file of the app,  the models for the users, vaccination centers, and vaccinations are defined.
User model contains fields for username, password, and role (admin or user).
VaccinationCenter model contains fields for the name, location, and capacity.
Vaccination model contains fields for the user, vaccination center, and date.

Run the following command to create the database table:
 "python manage.py makemigrations" and then "python manage.py migrate"
 
 
 ->>>Creating  the views:
In the views.py file of the app, create the views for handling the user and admin use cases.
For the user cases we have:
a view for the login page, a view for the signup page, a view for searching for vaccination centers, a view for applying for vaccination, and a view for logging out.
For the admin use cases we have:
a view for adding vaccination centers, a view for getting dosage details, and a view for removing vaccination centers.


->>>Creating  the templates:
In the templates directory of the app, create the HTML templates for the views.
you can create a template for the login page, a template for the signup page etc.
Using HTML, CSS, and Bootstrap to design the templates and make them responsive.


->>Creating the URLs:
In the urls.py file of the app, create the URLs for the views.
we have a URL for the login page, a URL for the signup page, a URL for the search results page, etc.


->>>Test the application:
Run the Django development server using python manage.py runserver
Open a web browser and navigate to the URLs of the views to test the application.
