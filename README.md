![logo](https://res.cloudinary.com/millermayhem/image/upload/v1654768465/Logo_Hannahs_screen_qqpu7y.jpg)

# Portfolio Project 4 - Full Stack Toolkit - Hannah's Nail Bar
***

![mockup](https://res.cloudinary.com/millermayhem/image/upload/v1654770340/Screens_mockup_sde3gr.png)
##  [Visit the site on Heroku]([https://stevemiller7.github.io/Bad_Dog_Portfolio_1/](https://hannahs-nails.herokuapp.com/)).

My website presents Hannah's Nail Bar. Based in Auchterarder, Perthshire, Scotland. Users will be 
able to find information on the salon and hannah herself. Images of past work are presented in the Inspiration page.
Information on prices as well as the option to create a user account, make, amend and delete online bookings are also available. 

This is a responsive full stack data model web application structured using Django and Bootstraps and featuring authentication and permissions features.  

Contact information can be found in the footer of each page along side social media links and site navigation links.

Aesthetically, the aim was to create a clean, soft, user friendly site to tie in with the floral presentation of hannah's salon. 

***

# Table of Contents

- [Website Objectives](#website-objectives)
  - New User Benefits
  - Returning User Advantages
- [Website Layout](#website-layout)
- [Wireframes](#wireframes)
  - Home Page
  - Gallery Page
  - Contact Page
- [Aesthetics](#aesthetics)
  - Colour Palette
  - Fonts
  - Images
- [Features](#features)
  - Navigation Bar
  - Header
  - Information Section
  - Thumbnail Images
  - Owner Information
  - Footer
  - inspiration Gallery
  - Prices
  - User Authentication - Register, Login and Logout
  - Make A Booking
  - My Bookings
  - Messages
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - Functionality Testing
  - Compaitibility Testing
  - Performance testing
- [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits](#credits)


***

# Website Objectives
The primary function of this website is to promote Hannah's business and boost an already thriving customer base with the introduction of a booking system.
Presentation of essential information such as prices, contact details, past work is also a big factor. Currently the business is promoted through social media pages but now a more all rounded professional image can be portrayed. 

## New User Benefits

- Obtain information on the business
- Find contact details
- View gallery images of past work
- Access the companies social media sites
- Be introduced to Hannah
- Create an account
- Book an appointment

## Returning User Advantages

- Edit and delete appointments as required
- See the ever changing image gallery updated regulalry by Hannah through the admin site
- Refresh knowledge on the companies services
- Access social media accounts to leave feedback on services

***

# Website Layout

The wireframe layouts were created using Adobe Illustrator. 
It has been desinged to be clean, soft, professional and as user friendly as possible with the use of simple sight navigation links.
Accessibility has been carefully considered with the use of cointrasting colours and alt text equivalents for the visually immpared. 
The site is responsive for all screen sizes and tailored to suit each. The user experince will be smooth and satisfying accros all devices. 

# Wireframes

## Home Page
![wireframe-home](https://res.cloudinary.com/millermayhem/image/upload/v1654772491/Wireframe_Home-01_wzzug3.png)

## Gallery Page

![wireframe-gallery](https://res.cloudinary.com/millermayhem/image/upload/v1654772501/Wireframe_Image_Gallery-01_wrcj8d.png)

## Prices

![wireframe-prices](https://res.cloudinary.com/millermayhem/image/upload/v1654772586/Wireframe_Prices-01_nhbb4t.png)

## Make A Booking Page

![wireframe-booking-page](https://res.cloudinary.com/millermayhem/image/upload/v1654772555/Wireframe_Booking_Form-01_a1vcak.png)

## My Bookings

![wireframe-my-bookings](https://res.cloudinary.com/millermayhem/image/upload/v1654772567/Wireframe_My_Bookings-01_d2stc4.png)


# Aesthetics

The overall look of the site was created with the aim of being clean, soft, professional and modern.

Softer colours were choesn to create a more relaxing feel to the site. Whites, lights greys and soft pinks reflect the clean image of the salon. Toned down images for backgrounds where required match the soft feel.

## Colour Palette
- Soft Pink Hex #f6b9d5
- Light Grey Hex #f2f2f2
- White
- Black

## Fonts
- Open Sans - Google Fonts
- Playfair Display - Google Fonts
- 

## Images

No paid assets or royalty images were used in this project, only Hannah's own collection. Future gallery updates will only be images of Hannah's own work. 

[Back to Table of Contents](#table-of-contents)

***

# Features

The website is made up of 8 pages.

- Home
- Inspiration
- Prices
- Register
- Login
- Logout
- Book Appointment
- My Appointments

Key features are as follows:

## Navigation Bar with Off Canvas

![features-Navbar](https://res.cloudinary.com/millermayhem/image/upload/v1654774468/Screenshot_2022-06-09_at_12.32.44_nk8o5x.png)
![features-off-canvas](https://res.cloudinary.com/millermayhem/image/upload/v1654779889/Screenshot_2022-06-09_at_14.04.08_xqo3he.png)
![features-off-canvas-logged-in](https://res.cloudinary.com/millermayhem/image/upload/v1654779889/Screenshot_2022-06-09_at_14.04.34_c0zs0n.png)

The Navigation Bar is located at the top of each page and is consitent in style throughout the site. 

A business logo is placed to the left and will navigate you to the home page when clicked.
The burger icon opens the off canvas content which contains navigation links around the site. 
I decided to have the nav bar stuck to the top of the screen with an opacity applied which has a nice feel.

Links to each page are included for easy navigation to:
- Home
- Inspiration
- Prices
- Register
- Login

And when authenticated

- Book An Appointment
- My Appointments
- Logout

## Header

![features-header](https://res.cloudinary.com/millermayhem/image/upload/v1654775163/Screenshot_2022-06-09_at_12.45.46_ulm3zw.png)

 The header includes two features:
 - Opacity applied image of inside Hannah's shop
 - 'Hello Gorgeous' title which matches neon sign she has in her salon
 - Button, which changes from 'Member Login' to 'Appointments' when user is logged in

## Information Section

Offering backround information onthe salon and Hannah as well as some images to match.
 
 - Salon information labelled 'The Sanctuary'
 - Thumbnail images of the salon
 - Hannah information section with image and title

## Footer

![features-footer](https://res.cloudinary.com/millermayhem/image/upload/v1654775569/Screenshot_2022-06-09_at_12.52.36_ywixao.png)

A clean minimal fopoter containing:
- Social media links
- Title and slogan
- Usefull links
- Contact details

## Inspiration / Memory Book

A selection of images from past customers which is customisable from the admin log in offering the owner the ability to keep images
fresh, rotated and up to date with trends. 

## Price List

A JPeg of the current price list which she has printed and in the salon.

## Authentication

![feature-register](https://res.cloudinary.com/millermayhem/image/upload/v1654779787/Screenshot_2022-06-09_at_14.02.14_gmal4j.png)
![features-login](https://res.cloudinary.com/millermayhem/image/upload/v1654779787/Screenshot_2022-06-09_at_14.02.27_r0wtl9.png)
![features-logout](https://res.cloudinary.com/millermayhem/image/upload/v1654779812/Screenshot_2022-06-09_at_14.03.17_wvbwhs.png)

The site includes the ability to register and log in.
Additional features open up once logged in. These include the ability to make, edit and delete bookings.
Customers will add a username along with a password. When making a booking a phone number is to be added to the form.
All of the information is stored on a database. This is a heroku postgres database which is secured using a secret key. This key cannot be found anywhere
in the source code and is stored in heroku along with the database url.

## Book An Appointment

![feature-book-appointment](https://res.cloudinary.com/millermayhem/image/upload/v1654780377/Screenshot_2022-06-09_at_14.11.50_t1vxgb.png)
 
This page allows users to book appointments online. It collects a date, timeslot, prefered technician and contact number. If the time slot is already booked on a particular day a message will appear.
The page also contains a button to easily navigate the user to their bookings. 

![feature-already-booked-warning](https://res.cloudinary.com/millermayhem/image/upload/v1654780506/Screenshot_2022-06-09_at_14.14.31_t313z1.png)

The salon is closed on a Sunday and a Monday so if they try to book on those days another message will appear

![feature-register](https://res.cloudinary.com/millermayhem/image/upload/v1654780506/Screenshot_2022-06-09_at_14.14.48_lombsm.png)

## My Appointments

![feature-my-appointments](https://res.cloudinary.com/millermayhem/image/upload/v1654781237/Screenshot_2022-06-09_at_14.26.58_u5kq4j.png)

Here the user will find all of theor future appointments. They have the ability to edit the booking by clicking the 'edit' button or delete it using the 'Delete' button. Pressing the 'Edit' button will take them to booking page which will have the cells prepopulated. If they choose to delete the booking a warning modal will appear asking if they are sure they want to delete the booking. 

![feature-delete-modal](https://res.cloudinary.com/millermayhem/image/upload/v1654781299/Screenshot_2022-06-09_at_14.27.43_kzhmtq.png)

## Messages

![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657496/Hannah/Screenshot_2022-09-08_at_18.14.36_xlda4o.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657512/Hannah/Screenshot_2022-09-08_at_18.13.04_zzgjws.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657532/Hannah/Screenshot_2022-09-08_at_18.10.44_ub4fz8.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657546/Hannah/Screenshot_2022-09-08_at_18.10.02_wivw3b.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657556/Hannah/Screenshot_2022-09-08_at_18.12.01_eszf2i.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662657576/Hannah/Screenshot_2022-09-08_at_18.12.32_sg0kr5.png)
![messages](https://res.cloudinary.com/millermayhem/image/upload/v1662658814/Hannah/Screenshot_2022-09-08_at_18.39.03_pob0yk.png)

When users carry out a particular action on the site messages will appear to inform them of successfull and failed operations.

Success messages will include:
- Registering a username
- Logging in
- Logging out
- Making an appointment
- Editing an appointment
- Deleting an appointment

Error messages will appear when:
- A user tries to book an appointment on a time that isn't suitable.
- A user tries to edit an appointment to an unsuitable time.


[Back to Table of Contents](#table-of-contents)

***

# Technologies Used

## HTML 5
- Structure Language

## CSS
- Styling Language

## Bootstraps
- Frontend frameworks

## Django
- Database framework

## Google Fonts
- As a font resource.

## Font Awesome
- Social media icons

## Github
- As a software hosting platform.

## Gitpod
- For code development.

## Heroku
- App Hosting platform

## Postgres
- Database

## Adobe Illustrator
- Logo creation
- PNG and JPEG production
- Wireframes
- Readme images

## Photoshop
- Screens mockup image

## Cloudinary
- Image hosting

[Back to Table of Contents](#table-of-contents)

***

## Performance Testing

![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654786967/Screenshot_2022-06-09_at_14.44.46_fueorx.png)
![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654786967/Screenshot_2022-06-09_at_14.50.22_bptfg6.png)
![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654786967/Screenshot_2022-06-09_at_14.45.57_smcqly.png)
![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654786967/Screenshot_2022-06-09_at_14.47.01_mgfxws.png)
![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654786967/Screenshot_2022-06-09_at_14.49.28_zeixwc.png)


Website functionality testing was done using Google Chrome Developer Tools Lighthouse.
Improvements were made after testing the site build upon original completion.

Issues first raised included missing alt attributes on images, a missing aria-label for my toggle burger button on the navbar and image resolution sizes being too big. 
I had a issue with the low resolution logo in the navbar but i had trouble using a larger image so i reverted back to the original image. 

After ammending the issues raised further tests were carried out and the results were improved.

![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654787704/Screenshot_2022-06-09_at_16.13.24_uumu03.png)
![lighthouse performance results image](https://res.cloudinary.com/millermayhem/image/upload/v1654787704/Screenshot_2022-06-09_at_16.14.13_wdpcdm.png)

I still had the issue with the low res logo. I also have original isses with 'Issues logged to the `Issues` panel in Chrome Devtools', but i dont know how to amend them. 


## Manual Functionality Testing

Throughout the build manual function tests were carried out constantly to assess whether buttons, links, admin updates etc all worked. Trial and error got me to the results I was after. 

Forms were all tested repeatedly and checked against the admin databse records. 

The booking function works nicely and when changes are made the fields are prepopulated which benefits the user.

I followed 3 steps in my manual testing procedure.

### White Box Testing

As the developer I thoroughly checked the infrastrcutre and every line of code during the build, when formatting code and when running through the code validator. Changes were made where required, when required. All Inputs, links, updates, deletes, edits, navigations, external links, login, logout, registers and backend additions were checked against output results and everything worked nicely by the end of the build. All bugs were removed and all features work well. Information is passed to the database and everything syncs up and corresponds with each other. 
Admin users can add and remove additional nail technicians should it be required. The image gallery on the inspiration.html page can also be updated by admin users to keep it fresh and inkeeping with current trends"

### Black Box Testing

As well as testing the deployed application myself on iMac, Macbook, iPad and iPhone, I invited 5 other people to perform functionality testing through whatever whatever digital media they had access to. 
Feedback on UX design, functionality and aesthetics was very positive from the other people testing the site. 

### Grey Box Testing

As mentioned in Black Box Testing I tested the functionality myself using both knowledge of the code and via the deployed site. I found no functional issues myself but did have some future improvments in mind as detailed a little below.

Future improvements would also include:

- Customise sign up form to remove username, use email as the main login cell along side the password, have email required, phone required, first and last names.
- Email confirmation of booking changes to nail tech and customer.
- Have the ability to update all personal details.
- Add a blog page where customers could share experiences and like and comment on images posted of their nails.

## Compaitibility testing

The site was tested on various devices including:
- iPhone
- Macbook Pro
- iMac
- iPad
- I also tested responsiveness on Google Chrome Dev Tools. 


# Code Validation

I checked my HTML and CSS code using 2 websites.
- validator.w3.org
- jigsaw.w3.org

![Html validator warning image](https://res.cloudinary.com/millermayhem/image/upload/v1654793074/Screenshot_2022-06-09_at_17.42.36_hflul8.png)

There was a warning left regarding a heading in the footer section but I dont wnat a heading where it suggests.

![CSS validator warning image](https://res.cloudinary.com/millermayhem/image/upload/v1654793532/Screenshot_2022-06-09_at_17.51.37_dkmm7i.png)


CSS validation had no Errors returned after inpouting my CSS file content directly on to jigsaw.w3.org


[Back to Table of Contents](#table-of-contents)

***

# Deployment

The project is deployed via Heroku. 

I used Gitpod as a development environment where I commited all changes to git version control system. I used push command in Gitpod to save changes into GitHub.

To deploy the project I had to connect my Github respitory to Heroku through the Heroku 'Deploy' page.
All of the necessary config vars were created to allow the application to work.

The site is published at https://hannahs-nails.herokuapp.com/ 

To run localy:

- Log in to GitHub and click on repository to download (P4-Hannahs-Nails)
- select `Code` and click Download the ZIP file.
- after download you can extract the file and use it in your local environment

Alternatively you can Clone or Fork this repository (P4-Hannahs-Nails) into your github account.

***

# Credits

Initital creation of the project was done using Code Institute student template: 
- gitpod full template

Ideas and coding guides:
- www.w3schools.com
- Diploma in Software Development (E-commerce Applications) from Code Institute.
- 'I Think Therefore I Blog' Walkthrough via Code Institute
- 'Hello Django' Walkthrough via Code Institute
- 'Bootstrap Resume' via Code Institute
- Bad_Dog_Portfolio_1 done through Code Institute
- Github Developer-Felix Doctor---Patient-Scheduler
- webforefront.com
- slackoverflow.com
- docs.djangoproject.com
- pypi.org
- pythonguides.com
- codegrepper.com
- youtube.com - Max Goodridge

## Content

Information for this website was written by myself and Hannah of Hannah's Nail Bar. Hannah's own images are used.

## Images, Styling, Frameworks

Licensed and royalty free images were taken from:
- fontawesome.com
- fonts.google.com
- mdbootstraps.com
- bootstrap.com
- cloudinary.com
- Adobe stock
- Adobe Illustrator
- Adobe Photoshop
- django
- django-crispyforms
- django-allauth

[Back to Table of Contents](#table-of-contents)
