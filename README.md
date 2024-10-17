# THE FORK RESTAURANT

# Features

This mock restaurant a newly opened restaurant where your palates will be excited to taste the finest and freshest food you'll ever get.
We specialize in desserts and Italian Cuisine. We are also located at the heart of Stockholm City, Sweden.

# Wireframing

Before I started creating the website I had to visualize first what needs to be done. 
The outline of the website is like this 

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchomepage_azdo6s.jpg)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/sketchmenu_d909wj.jpg)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/scketchreservationpage_k8axeu.jpg)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718783913/format_for_review_a8xnyb.png)




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



IDE used is gitpod. I started with the following steps to install everything

1. Create a New Directory

    -mkdir my_django_project
    -cd my_django_project


2. Initialize Git Repository

    -git init

3. Set Up Virtual Environment and Install Dependencies

    -python3 -m venv venv

    -source venv/bin/activate

    -pip install django psycopg2-binary cloudinary django-environ gunicorn

4. Set Up Cloudinary and PostgreSQL Accounts

    -Sign up for Cloudinary and get your cloud name, API key, and API secret.

    -Sign up for PostgreSQL (e.g., on ElephantSQL) and get your database URL.

6. Create env.py with the following environment variables
    env.py
    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_URL=postgres://siuytvjs:FS4uTNpAhVt7_DUlJlZBAMazj_k5flvQ@cornelius.db.elephantsql.com/siuytvjs
    ALLOWED_HOSTS=*
    CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name
    CLOUDINARY_API_KEY=your-cloudinary-api-key
    CLOUDINARY_API_SECRET=your-cloudinary-api-secret
    CSRF_TRUSTED_ORIGINS=https://8000-elena5875-restaurantdja-vfwg9p1t2ot.ws-eu114.gitpod.io
    GITPOD_WORKSPACE_URL=https://8000-elena5875-restaurantdja-vfwg9p1t2ot.ws-eu114.gitpod.io
    DEFAULT_FROM_EMAIL=theforkrestaurant@yahoo.com
    EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
    ADMIN_EMAIL=theforkrestaurant@gmail.com

7. Create Project Files

8. Start Coding

9. Commit Changes

    -using git add .

    -git commit -m "initial commit"

    -git push

    *before you push make sure debug is set to False



OPENING  Heroku thru CLI

1. Install Heroku CLI using this code

  curl https://cli-assets.heroku.com/install.sh | sh

2. Login to Heroku using this code

  heroku login -i

3. You will be asked to enter email and password

    email is elenafreire75@gmail.com

    password is HRKU-3e5a6715-3b88-4520-b0b8-bc3aa1e90124

4. To access the file write the code 

    heroku git:remote -a djagnoresto

5. Push our code to Heroku using this code 

    git push heroku main

6. To open the app write

    heroku open

Deploy to Heroku manually 

Here is the Url from heroku

    https://djagnoresto-267ab1695d73.herokuapp.com/

Deploying app locally

If you want to deploy locally here is the Url

    https://8000-elena5875-restaurantdja-hlvxl9n5m7u.ws-eu114.gitpod.io/


## To get inside the Django Admin 

1. Copy paste the Url

    https://8000-elena5875-restaurantdja-hlvxl9n5m7u.ws-eu114.gitpod.io/admin/

2. You will be asked to log in. As a user you can use

    Username: Elena

    Password: elenagwapa5804

3. Once you are inside the Admin. You will be able to see 

    Groups

    User

    Comments

    Reservation 

    Review.

4. You can now edit by either delete, approve or reject both reservation and review. In 
Review you can also add comments and post the review and comments to the website.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/django_admin2_aneh6w.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718783246/reservation_admin_q2mcoj.png)

# Here is the Result of the Fork Restaurant

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

# Review.

The user will also see a review and comments section after the gallery. The user will be able to see the comments and reviews from previous users who ate in the restaurant.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781594/reviews_fkygbh.png)

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

            Time: (user gets to choose between 3 pm till 11 pm)

            Number of people (user gets to choose from 1 till 9 people)

        a note will say if more than 9 people are coming please call the restaurant.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718782752/toppage_cpy0za.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781594/successful_email_sent_dcviwx.png)


# Write a Review

