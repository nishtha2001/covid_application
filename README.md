Tech Stack:
Front-end : html,css,bootstrap <br>
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

->>> Create a Django project and app:</br>
Install Django using:</br>
"pip install django"</br>
Create a new Django project using: </br>
"django-admin startproject myproject"</br>
Change into the project directory:</br>
"cd myproject"</br>
Create a new Django app using:</br>
"python manage.py startapp vaccination"</br>

->>> Designing the database:</br>
In the models.py file of the app,  the models for the users, vaccination centers, and vaccinations are defined.</br>
User model contains fields for username, password, and role (admin or user).</br>
VaccinationCenter model contains fields for the name, location, and capacity.</br>
Vaccination model contains fields for the user, vaccination center, and date.</br>

Run the following command to create the database table:</br>
 "python manage.py makemigrations" and then "python manage.py migrate"</br>
 
 
 ->>>Creating  the views:</br>
In the views.py file of the app, create the views for handling the user and admin use cases.</br>
For the user cases we have:</br>
a view for the login page, a view for the signup page, a view for searching for vaccination centers, a view for applying for vaccination, and a view for logging out.</br>
For the admin use cases we have:</br>
a view for adding vaccination centers, a view for getting dosage details, and a view for removing vaccination centers.</br>


->>>Creating  the templates:</br>
In the templates directory of the app, create the HTML templates for the views.</br>
you can create a template for the login page, a template for the signup page etc.</br>
Using HTML, CSS, and Bootstrap to design the templates and make them responsive.</br>


->>Creating the URLs:</br>
In the urls.py file of the app, create the URLs for the views.</br>
we have a URL for the login page, a URL for the signup page, a URL for the search results page, etc.</br>


->>>Test the application:</br>
Run the Django development server using python manage.py runserver</br>
Open a web browser and navigate to the URLs of the views to test the application.</br>
