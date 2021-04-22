# Group Project for USU CS3450

## Setup Instructions

Detailed setup instructions:

you will need to run the parking_api django server and the parking-client react client

## DJANGO SERVER
## Necessary installations

```$ pip install django```

```$ pip install djangorestframework```

```$ pip install djangorestframework_jwt```

```$ pip install django-cors-headers```


## Running instructions
Make sure you are using python3.

```$ python manage.py makemigrations```

```$ python manage.py migrate```

```$ python manage.py runserver```

Check the output to see where it is running on localhost


## REACT CLIENT
##SETUP AND RUN

```$ npm install```

```$ npm start``` or ```yarn start```

Use path /login to log into the system once running.
Use path /register to create a user and log into the system once running.

## Tool Stack Description and Setup Procedure

This project is built using Django and React. Django provides a backend, serving
files and providing database services. React runs on the front end, and provides
more simple and powerful JavaScript extensions.

Django setup Docs:
[https://docs.djangoproject.com/en/3.1/topics/install/#install-the-django-code](https://docs.djangoproject.com/en/3.1/topics/install/#install-the-django-code).

React setup Docs:
[https://create-react-app.dev/docs/getting-started/](https://create-react-app.dev/docs/getting-started/).

### Login Credentials

Using the default migration in Django, the following users are set up:

 - Customer account: username ```austin```, password ```password```,
   logging in at ```localhost:3000/login```.
 - Attendant account: username ```attendant```, password ```password```,
   logging in at ```127.0.0.1:8000/attendant/login```.
 - Lot owner account: username ```LotOwner```, password ```password```,
   logging in at ```127.0.0.1:8000/lot-owners/login```.
 - University admin account: username ```admin```, password ```admin```,
   logging in at ```127.0.0.1:8000/university/login``` or at 
   ```127.0.0.1:8000/admin```.

If you get a notification that you're not authorized for a page, try logging
out (using ```./logout``` if needed) and then logging in as the correct user
type. We are still chasing a weird bug in lot-owners, if you get a CRFS error
try the same thing.

## Requirements

 - Transactions, collecting money, University takes commission
 - Actors: parkers, lot owners, lot attendants, University, supervisor
 - All lots have attendants
 - Prices set by lot owners
 - Phone friendly, no app required
 - Different sizes of parking spots (mobile homes, large sites for tailgating, etc.)
 - QR codes required for authentication on the spot

## Organization

The workspace is organized as follows:

 - Documentation is contained in the ```docs/``` folder.
 - Videos are in ```docs/video```.
 - Source code is contained in the ```Apps/``` folder, and each project (client
   side, server side, test suites etc.) are in their own folders.

## Version Control

### Collaboration

All team members are contributors as far as the GitHub system is concerned. When
this project begins in earnest, all individual work will be done on seperate
branches. Merge conflicts will be discussed in Slack and resolved in team
meetings.

## Unit Testing Instructions

Test suites, when they're available, will be run from their own directories
under ```Apps/```. The test suites here will automatically check that the database
will accept new information and CRUD operations, that running the servers works
correctly, and so on.

## System Testing Instructions

 - Testing login: use invalid credentials and make sure you get an error code,
   use valid login and ensure that the correct user is displayed with the correct
   privileges
 - Log in and ensure that deleted information stays deleted, changed information
   stays changed, and that untouched information remains the same.
 - Login as each of the user groups and ensure that the correct interface is shown
   for each.