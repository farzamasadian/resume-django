# My Django Resume Project

This project is a personal resume website built with Django. It showcases my biography, skills, projects, and contact information. The project is designed to be a professional portfolio, and it can be easily customized for anyone looking to create an online resume.

## Features

Biography Section: Displays personal background information, including educational history and career interests.
Skills Section: Showcases your skills in various technologies and tools.
Projects Section: Lists important personal and professional projects with descriptions and links.
Contact Section: Provides your contact details, including email, phone number, and social media links.
Responsive Design: The website is designed to be fully responsive and looks great on all devices.
Technologies Used

Django: The backend framework used to create the web application.
HTML/CSS/JavaScript: For building and styling the frontend.
Bootstrap: A framework used for responsive and modern design.


Before you begin, ensure you have the following installed on your machine:

Python 3.x
pip (Python package installer)
Git (for version control)


Clone the repository:
git clone https://github.com/farzamasadian/resume-django.git
cd resume-django
Create a virtual environment and activate it:
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
Install the required packages:
pip install -r requirements.txt
Set up the database:
For development, use the default SQLite database.
For deployment on Heroku, use PostgreSQL, and configure it in settings.py.
Run the migrations:
python manage.py migrate
Create a superuser to access the Django admin panel:
python manage.py createsuperuser
Start the development server:
python manage.py runserver
Open the website in your browser: Go to http://127.0.0.1:8000/ to see your resume website.

## Customization

You can customize this project by modifying the views.py and templates to update the content, such as your personal biography, projects, and contact information. You can also update the styles in the CSS files to match your branding or preferred design.
