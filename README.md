# THE FORK RESTAURANT

# Features
This mock restaurant a newly opened restaurant where your palates will be excited to taste the finest and freshest food you'll ever get.
We specialize in desserts and Italian Cuisine. We are also located at the heart of Stockholm City, Sweden.

# Header
The website will have a header with a green background with the following navigation links for the user to see 
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/homepage_django_vn2t75.jpg")


# About Us. 
Is a short preview of what the restaurant is all about. It has a picture of a fork in a round border.It also shows the opening hours of the restaurant with a pictuer of an OPEN word could be seen.
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487147/about_us-django_s9eqbl.jpg")
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/openinghours_django_mwhnbu.jpg")
# Location: 
It will show you the address, tel. number, and email address. User will also be shown how a google map and see where the restaurant is located
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/location_django_c1lzzc.jpg")

# Gallery. 
The user will see some great photo of what the restaurant is serving. It will also show the character and ambiance of the restaurant. If you hover the mouse in the photo it will increase its size to 5%
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710491385/gallery_django2_khq1lp.jpg")
# Menu.
Once the user clicks this navigation tool. It will open into a new page where the user will be shown the full list of what food the restuarant has to offer. It will show the price and what kind of food they prepare in the restaurant.
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/menu-django_idvtfi.jpg")

# Reservation.
This will open up to a new page and the user will be prompted to a site where the user will be asked for its name, email and telephone number. The User can then choose the data, time and how many people will come to eat at the restaurant. Once the user submits the form and has successfully submit it. The user will be prompted with a notice that its reservation has been a success and will await for approval.The approval email is only sent thru a mock email.
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/reservationformdjango_yfh2cx.jpg")

# Footer: 
In here you will see the icon of both facebook and instagram. If you click the icons you will be redirected to the restaurant's socila media sites. Another thing the user will see is the copy right of the fork Logo. 
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710491385/footer_django_ytfmgn.jpg")

# Django Administration. 
In the administrial side. The admin gets to approve, delete or reject the reservations done by the customers. An automatic email will be generated once the admin has decide to approve or reject the reservation
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/site_adminreservation_jo6vgd.jpg")

![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/djangoadmin1_g8eaun.jpg")


![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/delete_approve_reject_fkwjwe.jpg")


# The Reservation Form. 
The reservation form contains the following :
            Name:
            Email:
            Phone number:
            Date:
            Time: (user gets to choose between 5 pm till 11 pm)
            Number of people (user gets to choose from 1 till 9 people)
        a note will say if more than 9 people are coming please call the restaurant.

# Inception.
Before I started creating the website I had to visualize first what needs to be done. 
The outline of the website is like this 
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchomepage_azdo6s.jpg")
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchmenu_d909wj.jpg")
![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/scketchreservationpage_k8axeu.jpg")


# Directory
The directory of the website should look like this 

restaurant_django/
│
├── mainproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│   └── asgi.py
│
├── templates/
│   ├── home.html  
│   ├── navigation.html
│   ├── menu.html
│   ├── reservation.html
│   ├── contacts..html
│   ├── reservation_approved_email.html
│   ├── reservation_rejected_email.html
│   ├── reservation_success.html
│	
│
├── static/
│   └── css/
│       ├── styles.css   
│       ├──about.css
│       ├──gallery.css
│       ├──location.css
│       ├──menu.css
│       ├──location.css
│       └──siccess.css
│
│   └──js
│      ├──script.js
│	    ├── reservation.js
│
│
│└── restaurant/
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── migrations/
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    ├──views.py   
│    ├── forms.py
│    ├──models.py
│    ├──apps.py
│    ├──admin.py
│
│
├──manage.py
├──env.py
├──requirements
├──Procfile




# Dependencies
The project relies on several tools and packages to function properly. Here's a list of the main dependencies:
   Django
   Heroku
   Gitpod 
   Github
   cloudinary
   posrtgreSQL

Additionally, the project utilizes the following Python packages/modules:
   django-crispy-form
   django-environ
   django-extensions
   gunicorn
   whitenoise
   psycopg2

# INSTALLATION and DEPLOYMENT
Before getting started, make sure you have the following:

- A GitHub account
- A Gitpod account 
- A Heroku account
- A Cloudinary account
- Access to a PostgreSQL database

IDE was gitpod. I started with the following steps to install everything
1. Create a New Directory
2. Navigate to the Project Directory
3. Initialize Git Repository
4. Install Dependencies
5. Create env.py
6. Set Up Cloudinary and PostgreSQL
7. Create Project Files
8. Start Coding
9. Commit Changes
    using git add .
          git commit -m "initial commit"
          git push
    *before you push make sure debug is set to False
10. Deploy to Heroku

Here is the Url from heroku
djagnoresto-267ab1695d73.herokuapp.com

If you want to deploy locally here is the Url
8000-elena5875-restaurantdja-3bsxhmvzmgn.ws-eu108.gitpod.io

# Credits

All my pictures are downloaded from pexel.com
https://www.pexels.com/


# References:
https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
https://www.djangoproject.com/start/
https://learndjango.com/tutorials/django-email-contact-form-tutorial
https://whitenoise.readthedocs.io/en/stable/django.html#use-a-content-delivery-network
https://dev.to/thomz/my-django-heroku-checklist-3p72
https://www.atlassian.com/git/tutorials
https://tutorial.djangogirls.org/en/django_installation/