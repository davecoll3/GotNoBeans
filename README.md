![Responsive Mockup](/documentation/readme_images/mockup.webp)

# Got No Beans

GotNoBeans is an online retailer specialising in coffee brewing equipment. Specifically targeted at the home enthusiast. They offer a wide variety of home brewers and accessories. Beyond this, they offer brewing recipes that are specific to their products to empower users to feel confident when purchasing a product they are unfamiliar with. In order to promote the business and build a community around it, GotNoBeans host events around the UK during which they showcase and educate around their products.

The GotNoBeans website is a full-stack e-commerce site built using Django, Python, JavaScript, CSS, and HTML.

[View the live site here](https://got-no-beans.herokuapp.com/)

&nbsp;

# Table of Contents
* [UX and UI](#ux-and-ui)
    * [Research](#research)
    * [Owner Goals](#owner-goals)
    * [User Stories](#user-stories)
    * [User Requirements](#user-requirements)
    * [Design](#design)
    * [Sitemap](#sitemap)
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

Research for the creation of this site was carried out by searching for various forms of online home coffee equipment retailers. A selection of sites found are shown below. 

* [Clumsy Goat Coffee](https://clumsygoat.co.uk/pages/home-coffee-equipment)
* [Coffee Island](https://www.coffeeisland.co.uk/catalog/homeBarista/46)
* [Odd Kin Coffee](https://www.oddkincoffee.com/collections/coffee-brewing-equipment)
* [Roast Works](https://www.roastworks.co.uk/collections/gear)

&nbsp;

## Owner Goals
The store owner has several goals for this site, which are outlined below:
* Provide an e-commerce site that will appeal to the home brew coffee enthusiast.
* Showcase a product line that consists of a range of coffee brewers and accessories.
* List store organised events that help generate interest and a community around the business.
* Educate the user in brewing methods by listing product specific recipes.

&nbsp;

[Back to top &uarr;](#got-no-beans)

## User Stories

**Site Admin**
| ID | As a...         | I want to be able to...                       | So that I can..                                |
| -- | --------------- | --------------------------------------------- | ---------------------------------------------- |
| 1  | **Site Owner**  | login and have access to the store backend    | manage product, recipe and event listings.      |
| 2  | **Site Owner**  | restrict backend access to admins/superusers  | keep the site, listings and customers secure.  |
| 3  | **Site Owner**  | mange product listings                        | add, edit and delete products on the site.     |
| 4  | **Site Owner**  | mange recipe listings                         | add, edit and delete recipes on the site.      |
| 5  | **Site Owner**  | mange event listings                          | add, edit and delete events on the site.       |

&nbsp;

**Viewing & Navigation**
| ID | As a...         | I want to be able to...             | So that I can..                                  |
| -- | --------------- | ----------------------------------- | ------------------------------------------------ |
| 6  | **Site User**   | easily see the purpose of the site  | be informed as to whether it meets my needs.     |
| 7  | **Site User**   | browse the full range of products   | view the selection and make a purchase.          |
| 8  | **Site User**   | view individual product details     | identify the price, description, and image.      |
| 9  | **Site User**   | see a running total for my basket   | be informed as to how much I'm spending.         |
| 10 | **Site User**   | browse the full range of recipes    | have knowledge around the use of site products.  |
| 11 | **Site User**   | view individual recipe details      | see the recipe method and find linked products.  |
| 12 | **Site User**   | browse the full range of events     | attend any local events that interest me.        |

&nbsp;

**Sorting & Searching**
| ID | As a...        | I want to be able to...                          | So that I can..                                          |
| -- | -------------- | ------------------------------------------------ | -------------------------------------------------------- |
| 13 | **Site User**  | easily sort the list of products available       | find products by price or name.                          |
| 14 | **Site User**  | easily sort products by category                 | narrow products down to the most relevant for my needs.  |
| 15 | **Site User**  | search products by name or description           | find a specific product.                                 |
| 16 | **Site User**  | view a filtered products list based on my search | easily see if my desired product is available.           |

&nbsp;

**Basket & Checkout**
| ID | As a...        | I want to be able to...                       | So that I can..                                 |
| -- | -------------- | --------------------------------------------- | ----------------------------------------------- |
| 17 | **Site User**  | easily add products to my basket              | compile a selection of products to purchase.    |
| 18 | **Site User**  | view the products in my basket                | see what I have selected and adjust if needed.  |
| 19 | **Site User**  | easily enter my delivery and payment details  | complete a quick and hassle free purchase.      |
| 20 | **Site User**  | view my order confirmation after checkout     | verify that the order details are correct.      |
| 21 | **Site User**  | receive an order confirmation email           | keep order details for my records.              |

&nbsp;

**Registration & User Accounts**
| ID | As a...              | I want to be able to...                          | So that I can..                                         |
| -- | -------------------- | ------------------------------------------------ | ------------------------------------------------------- |
| 22 | **Site User**        | easily register for a new account                | have a personal profile.                                |
| 23 | **Registered User**  | receive a verification email during registration | be confident that my registration is successful.        |
| 24 | **Registered User**  | easily login and out of my account                | use the site with the advantages of a registered user.  |
| 25 | **Registered User**  | recover my email if I forget it                  | regain access to my account.                            |
| 26 | **Registered User**  | have a personal user profile.                    | view my order history and default delivery details.     |
| 27 | **Registered User**  | keep a list of my favourite products             | easily find and purchase them at a later date.          |

&nbsp;

[Back to top &uarr;](#got-no-beans)

## User Requirements
* Appealing visual presentation that enhances the user experience.
* Familiar and intuitive design that negates any learning curve.
* Feedback when interacting with the site that is also instructive.
* Colour choices for links and buttons should be familiar and logical.
* A reactive site that is user friendly and well presented on all types of device and screen sizes.
* Adequate levels of colour contrast across the site that presents content in an accessible and easy to read manner.

&nbsp;

## Design

### Image
* A large colourful image showing a selection of coffee brewers is used as a background for the site homepage. The image itself is visually appealing while also making a direct link to the products sold on the site. 

### Colour Scheme
* Black text on a white background forms the main basis of the site. This clean and classic pairing offers maximum contrast to the user while also being visually appealing and working well with other colours. The navbar is an extremely dark shade of brown (#1a0d00) which is used to provide a subtle link to that of coffee beans. Brown is also used on the footer with an opacity of .5 to add lightness and allow the background image to be seen through it on the homepage.

* Main Colour Pallet:
    * Background: #fff
    * Text: #000
    * Navbar: #1a0d00
    * Footer: rgba(26,13,0,.5)
    * Buttons and Links: #000, #adb5bd, #0d6efd, #dc3545 (Bootstrap theme colours)

![Colour Pallet](/documentation/readme_images/colours.png)

### Fonts
* The Google font of Roboto Mono was chosen for this site. A monospaced member of the Roboto family type, this font is optimised for readability on screens across a wide variety of devices and reading environments. It works very well with the site theme and helps to provide a clean aesthetic.

### Structure
* The information architecture type used for this site is the hierarchical tree structure. This common structure allows for simple navigation throughout the site and allows for easy expansion of the site in the future. The use of the burger navigation icon, along with a floating return to top button, help to overcome the common issues with this structure on mobile devices.

### Sitemap
![Site Map](/documentation/readme_images/sitemap.png)

&nbsp;

[Back to top &uarr;](#got-no-beans)

## Wireframes

* Balsamiq Wireframes was used to create the wireframes for this site. 
Wireframes for desktop and mobile devices can be found below:

  ### [Mobile Wireframe](documentation/readme_docs/mobile_wireframes.pdf)

  ### [Desktop Wireframe](documentation/readme_docs/desktop_wireframes.pdf)

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Data Model
The site is underpinned by a relational database model and the database schema can be seen below. This represents the models, fields, field types and relationships between models. 

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

    * A large colourful image showing a selection of coffee brewers is used as a background for the site homepage. The image itself is visually appealing while also making a direct link to the products sold on the site. This immediately demonstrates to the user the purpose of the site and is overlaid with a 'Shop Now' which encourages them to view the products on offer. The tagline of "You do the brew, we'll do the beans" is used to convey that the site specialises in brewing equipment rather than coffee itself. 

        ![Homepage](/documentation/readme_images/homepage.png)

* Page Headers

    * Page headers can be found sitewide and assist the user to keep track of which page they are currently on. Page headers are generally uniform across the site, with two main styles, but it differs slightly on the 'Products' page. The products header itself is linked to the products page and shows all products (brewers and accessories), this is particularly helpful on mobile devices. Two category badges can be found under the products header which filter products by category.

        ![Page Header](/documentation/readme_images/header.png)

* Forms

    * All forms are uniform in appearance with a header above the form fields. Each field is labelled and mandatory fields are marked with an asterisk to assist the user. Date and time pickers are used where required as per best practice. Form validation is present and Bootstrap toasts provide additional feedback to the user. When editing a form with an image field, a minified preview is shown to the user if an image is present.

        ![Form](/documentation/readme_images/form.png)

* Delete Item Modal

    * Should the admin attempt to delete a product, recipe or event, a modal will appear to confirm that they do indeed want to delete the selected item. This helps to avoid accidental deletion of items as it is a two step process.

        ![Delete Item Modal](/documentation/readme_images/modal.png)

* All Products and Recipes Pages

    * The products and recipes pages follow the same format displaying images for each item along with a name, both linked to that item's description page; the products page additionally shows the item price and has a sort selector for sorting the products by name or price. Edit and delete options are also displayed to superusers. A back to top button can be found in the bottom right corner of both pages, this is particularly useful to users on a mobile device.

        ![Products](/documentation/readme_images/products.png)

* Products Details Page

    * The product detail page displays an image of the product which opens in a new tab when clicked. It is accompanied by information on the product such as price and description. There is also a quantity adjuster along with the buttons 'Add to Favourite', "Keep Shopping' and 'Add to Basket'. Edit and delete options are also displayed to superusers.

        ![Product Details](/documentation/readme_images/product_details.png)

* Recipe Details Page

    * The recipe detail page displays an image associated with the recipe which opens in a new tab when clicked. It is accompanied by information on the recipe such as recommended grind size, water volume and brewing method. There are also suggested products listed, that relate to the recipe, which are linked to their product detail page. Edit and delete options are also displayed to superusers.

        ![Recipe Details](/documentation/readme_images/recipe_detail.png)

* Events Page

    * The events page consists of an accordion that displays basic information for each event with further details available when expanded. In the expanded view the user can see full details (description, date, time, location) for each event along with a list of linked products that will be showcased at each event. Superusers will additionally have access to edit and delete options.

        ![Events](/documentation/readme_images/events.png)

* Profile Page

    * The profile page is only available to registered users and displays the user's order history and default delivery information. Housed within an accordion, the top card contains a list of the user's previous orders while the bottom card contains a form where the user can add or update their default delivery information. Each order within the order card is linked to an order summary page where the user can review full details of each order.

        ![Profile](/documentation/readme_images/profile.png)

* Favourites Page

    * The favourites page allows the user to compile a selection of favoured items that are easily accessible for future reference. A product name and price is displayed for each item alongside a minified product image. The product name and image both link to the description page for that particular item should the user wish to see further details or purchase the item. A remove button is also displayed beside each item should the user wish to remove that item from their favourites.

        ![Favourites](/documentation/readme_images/favourites.png)

* Basket

    * The basket page summarises the products added by the user, displaying a product name, sku, unit price, subtotal, delivery cost and grand total. It also contains a quantity selector which can be used to adjust the quantity of each item, it is also possible to remove individual products completely. 'Keep Shopping' and 'Checkout' buttons are at the bottom of the page and these link to the products page and checkout respectively.

        ![Basket](/documentation/readme_images/basket.png)

* Checkout Page

    * The checkout page consists of a form for the user to input their personal details and delivery information; this is auto-populated if a registered user has saved their default information. Underneath the form is a payment field supplied by Stripe for card details. At the bottom of the page there is an 'Adjust Basket' button, linked to the basket, and a 'Complete Order' button, used to submit the order.

        ![Checkout](/documentation/readme_images/checkout.png)

* Checkout Success Page

    * The checkout success page consists of a complete summary of the order, listing the order number, product name and quantity, delivery, and billing information. It also confirms to the user that an email was sent to the email address provided. A 'Forgot Something?' button is located at the bottom of the page to encourage them to search for additional products and links to the products page.

        ![Checkout Success](/documentation/readme_images/checkout_success.png)

* Footer

    * The footer consists of GotNoBeans copyright text and a mailto link which users can use to contact the site owner. It has an opacity of .5 to add lightness and allow the background image to be seen through it on the homepage.

        ![Footer](/documentation/readme_images/footer.png)

* Toasts

    * Bootstrap toasts are used to provide users with a variety of success, error, and alert messages. They disappear after a short period and can also be closed by the user.

        ![Toasts](/documentation/readme_images/toasts.png)

* Admin Features

    * Site admins (superusers) can perform full CRUD functionality on the site with the ability to create, read, update and delete products, recipes and events.
    * When an admin logs into the site, they are presented with an extra 'Admin' dropdown in the navbar containing links to add new products, recipes and events to the site.
    * Additionally, edit and delete options are available to them in the products and product detail pages, the recipes and recipe detail pages and the events page.

* Registered User Features

    * Users who have registered on the site have access to additional features that improve their user experience; including access to order history, a personal favourite products list and the ability to add and update their default personal and delivery information.
    * When a registered user logs into the site they are offered additional links under the 'Profile' dropdown in the navbar, specifically linking to their 'Profile' page and 'Favourites' list.
    * Their profile page shows a list of their previous orders and allows them to maintain their personal and delivery information.
    * The favourites page lists and items that they have favourited and links back to the product detail page for each individual item should they wish to purchase it at a future date. Products can be added to their favourites list by clicking on the "Add to Favourites' button on the product detail page.

&nbsp;

[Back to top &uarr;](#got-no-beans)

## Features to be Implemented in Future

* Breadcrumbs
    * The addition of breadcrumbs to the top of each page would be a useful way for users to keep track of where they are on the website.

* Favourite Recipes
    * In addition to having product favourites, it would be a nice feature to be able to do the same with brewing recipes; especially if the recipe selection expands greatly in the future.

* Categories CRUD
    * At present, full CRUD functionality is not required for the store as it specialises in a narrow range of goods. However, to allow for future growth it might be beneficial for admins to be able to create, update and delete product categories.

* Stock levels built in
    * It would be very useful for admins to include stock levels for each product and have these auto update when items are purchased through the store.

* Social Media Login
    * The ability to register and login using social media accounts would be a useful addition and provide a faster sign-up process to users.

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Libraries, Programs and Extensions
* [Amazon Web Services: AWS](https://aws.amazon.com/): Used to store static and media files.
* [Balsamiq](https://balsamiq.com/): Used to create site wireframes.
* [Bootstrap](https://getbootstrap.com/): Used to enable responsive front-end site development.
* [Django](https://www.djangoproject.com/): Used to build the project framework.
* [Font Awesome](https://fontawesome.com/): Used to locate and import icons used throughout the site.
* [Git](https://en.wikipedia.org/wiki/Git): Used as a project development environment and is connected to GitHub.
* [GitHub](https://en.wikipedia.org/wiki/GitHub): Used to hold the project repository which is linked to Heroku.
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
  * [LambdaTest](https://www.lambdatest.com/): Used to perform cross browser testing.

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Testing 

Testing information can be found in the [testing file][TESTING.md].

&nbsp;

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
2. Once in the repository, navigate to the "Fork" button at the top right hand corner of the page.
3. Click on the fork dropdown arrow and then select "Create a new fork".
4. You should now have a copy of the original repository in your GitHub account.

&nbsp;

## Making a Local Clone
1. Log in to GitHub and locate the repository: [GotNoBeans](https://github.com/davecoll3/GotNoBeans).
2. Click on the green "Code" button at the top of the page.
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

&nbsp;

[Back to top &uarr;](#got-no-beans)

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

[Back to top &uarr;](#got-no-beans)

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
21. Return to Heroku and navigate to your app's settings. In the Config Vars, add a new Config Var named "DISABLE_COLLECTSTATIC" and set its value to "1". This prevents Heroku from collecting static files when you deploy.
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
29. Back in Heroku, you can set your app to be deployed automatically by navigating to the app "Deploy" menu. Scrolling down to the 'Deployment Method' section and connecting it to github. You will need to search for your repository, once located click 'connect'. Then scroll further down and click 'Enable Automatic Deploys'. Once connected, your code will automatically deploy to Heroku whenever you push to github.

The live Heroku app link can be found [here](https://got-no-beans.herokuapp.com/)

&nbsp;

[Back to top &uarr;](#got-no-beans)

## AWS

### S3 Bucket
Amazon Web Services are used to store your static and media files.
1. Go to the AWS website and [create an account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email).
2. Once signed up and logged in, locate "My Account" in the navbar and then select "AWS Management Console".
3. From here, search for 'S3' search bar and select it from the search results.
4. On the S3 Buckets page, click on the "Create Bucket" button.
5. Name your new bucket (usually the same as your app name) and select your local region.
6. Under "Object Ownership" select "ACLs enabled" and then "Bucket owner preferred.
7. Uncheck "Block all public access" and acknowledge the change when prompted.
8. Scroll to the bottom and click on the "Create Bucket" button.
9. Navigate to your new bucket and, within the "Properties" tab, locate "static website hosting" by scrolling down to the bottom of the page. Click "Enable" and specify the index and error document names (index.html and error.html are fine for this). Click save.
10. Now navigate to the permissions tab, scroll down to the "Cross-origin resource sharing (CORS)" section. Click edit and paste in the following code:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
11. Scroll back up to the 'Bucket Policy' section. Click 'Edit' and then 'Policy generator'. This will open the AWS policy generator page.
12. Under the 'Select Type of Policy' dropdown, select 'S3 Bucket Policy'. Then inside 'Principle' allow all principals by typing '*' and from the 'Actions' dropdown, select 'Get object'.
13. Back in the previous tab, locate the Bucket ARN number. Copy this number and return to the policy generator, pasting it in the field labelled 'Amazon Resource Name (ARN)'. Then click 'Add Statement'.
14. From here click 'Generate Policy'. Copy the generated policy and paste it into the bucket policy editor.
15. Add a '/*' at the end of your resource key; this allows access to all resources in this bucket. Click 'Save'.
16. Now scroll down to the 'Access control list (ACL)' section and click 'Edit' and and enable list for 'Everyone (public access)';
accepting the warning box. Then click 'Save'.

&nbsp;

[Back to top &uarr;](#got-no-beans)

### IAM (Identity and Access Management)
1. Now that your bucket is ready, you will need to create a user to access it. In the search bar at the top of the window, search for IAM and select it from the search results.
2. On the IAM page, click 'User Groups' from the side bar, then click 'Create group'.
3. Name your group 'manage-your-project-name' and click 'Create Group' at the bottom of the page.
4. From the sidebar click 'Policies' and then 'Create policy'.
5. On the JSON tab, click 'Import Managed Policy'. Then search for 'S3' and select 'AmazonS3FullAccess'. Click import.
6. Once imported you will need to edit the policy slightly. Go back to your S3 bucket and copy your ARN number. Coming back to the policy, update the 'Resource' key to include your ARN and add a second line with your ARN followed by '/*'. See below for reference.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "your-arn-number",
                "your-arn-number/*"
            ]
        }
    ]
}
```
7. Now click 'Next: Tags' and then click 'Next: Review'. On the 'Review Policy' page give the policy a name and a short description. Click 'Create Policy'.
8. This will take you back to the policy page where you should see your new policy.
9. From the sidebar click 'User Groups' and select your group. Go to the permissions tab,
open the 'Add permissions' dropdown and click 'Attach policies'. Select the policy and click 'Add
permissions' at the bottom.
10. Finally you will create a user to put in the group. Select 'Users' from the sidebar and click 'Add user'.
11. Provide a username, check 'Programmatic Access' and then click the 'Next: Permissions' button.
12. Select your group, that has the policy attached, and click 'Next: Tags', 'Next: Review' and then 'Create user'.
13. On the next page you will need to download the CSV file. This contains the user's access key and secret access key which you will need.

### Connecting AWS to Django
Now that you have an S3 bucket, you will need to connect it to Django.
1. Start by installing Boto3 and Django-storages in your IDE. Run the following commands sequentially in your terminal:
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add 'storages' to your installed apps section inside your settings.py file.
3. Scroll down your setting.py file and add the settings below to let Django know which bucket it is communicating with. Somewhere near the bottom of the file you can write an if statement to check if there is an environment variable called USE_AWS. 
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
4. Go back to Heroku, in the settings tab, you will have additional Config Vars from the CSV file that you downloaded earlier. First, add 'AWS_ACCESS_KEY_ID' with the value in the CSV. Then add 'AWS_SECRET_ACCESS_KEY' with the value from the CSV file. Once they have both been added, add 'USE_AWS' and set it to True.
5. You can now remove the 'DISABLE_COLLECTSTAIC' variable, as django should now collect static files automatically and upload them to S3.
6. Return to your settings.py file, in your django project, and go back to the if statement you wrote earlier. In order to tell django where our static files will be coming from in production, inside the if statement add:
```
WS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
7. Now we need to create a file to tell django that we want to use S3 to store our static files, whenever someone runs collectstatic, and  that we want any uploaded images to go there too.
8. In the root directory of your project create a file called 'custom_storages.py'. Inside this file you will import your settings as well as the s3boto3 storage class. At the top of the file insert:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
```
9. Underneath these imports insert two classes.
```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
10. Back in the settings.py file, you will now define 'STATICFILES_LOCATION' and 'MEDIAFILES_LOCATION'. Underneath the bucket config settings, inside the if statement, add the following:
```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
```
11. You will now need to override and explicitly set the URLs for static and media files using your custom domain and new locations. You can do this by adding these two lines inside the if statement.
```
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
12. Save, add, commit and push your changes to GitHub which will, in turn, trigger an automatic deployment to Heroku. You should now see that your S3 bucket has a static folder with all your static files inside. 
13. Add the following code to help speed things up by letting the browser know that it's ok to cache static files for a long time.
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```
14. You complete if statement should now look something like this:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your-app-name'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
15. Back on AWS and in S3, go to your bucket. Click 'Create folder' and name it 'media'. Click 'Save'.
16. Inside this new media folder, click 'Upload' then 'Add files'. Select all the images that you are using on your site.
17. Under 'Permissions' select the option 'Grant public-read access' and click upload. You may also need to check an acknowledgment warning checkbox.
18. Once that is done, your static and media files should be automatically linked from django to your S3 bucket.

&nbsp;

[Back to top &uarr;](#got-no-beans)

## Stripe
Stripe is used to handle all payments in the checkout process. If you don't already have one, you will need to sign-up for an account which you can do on their [website](https://dashboard.stripe.com/register).

### Payments
You can set up Stripe payments by following their [step-by-step guide](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

### Webhooks
1. To set up a new webhook, log into your Stripe account and click 'Developers' on the navbar; top right-hand corner.
2. Click on the 'Webhooks' tab, just under the Developers heading, then 'Add endpoint'.
3. You will then need to input the URL for your Heroku app followed by '/checkout/wh/'. It should look something like this:
```
https://your-app-name.herokuapp.com/checkout/wh/
```
4. Then click the '+ Select events' button and check the 'Select all events' checkbox before clicking 'Add events' at the bottom. Once this is done finish the setup by clicking 'Add endpoint'.
5. Your webhook has now been created and it will have generated a secret key. You will need this to add to your Config Vars in Heroku.
6. Now go to your app in Heroku and under settings click 'Reveal Config Vars'. You will need the secret key from your newly generated webhook along with your Stripe 'Publishable Key' and 'Secret Key' which you can find in the API keys section of stripe.
```
STRIPE_PUBLIC_KEY = your_stripe_publishable_key
STRIPE_SECRET_KEY = your_secret_key
STRIPE_WH_SECRET = your_webhook_secret_key
```
7. To finish, go back to your setting.py file in your IDE and insert the following near the bottom of the file.
```
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```
8. You can now checkout using a test credit card number (such as 4242 4242 4242 4242) and check that they're coming through to your webhook on stripe.

&nbsp;

[Back to top &uarr;](#got-no-beans)

# Credits 

## Content 

* The Code Institute's readme-template provided the basic structure for the readme.md file.
* The Code Institute's Boutique Ado walkthrough project was used to provide the core structure and functionality.

## Media

* The favicon image was sourced from [Icons8](https://icons8.com) and was freely used under the [Icons8 licence](https://icons8.com/license).
* All site images were sourced from [Pexels](https://www.pexels.com/) and was freely used under the [Pexels licence](https://www.pexels.com/license/).

## Acknowledgements

* I would like to thank my mentor, Oluwaseun Owonikoko, who assisted me on this project.
* I would like to thank Iris Smok, the Code Institute's cohort facilitator for Coleg y Cymoedd, for her advice and encouragement.
* I would also like to acknowledge the support and advice obtained from the Code Institute's Tutor Support and Slack community. 

&nbsp;

[Back to top &uarr;](#got-no-beans)

[TESTING.md]: TESTING.md