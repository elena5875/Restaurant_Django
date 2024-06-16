# THE FORK RESTAURANT

# Features
This mock restaurant a newly opened restaurant where your palates will be excited to taste the finest and freshest food you'll ever get.
We specialize in desserts and Italian Cuisine. We are also located at the heart of Stockholm City, Sweden.

# Header
The website will have a header with a green background with the following navigation links for the user to see 
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/homepage_django_vn2t75.jpg)


# About Us. 
Is a short preview of what the restaurant is all about. It has a picture of a fork in a round border.It also shows the opening hours of the restaurant with a pictuer of an OPEN word could be seen.
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487147/about_us-django_s9eqbl.jpg)
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/openinghours_django_mwhnbu.jpg)
# Location: 
It will show you the address, tel. number, and email address. User will also be shown how a google map and see where the restaurant is located
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/location_django_c1lzzc.jpg)

# Gallery. 
The user will see some great photo of what the restaurant is serving. It will also show the character and ambiance of the restaurant. If you hover the mouse in the photo it will increase its size to 5%
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710491385/gallery_django2_khq1lp.jpg)
# Menu.
Once the user clicks this navigation tool. It will open into a new page where the user will be shown the full list of what food the restuarant has to offer. It will show the price and what kind of food they prepare in the restaurant.
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/menu-django_idvtfi.jpg)

# Reservation.
This will open up to a new page and the user will be prompted to a site where the user will be asked for its name, email and telephone number. The User can then choose the data, time and how many people will come to eat at the restaurant. Once the user submits the form and has successfully submit it. The user will be prompted with a notice that its reservation has been a success and will await for approval.The approval email is only sent thru a mock email.
The reservation form contains the following :
            Name:
            Email:
            Phone number:
            Date:
            Time: (user gets to choose between 5 pm till 11 pm)
            Number of people (user gets to choose from 1 till 9 people)
        a note will say if more than 9 people are coming please call the restaurant.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/reservationformdjango_yfh2cx.jpg)

# Footer: 
In here you will see the icon of both facebook and instagram. If you click the icons you will be redirected to the restaurant's socila media sites. Another thing the user will see is the copy right of the fork Logo. 
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710491385/footer_django_ytfmgn.jpg)

# Django Administration. 
In the administrial side. The admin gets to approve, delete or reject the reservations done by the customers. An automatic email will be generated once the admin has decide to approve or reject the reservation
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/site_adminreservation_jo6vgd.jpg)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/djangoadmin1_g8eaun.jpg)


![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/delete_approve_reject_fkwjwe.jpg")



# Wireframing
Before I started creating the website I had to visualize first what needs to be done. 
The outline of the website is like this 
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchomepage_azdo6s.jpg)
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchmenu_d909wj.jpg)
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/scketchreservationpage_k8axeu.jpg)



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

## Setup Environment Variables

This project requires some environment variables to be set. You can use the `.env.example` file as a template.

1. Copy the `.env.example` file to `.env`:

   SECRET_KEY=your-secret-key
  DEBUG=True
  DATABASE_URL=postgres://username:password@localhost:5432/mydatabase
  ALLOWED_HOSTS=your-allowed-hosts
  CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name
  CLOUDINARY_API_KEY=your-cloudinary-api-key
  CLOUDINARY_API_SECRET=your-cloudinary-api-secret
  CSRF_TRUSTED_ORIGINS=your-csrf-trusted-origins
  DEFAULT_FROM_EMAIL=your-default-from-email
  EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
  ADMIN_EMAIL=your-admin-email

2. Load the environment variables by running the init_env.sh script:
  ./init_env.sh

3. Verify that the environment variables are set:
  echo $DATABASE_URL
  echo $SECRET_KEY



4. Ensure `init_env.sh` is Correct

Make sure your `init_env.sh` script is set up to load the environment variables.

**Example `init_env.sh` Script:**

```sh
#!/bin/bash
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

Run the script to make it executable

5. Apply migrations and start the server:
  python3 manage.py migrate
  python3 manage.py runserver


6. Ensure your settings.py is correctly set up to read from the environment variables.

7. To run the application use the command 
  python3 manage.py runserver

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



OPENING thru Heroku

1. Install Heroku CLI using this code
  curl https://cli-assets.heroku.com/install.sh | sh
2. Login to Heroku using this code
  heroku login -i
3. You will be asked to enter email and password
  email is elenafreire75@gmail.com
  password is HRKU-3e5a6715-3b88-4520-b0b8-bc3aa1e90124
4. To access the file write the code 
  heroku git:remote -a restaurantdjango
5. Push our code to Heroku using this code 
  git push heroku main
6. To run the code use 
  heroku run bash -a restaurantdjango


# Test
Most of my test were done manually and locally from gitpod

The automated test should some failure with regard to restaurant/models.py code. 
I have yet to address this issue

# Issues
IDE's would sometimes not open or worst my work would just suddenly disappear. 
I used codeanywhere and gitpod but both had alot of issue during the time I was building my website

Due to time constraints, I was not able to link my reservation form to django administration. 
Django administration is working as I want it to be but my reservation form has a lot of issues, namely:
  time: the user was supposed to see a dropdown menu where the user can choose between 5pm till 11 pm
No matter what code I do the dropdown menu would not work in the website but would work in django administration.

  Submit button: When the user clicks the submit button, it should automatically store the data to django admin
     and at the same time create a mock email stating that the reservation has been successful.


# Credits

All my pictures are downloaded from pexel.com
https://www.pexels.com/
And all the pictures were stored in cloudinary account
https://console.cloudinary.com/pm/c-27ce96169f2fa7ccae6699f09c4863/developer-dashboard


# References:
https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
https://www.djangoproject.com/start/
https://learndjango.com/tutorials/django-email-contact-form-tutorial
https://whitenoise.readthedocs.io/en/stable/django.html#use-a-content-delivery-network
https://dev.to/thomz/my-django-heroku-checklist-3p72
https://www.atlassian.com/git/tutorials
https://tutorial.djangogirls.org/en/django_installation/
