![Responsive Mockup](/documentation/readme_images/mockup.webp)

# Got No Beans

GotNoBeans is an online retailer specialising in coffee brewing equipment. Specifically targeted at the home enthusiast. they offer a wide variety of home brewers and accessories. Beyond this, they offer brewing recipes that are specific to their products to empower users to feel confident when purchasing a product they are unfamilar with. In order to promte the business and build a community around it, GotNoBeans host events around the UK during which they showcase and educate around their products.

The GotNoBeans website is a full-stack e-commerce site built using Django, Python, jQuery, CSS, and HTML.

[View the live site here](https://got-no-beans.herokuapp.com/)

&nbsp;

# Table of Contents
* [UX and UI](#ux-and-ui)
    * [Research](#research)
    * [Owner Goals](#owner-goals)
    * [User Stories](#user-stories)
    * [User Requirements](#user-requirements)
    * [Design](#design)
    * [Wireframes](#wireframes)
* [Data Model](#data-model)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be Implemented in the Future](#features-to-be-implemented-in-future)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks, Libraries, Programs and Extensions](#frameworks-libraries-programs-and-extensions)
    * [Testing and Validation Tools](#testing-and-validation-tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Creating a GitHub Repository](#creating-a-github-repository)
    * [Forking the GitHub Repository](#forking-the-github-repository)
    * [Making a Local Clone](#making-a-local-clone)
    * [Django](#django)
    * [Heroku](#heroku)
    * [AWS](#aws)
    * [Stripe](#stripe)
* [Credits](#credits)

&nbsp;

# UX and UI

## Research

Research for the creation of this site was carried out by searching for various forms of...

* [Clumsy Goat Coffee](https://clumsygoat.co.uk/pages/home-coffee-equipment)
* [#](#)
* [#](#)
* [#](#)

&nbsp;

## Owner Goals
The store owner has several goals for this site, which are outlined below:
* Provide an e-commerce site that will appeal to the home brew coffee enthusiast.
* Showcase a product line that consisting of a range of coffee brewers and accessories.
* List store organised events that help generate interest and a community around the business.
* Educate the user in brewing methods by listing product specific recipes.

&nbsp;

## User Stories

**Site Admin**
| As a...         | I want to be able to...                       | So that I can..                                |
| --------------- | --------------------------------------------- | ---------------------------------------------- |
| **Site Owner**  | login and have access to the store backend    | mange product, recipe and event listings.      |
| **Site Owner**  | restrict backend access to admins/superusers  | keep the site, listings and customers secure.  |
| **Site Owner**  | mange product listings                        | add, edit and delete products on the site.     |
| **Site Owner**  | mange recipe listings                         | add, edit and delete recipes on the site.      |
| **Site Owner**  | mange event listings                          | add, edit and delete events on the site.       |

&nbsp;

**Viewing & Navigation**
| As a...         | I want to be able to...             | So that I can..                                  |
| --------------- | ----------------------------------- | ------------------------------------------------ |
| **Site User**   | easily see the purpose of the site  | be informed as to whether it meets my needs.     |
| **Site User**   | browse the full range of products   | view the selection and make a purchase.          |
| **Site User**   | view individual product details     | identify the price, description, and image.      |
| **Site User**   | see a running total for my basket   | be informed as to how much I'm spending.         |
| **Site User**   | browse the full range of recipes    | have knowledge around the use of Site products.  |
| **Site User**   | view individual recipe details      | see the recipe method and find linked products.  |
| **Site User**   | browse the full range of events     | attend any local events that interest me.        |

&nbsp;

**Sorting & Searching**
| As a...        | I want to be able to...                          | So that I can..                                          |
| -------------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Site User**  | easliy sort the list of products available       | find products by price or name.                          |
| **Site User**  | easily sort products by category                 | narrow products down to the most relevant for my needs.  |
| **Site User**  | search products by name or description           | find a specific product.                                 |
| **Site User**  | view a filtered products list based on my search | easily see if my desired product is available.           |

&nbsp;

**Basket & Checkout**
| As a...        | I want to be able to...                       | So that I can..                                 |
| -------------- | --------------------------------------------- | ----------------------------------------------- |
| **Site User**  | easliy add products to my basket              | compile a selection of products to purchase.    |
| **Site User**  | view the products in my basket                | see what I have selected and adjust if needed.  |
| **Site User**  | easily enter my delivery and payment details  | complete a quick and hassel free purchase.      |
| **Site User**  | view my order confirmation after checkout     | verify that the order details are correct.      |
| **Site User**  | recieve an order confirmation email           | keep order details for my records.              |

&nbsp;

**Registration & User Accounts**
| As a...              | I want to be able to...                          | So that I can..                                         |
| -------------------- | ------------------------------------------------ | ------------------------------------------------------- |
| **Site User**        | easliy register for a new account                | have a personal profile.                                |
| **Registered User**  | recieve a verification email during registration | be confident that my registration is successful.        |
| **Registered User**  | easliy login and out of my accout                | use the site with the advantages of a registered user.  |
| **Registered User**  | recover my email if I forget it                  | regain access to my account.                            |
| **Registered User**  | have a personal user profile.                    | view my order history and default delivery details.     |
| **Registered User**  | keep a list of my favourite products             | easily find and purchase them at a later date.          |

&nbsp;

## User Requirements
* Appealing visual presentation that enhances the user experience.
* Familiar and intuitive design that negates any learning curve.
* Feedback when interacting with the site that is also instructive.
* Colour choices for links and buttons should be familar and logical.
* A reactive site that is user friendly and well presented on all types of device and screen sizes.
* Adequate levels of colour contrast across the site that presents content in an accessible and easy to read manner.

&nbsp;

## Design

### Image
* A large colourful image showing a selection of coffee brewers is used as a background for the site homepage. The image itself is visually appealing while also making a direct link to the products sold on the site. 

### Colour Scheme
* Black text on a white background forms the main basis of the site. This clean and classic pairing offers maximium contrast to the user while also being visually appealing and working well with other colours. The navbar is an extremelt dark shade of brown (#1a0d00) which is used to provide a suttle link to that of coffee beans. Brown is also used on the footer with an opacity of .5 to add lightness and allow the background image to be seen through it on the homepage.

* Main Colour Pallet:
    * Background: #fff
    * Text: #000
    * Navbar: #1a0d00
    * Footer: rgba(26,13,0,.5)
    * Buttons and Links: #000, #adb5bd, #0d6efd, #dc3545 (Bootstrap theme colours)

### Fonts
* The Google font of Roboto Mono was chosen for this site. A monospaced member of the Roboto family type, this font is optimised for readability on screens across a wide variety of devices and reading environments. It works very well with the site theme and helps to provide a clean asthetic.

### Structure
* The information architecture type used for this site is the hierarchical tree structure. This common structure allows for simple navigation throughout the site and allows for easy expansion of the site in the future. The use of the burger navigation icon, along with a floating return to top button, help to overcome the common issues with this structure on mobile devices.

<details>
<summary>Site Map</summary>

![Site Map](/readme-files/images/sitemap.webp)

</details>

&nbsp;

## Wireframes

* Balsamiq Wireframes was used to create the wireframes for this site. 
Wireframes for mobile, tablet, and desktop can be found below:

  ### [Phone Wireframe](#)

  ### [Tablet Wireframe](#)

  ### [Desktop Wireframe](#)

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Data Model
The site is underpinned by a relational database model and the datbabase schema can be seen below. This represents the models, fields, field types and relationships between models. 

* The database currently consists of eight models, these include:
    * Category
    * Event
    * Favourites
    * Order
    * OrderLineItems
    * Product
    * Recipe
    * UserProfile

 &nbsp;

![Database Schema](/documentation/readme_images/database_schema.png)

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Features 

## Existing Features

* Navigation Bar

    * Featured on all pages, the full responsive navigation bar includes the GotNoBeans name in the upper lefthand corner, linked to the homepage. A search field in the top centre and three main links just below that for 'Products', 'Recipes', and 'Events'; these links also contain an active class as a navigational aid, indicating the current page to the user. A basket link and basket total are found in the upper righthand corner. Beside these are dropdown menus for 'Account' and 'Admin' with the latter only appearing for superusers. The 'Account' dropdown expands to show 'Register' and 'Login' links for users who haven't yet registered or logged in. Once logged in, registered users will instead see links to 'Profile', 'Favourites' and 'Logout' under the 'Account' dropdown.

    * On mobile devices the main links, 'Products', 'Recipes', and 'Events', collapse into a burger icon and are joined by a search link/field. The 'Account' and 'Admin' dropdowns remain in the same location beside the basket and basket total.

        ![Navbar: Desktop](/documentation/readme_images/navbar.png)

        <details>
        <summary>Navbar: Mobile</summary>

        ![Navbar: Mobile](#)

        </details>
        
        <details>
        <summary>Sidenav: Mobile</summary>

        ![Sidenav: Mobile](#)

        </details>

&nbsp;

* Homepage

    * A large colourful image showing a selection of coffee brewers is used as a background for the site homepage. The image itself is visually appealing while also making a direct link to the products sold on the site. This immediately demonstrates to the user the purpose of the site and is ovelayed with a 'Shop Now' which encourages them to view the products on offer. The tagline of "You do the brew, we'll do the beans" is used to convey that the site specailses in brewing equipment rather than coffee itself. 

        ![Homepage](/documentation/readme_images/homepage.png)

* Page Headers

    * Page headers can be found sitewide and assist the user to keep track of which page they are currently on. Page headers are generally uniform across the site, with two main styles, but it differs slightly on the 'Products' page. The products header itself is linked to the products page and shows all products (brewers and accessories), this is particularly helpful on moble devices. Two category badges can be found under the products header which filter products by category.

        ![Page Header](/documentation/readme_images/header.png)

* Forms

    * All forms are uniform in appearance with a header above the form fields. Each field is labeled and mandatory fields are marked with an asterisk to assist the user. Date and time pickers are used where required as per best practice. Form validation is present and Bootstrap toasts provide additional feedback to the user. When editing a form with an image field, a minified preview is shown to the user if a image is present.

        ![Form](/documentation/readme_images/form.png)

* Delete Item Modal

    * Should the admin attempt to delete a product, recipe or event, a modal will appear to confim that they do indeed want to delete the selected item. This helps to avoid accidental deletion of items as it is a two step process.

        ![Delete Item Modal](/documentation/readme_images/modal.png)

* All Products and Recipes Pages

    * The products and recipes pages follow the same format displaying images for each item alond with a name, both linked to that item's description page; the products page additionally shows the item price and has a sort selector for sorting the products by name or price. Edit and delete options are also displayed to superusers. A back to top button can be found in the bottom right corner of both pages, this is particularly useful to users on a mobile device.

        ![Products](/documentation/readme_images/products.png)

* Products Details Page

    * The product detail page displays an image of the product which opens in a new tab when clicked. It is accompanied by information on the product such as price and description. There is also a quantity adjuster along with the buttons 'Add to Favourite', "Keep Shopping' and 'Add to Basket'. Edit and delete options are also displayed to superusers.

        ![Product Details](/documentation/readme_images/product_details.png)

* Recipe Details Page

    * The recipe detail page displays an image associated with the recipe which opens in a new tab when clicked. It is accompanied by information on the recipe such as recommended grind size, water volume and brewing method. There are also suggested products listed, that relate to the recipe, which are linked to their product detail page. Edit and delete options are also displayed to superusers.

        ![Recipe Details](/documentation/readme_images/recipe_detail.png)

* Events Page

    * The events page consiste of an accordion that displays baisc information for each event with further details available when expanded. In the expanded view the user can see full details (descrprtion, date, time, location) for each event along with a list of linked products that will be showcased at each event. Superusers will additionally have access to edit and delete options.

        ![Events](/documentation/readme_images/events.png)

* Profile Page

    * The profile page is only available to registered users and displays the user's order history and default delivery information. Housed within an accordion, the top card contains a list of the user's previous orders while the bottom card contains a form where the user can add or update their default delivery information. Each order within the order card is linked to an order summary page where the user can review full details of each order.

        ![Profile](/documentation/readme_images/profile.png)

* Favourites Page

    * The favourites page allows the user to compile a selection of favoured items that are easily accessible for future refrence. A product name and price is displaed for each item alongside a minified product image. The product name and image both link to the description page for that particular item should the user wish to see further details or purchase the item. A remove button is also displayed beside each item should the user wish to remove that item from their favourites.

        ![Favourites](/documentation/readme_images/favourites.png)

* Basket

    * The basket page summarises the products added by the user, displaying a product name, sku, unit price, subtotal, delivery cost and grand total. It also contains a quantity selector which can be used to adjust the quantity of each item, it is also possible to remove individual products completely. 'Keep Shopping' and 'Checkout' buttons are at the bottom of the page and these link to the products page and checkout respectively.

        ![Basket](/documentation/readme_images/basket.png)

* Checkout Page

    * The checkout page consits of a form for the user to input their persoal details and delivery information; this is auto-populated if a registered user has saved their default information. Underneath the form is a payment field supplied by Stripe for card details. At the bottom of the page there is an 'Adjust Basket' button, linked to the basket, and a 'Complete Order' button, used to submit the order.

        ![Checkout](/documentation/readme_images/checkout.png)

* Checkout Success Page

    * The checkout success page consists of a complete summary of the order, listing the order number, product name and quantity, delivery, and billing information. It also confirms to the user that an email was sent to the email address provided. A 'Forgot Something?' button is located at the bottom of the page to encourage them to seach for additional proucts and links to the products page.

        ![Checkout Success](/documentation/readme_images/checkout_success.png)

* Footer

    * The footer consists of GotNoBeans copyright text and a mailto link which users can use to contact the site owner. It has an opacity of .5 to add lightness and allow the background image to be seen through it on the homepage.

        ![Footer](/documentation/readme_images/footer.png)

* Toasts

    * Bootstrap toasts are used to provide users with a variety of success, error, and alert messages. The dissapear after a short period and can also be closed by the user.

        ![Toasts](/documentation/readme_images/toasts.png)

* Admin Features

    * Site admins (superusers) can perform full CRUD functionallity on the site with the ability to create, read, update and delete products, recipes and events.
    * When an admin logs into the site, they are presented with an extra 'Admin' dropdown in the navbar containing links to add new products, recipes and events to the site.
    * Additionally, edit and delete options are available to them in the products and product detail pages, the recipes and recipe detail pages and the events page.

* Registered User Features

    * Users who have registered on the site have access to additional features that improve their user experience; including access to order history, a personal favourite products list and the ability to add and update their default personal and delivery information.
    * When a registered user logs into the site they are offered additional links under the 'Profile' dropdown in the navbar, spcifically linking to their 'Profile' page and 'Favourites' list.
    * Their profile page shows a list of their previous orders and allows them to maintain their personal and delivery information.
    * The favourites page lists and items that they have favourited and links back to the product detail page for each individual item should they wish to purchase it at a future date. Products can be added to their favorites list by clicking on the "Add to Favourites' button on the product detail page.

&nbsp;

## Features to be Implemented in Future

* Breadcrumbs
    * The addition of breadcrumbs to the top of each page would be a useful way for users to keep track of where they are on the website.

* Favourite Recipes
    * In addition to having product favourites, it would be a nice feature to be able to do the same with brewing recipes; especially if the recipe selection expands greatly in the future.

* Categories CRUD
    * At present, full CRUD functionallity is not require for the store as it specialises in a narrow range of goods. However, to allow for future growth it might be beneficial for admins to be able to create, update and delete product categories.

* Social Media Login
    * The ability to register and login using social media accounts would be a usful addition and provide a faster sign-up process to users.

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Libraries, Programs and Extensions
* [Amazon Web Services: AWS](https://aws.amazon.com/): Used to store static and media files.
* [Balsamiq](https://balsamiq.com/): Used to create site wireframes.
* [Bootstrap](https://getbootstrap.com/): Used to enable responsive front-end site development.
* [Django](https://www.djangoproject.com/): Used to build the project framework.
* [Font Awesome](https://fontawesome.com/): Used to locate and import icons used throughout the site.
* [Git](https://en.wikipedia.org/wiki/Git): Used as project development environment and is connected to GitHub.
* [GitHub](https://en.wikipedia.org/wiki/GitHub): Used to hold project repository which is linked to Heroku.
* [Google Fonts](https://fonts.google.com/): Used to import the 'Roboto Mono' font used throughout the site.
* [Heroku](https://en.wikipedia.org/wiki/Heroku): Used to host site and synced with GitHub repository.
* [jQuery](https://jquery.com/): Used to implement JavaScript code.
* [Stripe](https://stripe.com/): Used to take and process payments.


## Testing and Validation Tools
  * [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Used to carry out manual testing on the website and to simulate mobile devices.
  * [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input): Used to check the markup validity of the html code. 
  * [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_uri): Used to validate the css code.
  * [Flake8](https://flake8.pycqa.org/): Used to lint python code for errors, styling issues and complexity.
  * [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): Used to audit performance, accessibility, best practices and SEO across the website.
  * [a11y](https://color.a11y.com/): Used to verify that the colour contrast across the site adhered to the WCAG 2.1 Guidelines.
  * [LambdaTest](https://www.lambdatest.com/): Used to perform cross browser testing.

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Testing 

Testing information can be found in the [testing file][TESTING.md].

&nbsp;

[Back to top &uarr;](#got-no-beans)



[Back to top &uarr;](#got-no-beans)

# Deployment

## Creating a Gitpod Repository

A GitHub repository is used to store your project, with Git and GitHub used for version control. The following steps outline how to create a GitHub repository.
1. Log in to GitHub.
2. In the upper-right corner of any page, use the '+' drop-down menu and select 'New repository'.
3. Give your repository a name.
4. Choose your repository visibility; 'Public' or 'Private'.
5. Select Initialize this repository with a README.
6. Click Create repository.

&nbsp;

## Forking the GitHub Repository

Forking the GitHub Repository makes a copy of the original repository on your GitHub account; allowing you to view and/or make changes without affecting the original repository and can be done by using the following steps.
1. Log in to GitHub and locate the repository: [GotNoBeans](https://github.com/davecoll3/GotNoBeans).
2. Once in the repository, navigate to the "Fork" button at the top righthand corner of the page.
3. Click on the fork dropdown arrow and then select "Create a new fork".
4. You should now have a copy of the original repository in your GitHub account.

&nbsp;

## Making a Local Clone
1. Log in to GitHub and locate the repository: [GotNoBeans](https://github.com/davecoll3/GotNoBeans).
2. Click on the geen "Code" button at the top of the page.
3. From here you can select HTTPS, SSH or Github CLI; click on the clipboard icon to copy the URL.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Django
This project is built around the Dango framework which can be installed as follows:
1. Type the following command into your IDE:
```
pipe install 'django'
```
2. Then name your project to create it.
```
django-admin startproject your_project_name .
```
3. You will then see a folder with your project's name in the file explorer.
4. Create a .gitignore file by typing:
```
touch .gitignore
```
5. Inside the new .gitignore file add the following basics:
```
*.sqlite3
*.pyc
__pycache__
.env
```
6. Check the project by running it with the command below.This should expose port 8000 which, when open, should display Django's success page.
```
python3 manage.py runserver
```
7. Stop the server and run your initial migrations with the following command:
```
python3 manage.py migrate
```
8. Then create a superuser to allow you to log into the project admin. Type the command below, which will result in a request for you to provide a username, email address and password.
```
python3 manage.py createsuperuser
```
9. Finally, you can push your changes to github by running the commands below sequentially:
```
git add .
git commit -m "initial commit"
git push
```

### Allauth
Allauth is a django package that handles the registration and login process. It can be installed by following [this guide](https://django-allauth.readthedocs.io/en/latest/installation.html).  

&nbsp;

## ElephantSQL
The database used while developing your project within the IED is only available within the IED. You need to create a new database that can be accessed by your Heroku app. This can be achieved using [ElephantSQL](https://www.elephantsql.com/) and the steps are outlined below.
1. On the ElephantSQL site, log into your account to access your dashboard. If you don't have an account, you can create one [here](https://customer.elephantsql.com/signup).
2. Click on the green "+ Create New Instance" button in the top right-hand corner.
3. Set up your plan by giving it a name (usually the name of your project), select your plan; the tags are optional.
4. Select "Set Region" and choose a data centre near you.
5. Click "Review" and, if your details are correct, click "Create Instance".
6. Return to your dashboard and click on the database instance name for this project.
7. In the URL section, click on the copy icon to copy the database URL to your clipboard.
8. This URL will be used in your Heroku Config Vars to connect it to your database.

&nbsp;

## Heroku Deployment

1. On the [Heroku website](https://heroku.com/), log into your account. If you don't have a Heroku account, you can sign-up for one [here](https://signup.heroku.com/).
2. Click on the "New" button in the top right-hand corner and then "Create a New App".
3. Give your app a unique name and select your local region. Then click on the "Create App" button.
4. Open the new app's settings tab and click "Reveal Config Vars".
5. Add "DATABASE_URL" as a Config Var and paste your ElephantSQL URL as discussed in the "Creating a Database" guide above; do not add quotation marks to your URL.

Now that the Heroku app has been created and connected to the ElephantSQL database, you can return to your IDE to run migrations and add a superuser.
6. Back in your IDE, install dj_database_url and psycopg2 as both are needed to connect to your external database. Type the following command in your terminal.
```
pip3 install dj_database_url==0.5.0 psycopg2
```
7. You will then need to update your requirments.txt file.
```
pip freeze > requirements.txt
```
8. In your settings.py file, underneath the import for os,import dj_database_url by typing in the following (ignore "import os" below, it's just for reference):
```
import os
import dj_database_url
```
9. Scroll to the "DATABASES" section and update it to the following code, so that the original connection to sqlite3 is commented out and you can connect to your new ElephantSQL database instead. Paste your ElephantSQL database URL in place of 'your-database-url-here' below.
```
# DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
10. Do not commit the settings.py file with your database string in the code, this is temporary so that we can connect to your new database and make migrations.
11. Back in the terminal, run the showmigrations command to confirm you are connected to your external database.
```
python3 manage.py showmigrations
```
12. Migrate your models to your new database.
```
python3 manage.py migrate
```
13. Create a superuser for your database by typing:
```
python3 manage.py createsuperuser
```
14. Follow the steps to create a new superuser username and password; the email address is optional and can be left blank.
Return to the ElephantSQL website for the next few steps.
15. On your database page, select "Browser" from the left side navigation.
16. Click on the "Table Queries" button and then select "auth_user (public)".
17. When you click “Execute”, you should see your new superuser details. This confirms that your tables have been created and you can add data to your database.
18. Finally, to prevent exposing your database when you push to GitHub, delete your ElephantSQL database URL from settings.py. Instead, you can add an if statement in settings.py to run the ElephantSQL database when running the app on heroku or sqlite if not. Return to the "DATABASE" section of your settings.py file and refactor your code as follows:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
19. Next you will have to install a package called gunicorn, which will act as your web server. In the terminal, run the following command and then freeze your requirements.txt file to update it.
```
pip3 install gunicorn 
pip3 freeze > requirements.txt
```
20. Now you can create a Procfile to tell Heroku to create a web dyno and serve your Django app. In your root directory create a file called 'Procfile' and inside this file insert the following code:
```
web: gunicorn your_project_name_.wsgi:application
```
21. Return to Heroku and navigate to your app's settings. In the Config Vars, add a new Config Var named "DISABLE_COLLECTSTATIC" and set it's value to "1". This prevents Heroku from collecting static files when you deploy.
22. Back in your IDE, return to the settings.py file, and find "ALLOWED_HOSTS". Inside the brackets insert your app's URL followed by 'localhost'. As shown below:
```
ALLOWED_HOSTS = ['your-project-name.herokuapp.com', 'localhost']
```
23. Log into Heroku in the terminal and enter your details.
```
heroku login -i
```
24. Get your app name from heroku.
```
heroku apps
```
25. Set your heroku remote.
```
heroku git:remote -a <app_name>
```
26. Now add, commit and push your changes to GitHub.
27. Follow this up by pushing to Heroku with the command below.
```
git push heroku main
```
28. Your app will now be deployed on Heroku but without any static files.
29. Back in Heroku, you can set your app to be deployed automatically by navigaint to the app "Deploy" menu. Scrolling down to the 'Deployment Method' section and connecting it to github. You will need to search for your repository, once located click 'connect'. Then scroll further down and click 'Enable Automatic Deploys'. Once connected, your code will automatically deploy to Heroku whenever you push to github.

## AWS
Amazon Web Services are used to store your static and media files.
1. Go to the AWS website and [create an account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email).
2. Once signed up and logged in, locate "My Account" in the navbar and then select "AWS Management Console".
3. From here, search for 'S3' search bar and select it from the search results.
4. On the S3 Buckets page, click on the "Create Bucket" button.
5. Name your new bucket (usually the same as your app name) and select your local region.
6. Under "Object Ownership" select "ACLs enabled".







  1. Make sure that your project is initialized as a Git repository. You can check this by running the following command at the root of your project.
  ```
  git status
  ```

  2. If you encounter an error, that means that your project isn't yet a Git repository. You can initialize the repository by running the following command.
  ```
  git init
  ```

  3. Applications that feature an Express.js back end can use Heroku's PORT environment variable. To set this up, create a port variable with a value of process.env.PORT. You can also add a default value for local instances of your server by using the || syntax.
  ```
  const port = process.env.PORT || 3001
  ```

## Heroku Deployment: Create a Heroku App

Now that you have created the repository and configured the server, you can create an app on Heroku. Using the steps below, this can be done without opening the browser.
  1. Create a new Heroku app by running the following command in the root of your project:
  ```
  heroku create
  ```

  2. The Heroku CLI will randomly generate an app name, but you can specify a name using the following syntax.
  ```
  heroku create <app name>
  ```

  3. Once you have created the app, you can run 'git remote -v' to verify that the Heroku remote URL was added by the Heroku CLI
  ```
  git remote -v
  heroku  https://git.heroku.com/<heroku-app-name>.git (fetch)
  heroku  https://git.heroku.com/<heroku-app-name>.git (push)
  ```

  4. The remote URL gets added automatically to your Git repository without requiring any extra commands. You can now prepare for deployment.

## Heroku Deployment: Deploy to Heroku

  1. Add and commit all your project files, then push to Heroku.
  ```
  git add -A
  git commit -m "Pushing to Heroku"
  git push heroku main
  ```

  2. Confirm that the application was deployed successfully by visiting the application URL provided in the terminal. Sometimes the output will say that the build was successful, but you should still open your application in the browser to verify.
  ```
  remote: -----> Build succeeded!
  remote: -----> Discovering process types
  remote:        Procfile declares types     -> (none)
  remote:        Default types for buildpack -> web
  remote:
  remote: -----> Compressing...
  remote:        Done: 33.8M
  remote: -----> Launching...
  remote:        Released v9
  remote:        https://lit-retreat-65972.herokuapp.com/ deployed to Heroku
  ```

  3. Your app should now be deployed with a server to Heroku. The link will be accessible as long as your app exists on Heroku.

If you encounter any issues, further details on Heroku deployment and troubleshooting can be found [here](https://coding-boot-camp.github.io/full-stack/heroku/heroku-deployment-guide).

The live link can be found [here](#)

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Credits 

## Content 

  * The Code Institute's readme-template provided the basic structure for the readme.md file.
  * The Code Institute's Non-Relational Database Management Systems Mini Project was used to provide basic structure and authentication.
  * The [Bootstrap](#) front-end framework was used to supply components such as navbar, sidenav, collapsible, and search panel.

## Media

  * The favicon image was sourced from [Icons8](https://icons8.com) and was freely used under the [Icons8 licence](https://icons8.com/license).
  * The hero-image was sourced from [Unsplash](https://unsplash.com) and was freely used under the [Unsplash licence](https://unsplash.com/license).

## Code

  * The CSS code for...
  * The JavaScript code for...

## Acknowledgements

  * I would like to thank my mentor, Oluwaseun Owonikoko, who assisted me on this project.
  * I would like to thank Iris Smok, the Code Institute's cohort facilitator for Coleg y Cymoedd, for her advice and encouragement.
  * I would also like to acknowledge the support and advice obtained from the Code Institute's Tutor Support and Slack community. 

  &nbsp;

[Back to top &uarr;](#got-no-beans)

[TESTING.md]: TESTING.md