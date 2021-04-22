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
make sure you are using python3

```$ python manage.py makemigrations```

```$ python manage.py migrate```

```$ python manage.py runserver```

 check the output to see where it is running on localhost


 ## REACT CLIENT
 ##SETUP AND RUN

```$ npm install```

```$ yarn start```

 use path /login to log into the system once running
 use path /register to create a user and log into the system once running



## Tool Stack Description and Setup Procedure

This project is built using Django and React. Django provides a backend, serving
files and providing database services. React runs on the front end, and provides
more simple and powerful JavaScript extensions.

Django setup Docs:
[https://docs.djangoproject.com/en/3.1/topics/install/#install-the-django-code](https://docs.djangoproject.com/en/3.1/topics/install/#install-the-django-code).

React setup Docs:
 [https://create-react-app.dev/docs/getting-started/](https://create-react-app.dev/docs/getting-started/).

## Projects

There are three project boards currently, one will be used for each stage. The others are used as backlogs until we reach that stage.

## Wiki

There is a GitHub Wiki initialized, but it is currently empty. Perhaps eventually
it will be used for documentation and other customer-facing information.

## Requirements

 - Transactions, collecting money, University takes commission
 - Actors: parkers, lot owners, lot attendants, University, supervisor
 - All lots have attendants
 - Prices set by lot owners
 - Prices set by lot owner
 - Phone friendly, no app required
 - Different sizes of parking spots (mobile homes, large sites for tailgating, etc.)
 - QR codes required for authentication on the spot

## Organization

The workspace is organized as follows:

 - Documentation is contained in the ```docs/``` folder
 - Source code is contained in the ```Apps/``` folder, and each project (client
   side, server side, test suites etc.) are in their own folders.

## Version Control

### Version Numbering

All version control numbers are of the following format:

v0.1.2b

The last digit, 2b, signifies that this version contains the second small
feature update (2) and the second iteration (b) of the first major version
update (1) of the first major version (0) of the app.

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

## Prototypes

Prototype 1, located at [/Apps/prototype1](https://github.com/colewebb/group-8/tree/master/Apps/prototype1),
is a low-fidelity design rendered by Austin in Adobe XD. This prototype shows a
possible customer interface, designed to work equally well on mobile and desktop
devices. The root is located at
[/Apps/prototype1/Splash.png](https://github.com/colewebb/group-8/tree/master/Apps/prototype1/Splash.png).

Prototype 2, located at [/Apps/prototype2](https://github.com/colewebb/group-8/tree/master/Apps/prototype2),
is a high-fidelity design rendered by Cole in HTML/CSS. This prototype suggests
an interface for adding a new lot to the website from lot owner/administrator
perspective. This prototype contains experimental support for dark mode (to
enable, switch from ```assets/styles.css``` to ```assets/styles-dark.css```).
The root is located at
[/Apps/prototype2/index.html](https://github.com/colewebb/group-8/tree/master/Apps/prototype2/index.html).

Prototype 3, located at [/Apps/prototype3](https://github.com/colewebb/group-8/tree/master/Apps/prototype3),
is a low-fidelity design rendered by Cole in ASCII art. This prototype is an
alternative design for the customer interface, focused on a mobile interface
with notes on adaptivity for other form factors. The root is located at
[/Apps/prototype3/index.md](https://github.com/colewebb/group-8/tree/master/Apps/prototype3/index.md).
