


## Django Vehicle database listings project, deployed on Heroku 


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

<!-- Create a new file in your project called .gitignore and add .venv to it. -->

.venv/

## Creating a Django App 

py manage.py startapp hello_world

<!-- Add the new app to the list of installed apps in the projects settings.py file. -->


## Creating views 

<!-- In hello_world/views type -->

from django.http import HttpResponse


## creating URLS 

<!-- In my_project /urls.py type  -->
from hello_world import views as index_views

<!-- Above the admin pattern in urlpatterns, add: -->
path('', index_views.index, name='index'),


## settings.py
<!-- connect the app to the project -->

open my_project/settings.py file
find the INSTALLED_APPS list
Append 'APP_NAME', to the end of the list of INSTALLED_APPS


## Testing app 
<!-- Check server works -->

py manage.py runserver




## Migrate 

<!-- Now that your project is connected to the database, you can create database tables with Django's migrate command: -->

py manage.py migrate

## Migrate removal reset

<!-- When you change data type of a input  -->

py manage.py migrate blog zero

## Super User 

python3 manage.py createsuperuser

<!-- Choose a memorable user name, use your email address and choose a secure password. -->


## Create the model code

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