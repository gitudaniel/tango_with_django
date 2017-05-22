# tango_with_django
Based off of the book Tango with Django that teaches Django workflows


# To run this app
Create a virtual environment using virtualenv(https://virtualenv.pypa.io/en/stable/) or virtualenv wrapper(https://virtualenvwrapper.readthedocs.io/en/latest/)

Clone the directory to your local machine

Download pip (https://pip.pypa.io/en/stable/installing/)

Run pip install -r requirements.txt

Run python manage.py makemigrations rango (If you want to see what this does, run python manage.py makemigrations --dry-run)

Run python manage.py migrate

Then run python populate_rango.py -> This is a population script to load some data to the application

At this point you have everything you need to view the app

Run python manage.py runserver


