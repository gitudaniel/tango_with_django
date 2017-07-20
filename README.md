# resourcy
A publicly viewable bookmarks application that makes it easier for others to benefit from your insight.

# To run this app in development settings
Create a virtual environment using virtualenv(https://virtualenv.pypa.io/en/stable/) or virtualenv wrapper(https://virtualenvwrapper.readthedocs.io/en/latest/)

Clone the directory to your local machine

Download pip (https://pip.pypa.io/en/stable/installing/)

Run pip install -r requirements.txt

Run python manage.py makemigrations resourcy (If you want to see what this does, run python manage.py makemigrations --dry-run)

Run python manage.py migrate

At this point you have everything you need to view the app

Run python manage.py runserver --settings=resourcy_project.settings.local