Once the user clicks this icon, the user will be brought to another page where the user needs to input its name and a valid email address. The user can then write a comment about the experience he/she encountered while eating at the restaurant. 

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718782894/write_a_review_gnm3ha.png)


# Footer: 

In here you will see the icon of both facebook and instagram. If you click the icons you will be redirected to the restaurant's socila media sites. Another thing the user will see is the copy right of the fork Logo. 

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710491385/footer_django_ytfmgn.jpg)

# Django Administration
. 
In the administrial side. The admin gets to approve, delete or reject the reservations done by the customers. An automatic email will be generated once the admin has decide to approve or reject the reservation

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/django_admin2_aneh6w.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/mock_email2_skipri.png)

![Alt text]("https://res.cloudinary.com/dh5i9qtjf/image/upload/v1710487146/delete_approve_reject_fkwjwe.jpg")

The administration will also be able to approve, delete, post, reject and comment on the reviews written by the user based on their experience while at the restaurant.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/email_for_approved_review_trjcpy.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/email_for_approved_review_trjcpy.png)



## Mock Email.

In the Django Admin, I created a mock email wherein when the admin either rejects, approves, or post a review or reservation
an email is automatically sent to the customer. The mock email can be seen on the terminal in github or in the logs --tail in heroku.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718783246/reviewadmin_wyquss.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/email_for_approved_review_trjcpy.png)




# Test
Most of my test were done manually using python3 manage.py runserver code to run the program and manually test all the forms in the website. I have also test my website in Heroku by either manually deploying it or thru Heroku CLI.

The automated test I did was only using the python manage.py test. Which showed the following:

django was having issues connecting to PostPostgreSQL database on ElephantSQL when running the tests.
solution:
I have address the issue by making some changes in the settings.py., utils.py and test.py.
 
I have tested the reservation form which has shown no issues. 

While in my Review form, it has shown

one issue which is AssertionError: False is not true : Couldn't find 'There was an error with your submission. 

Please correct the errors below.' in response. I tried to correct the issue but so far 

I have corrected the issue and was able to pass the test on both reservation and review forms

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/runtest_lkgppm.png)

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718781593/approved_test_reservation_yspr5x.png)


# Validation

I have run some of the CSS file thru W3 validtor and showed no issues with the code

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718788101/cssvalidation_e2zxnp.png)

While I tried to validate my html file using also W3 validator and it had alot of errors showing. From research it shows that W3 validator could not evaluate Django template tag works hence the
errors in validation. When I ignore these errors, it will show that there are no errors in my html code for home.html.

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718788101/htmlvalidatonwitherrors_dore1h.png)

validation ignoring the errors
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718788101/htmlvalidationnoerrors_zjxhex.png)

I also validated my Js codes and it showed no issues in jshint validator

![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1718788127/scriptvalidation_lfcsdl.png)

# Screen Responsive

I tested the webpage for screen responsive and the webpage responds well to different screen types.
For smaller screen the user can slide the webpage horizontally to see all the navigation menu.
However, in phone screens in order to see the navigation menu bar it needs to be in a landscape mode and 
it can also slide horizontally to see the complete navigation menu.

picture of screen responsive for the webpage
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1719220076/responsive_screenshot_smdxc1.png)

For phone screens in landscape mode
![Alt text](https://res.cloudinary.com/dh5i9qtjf/image/upload/v1719220223/Screenshotforphonescreens_v0vm5v.png)



# Issues
IDE's would sometimes not open or worst my work would just suddenly disappear. 
I used codeanywhere and gitpod but both had alot of issue during the time I was building my website

Due to time constraints, I was not able to link my reservation form to django administration. 
Django administration is working as I want it to be but my reservation form has a lot of issues, namely:
time: the user was supposed to see a dropdown menu where the user can choose between 5pm till 11 pm
No matter what code I do the dropdown menu would not work in the website but would work in django administration.

I have encountered also an issue where the in smaller screens the gallery pictures and the menu icons are not all displayed or 
the pictures are too big.

Submit button: When the user clicks the submit button, it should automatically store the data to django admin
     and at the same time create a mock email stating that the reservation has been successful.

I had an issue in making sure that there is uniformity in the website as the user opens another tab. I would like

### I was able to address all the issues that I have mentioned earlier in my work and now the website is working properly both in the django admin site and also in the main website.

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
