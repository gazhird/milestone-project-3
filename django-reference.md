

## Create Workspace in IDE 

create folder on windows home screen and open in VS code
create a blank README.md
Use Source Control to link to github (icon on left)



## Create Environment    

Open settings (gear cog Bottom left of VS code)
click 'Command Palette'

click python create enviroment (top center)
Click Venu 
Click Python 


## install Packages 

pip3 install Django~=4.2.1

<!-- Isolates extensions from github  -->
pip3 freeze --local > requirements.txt


## Creating a Django Project

django-admin startproject my_project .


<!-- Check server works -->
py manage.py runserver


## Git ignore 

<!-- Create file called .gitignore and add .venv to it. -->
.venv/


## Creating a Django App 

py manage.py startapp hello_world



## app/views.py

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("hello, test!")


## project/urls.py 

<!-- the def name 'hello_world' from app/views.py   -->
from hello_world import views as index_views

path('', index_views.index, name='index'),


## project/settings.py

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com']

<!-- add app name to list -->
INSTALLED_APPS = [ 'new_app_name', ]


## Testing app 
<!-- Check server works -->

py manage.py runserver



--------------------------------------------------------------

## create database from PostgreSQL 

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101N+6/courseware/713441aba05441dfb3a7cf04f3268b3f/0758f42698bf498382b68a9cb8e72483/?child=first


## env.py

create new file called env.py
add env.py to .gitignore 

<!-- within env.py import pythons os and set value as 'your db link' -->

import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>")


## pip install packages for PostgreSQL

pip3 install dj-database-url~=0.5 psycopg2~=2.9

<!-- freeze for requirements  -->
pip3 freeze --local > requirements.txt

<!-- psycopg2 is a driver for interacting with PostgreSQL databases using Python. The dj-database-url Python package is a utility to connect Django to a database using a URL. -->

## project/settings.py 

<!-- connect the settings.py file to the env.py file: -->

from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

 <!-- comment out the local sqlite3 database connection. -->

<!-- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} -->

<!-- add following,  no pasting the db here url required -->

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


## Migrate 

<!-- Now that your project is connected to the database, you can create database tables with Django's migrate command: -->

py manage.py migrate


------------------------------------------------------------------------


## Migrate removal reset

<!-- When you change data type of a input  -->

py manage.py migrate blog zero


------------------------------------------------------------------------



## Super User 

py manage.py createsuperuser

<!-- Choose a memorable user name, use your email address and choose a secure password. -->

---------------------------------------------

# Secret Key 

<!-- make up your own secret key password -->

# env.py 

import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>")
os.environ.setdefault("SECRET_KEY", "<your_choice_of_secret_key>")

# settings.py

SECRET_KEY = os.environ.get("SECRET_KEY")

# heroku 

key: SECRET_KEY

VALUE: (the made up password from env)


-----------------------------------------------------------

## Heroku 

key: DISABLE_COLLECTSTATIC

value: 1

------

key: DATABASE_URL

value: "link from PostgreSQL"



-----------------------------------------------------------

## Create the model code

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101N+6/courseware/713441aba05441dfb3a7cf04f3268b3f/0758f42698bf498382b68a9cb8e72483/?child=first

<!-- Open your app/models.py file. Add a new import at the top for the User model. -->
<!-- then add table fields below -->

from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)



## adding images in models with Cloudinary


install these:
pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15


Freeze:
pip3 freeze --local > requirements.txt


sign into cloudinary - gazhird -> C.

copy the Cloudinary API


# env.py

os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://<your_api_key>:<your_api_secret>@dffpy8aov")

-----

# project/settings.py 

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary', ]

# app/models.py

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


featured_image = CloudinaryField('image', default='placeholder')


#  app/admin.py

from .models import model-name

admin.site.register(model-name)


# project/settings.py

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]



----------------------------------------------------------------------------------


blog/templates/blog/index.html file

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101N+6/courseware/713441aba05441dfb3a7cf04f3268b3f/0b5c6f09dcfd40fa99a9d68622d62b40/


-----------------------------------------------------------------------------------
## Use the model to update the database

py manage.py makemigrations blog

<!-- Note: A app/migrations/0001_initial.py file is created containing the instructions on what table to build. -->

<!-- Now we need to create that table in the database. -->

py manage.py migrate blog

<!-- Open the blog/admin.py file, import the Post model and register it -->

from .models import Post

admin.site.register(Post)

<!-- Open the codestar/settings.py file and add the following code. -->

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]

# make folders in a folder 

<!-- makes a folder called templates with a folder called blog in a existing folder called blog  -->

mkdir -p blog/templates/blog

# Summernote package 

pip3 install django-summernote~=0.8.20.0

## load json data to db from a file named posts

<!-- by default, e.g. blog/fixtures/posts.json -->

py manage.py loaddata posts

## check python version 

py -V

















git add --all
git commit -m "enable serving of static files"
git push origin main







## powershell / heroku migrations 

press windows + x 

use cd to move to project folder

cd C:\Users\GazHi\OneDrive\Desktop\wheels

heroku login

git add .

git commit -m "update migrations"

git push heroku main 

## fake zero and reapply (relation errors)

py manage.py migrate listings zero
py manage.py migrate listings




<!-- asgiref==3.10.0
certifi==2025.10.5
charset-normalizer==3.4.4
cloudinary==1.36.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==4.2.26
django-cloudinary-storage==0.3.0
gunicorn==20.1.0
idna==3.11
psycopg2==2.9.11
requests==2.32.5
setuptools==80.9.0
six==1.17.0
sqlparse==0.5.3
tzdata==2025.2
urllib3==1.26.20 -->





