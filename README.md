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

The site features the ability to register in order to make, edit and delete bookings.
The booking features open up once logged in.

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

![feature-delete-modal](https://res.cloudinary.com/millermayhem/image/upload/v1654781299/Screenshot_2022-06-09_at_14.27.43_kzhmtq.png])


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
