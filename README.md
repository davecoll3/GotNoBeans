# GotNoBeans

GotNoBeans is an online retailer specialising in coffee brewing equipment. Specifically targeted at the home enthusiast. they offer a wide variety of home brewers and accessories. Beyond this, they offer brewing recipes that are specific to their products to empower users to feel confident when purchasing a product they are unfamilar with. In order to promte the business and build a community around it, GotNoBeans host events around the UK during which they showcase and educate around their products.

The GotNoBeans website is a full-stack e-commerce site built using Django, Python, jQuery, CSS, and HTML.

[View the live site here](https://got-no-beans.herokuapp.com/)

&nbsp;

![Responsive Mockup](/documentation/readme_images/mockup.webp)

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
    * [Frameworks](#frameworks)
    * [Template Engine](#template-engine)
    * [Database](#database)
    * [Application Platform](#application-platform)
    * [Version Control](#version-control)
    * [Libraries](#libraries)
    * [Testing and Validation Tools](#testing-and-validation-tools)
* [Testing](#testing)
* [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Colour Contrast](#colour-contrast)
* [Deployment](#deployment)
    * [Creating a GitHub Repository](#creating-a-github-repository)
    * [Forking the GitHub Repository](#forking-the-github-repository)
    * [Making a Local Clone](#making-a-local-clone)
    * [Heroku Deployment: Project Setup](#heroku-deployment-project-setup)
    * [Heroku Deployment: Create a Heroku App](#heroku-deployment-create-a-heroku-app)
    * [Heroku Deployment: Deploy to Heroku](#heroku-deployment-deploy-to-heroku)
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

[Back to top &uarr;](#GotNoBeans)

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

[Back to top &uarr;](#GotNoBeans)

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

  * The products and recipes pages follow the same format displaying images for each item alond with a name, both linked to that item's description page; the products page additionally shows the item price and has a sort selector for sorting the products by name or price. Edit and delete options are also displayed to superusers.

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


## Features to be Implemented in Future

* Example Heading
  * In the future...

&nbsp;

* Example Heading
  * In the future...

&nbsp;

[Back to top &uarr;](#GotNoBeans)

# Technologies Used

## Languages
  * [HTML](https://en.wikipedia.org/wiki/HTML)
  * [CSS](https://en.wikipedia.org/wiki/CSS)
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks
  * [Django](#)
  * [Bootstrap](#)

## Template Engine
  * [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))

## Database
  * [#](#)

## Application Platform
  * [Heroku](https://en.wikipedia.org/wiki/Heroku)

## Version Control
  * [Git](https://en.wikipedia.org/wiki/Git)
  * [GitHub](https://en.wikipedia.org/wiki/GitHub)

## Libraries
  * [Font Awesome](https://fontawesome.com/)
    * Font Awesome was used to locate and import icons used throughout the site.
  * [Google Fonts](https://fonts.google.com/)
    * Google Fonts was used to import the 'Rubik' font used throughout the site.

## Testing and Validation Tools
  * [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Google Chrome DevTools was used to carry out manual testing on the website and to simulate mobile devices.
  * [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)
    * The W3C Markup Validation Service was used to check the markup validity of the html code. 
  * [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_uri)
    * The W3C CSS Validation Service was used to validate the css code.
  * [JSHint](https://jshint.com/)
    * The JSHint static code analysis tool was used to check if the JavaScript source code complies with coding rules.
  * [CI Python Linter](https://pep8ci.herokuapp.com/)
    * The Code Institute Python Linter ensures that the code is PEP8 compliant.
  * [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
    * Lighthouse was used to audit performance, accessibility, best practices and SEO across the website.
  * [a11y](https://color.a11y.com/)
    * The a11y Colour Contrast Accessibility Validator was used to verify that the colour contrast across the site adhered to the WCAG 2.1 Guidelines.
  * [LambdaTest](https://www.lambdatest.com/)
    * LambdaTest was used to perform cross browser testing.

&nbsp;

[Back to top &uarr;](#GotNoBeans)

# Testing 

Testing information can be found in the [testing file][TESTING.md].

&nbsp;

[Back to top &uarr;](#GotNoBeans)

# Validation

## HTML
The [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) was used to validate the code. The code was successfully validated with no errors or warnings.

<details><summary>Home</summary>
<img src="#">
</details>

<details><summary>Profile</summary>
<img src="#">
</details>

<details><summary>Add Term</summary>
<img src="#">
</details>

<details><summary>Edit Term</summary>
<img src="#">
</details>

<details><summary>Log In</summary>
<img src="#">
</details>

<details><summary>Sign Up</summary>
<img src="#">
</details>

&nbsp;

## CSS
The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_uri) was used to validate the code. The code was successfully validated with no errors or warnings.

<details><summary>CSS Validation</summary>
<img src="#">
</details>

&nbsp;

## JavaScript
[JSHint](https://jshint.com/) was used to check if the JavaScript code complies with coding rules. The code was successfully validated with no errors or warnings. The undefined variable shown 'M' relates to Materialize CCS Initialization code.

<details><summary>JavaScript Validation</summary>
<img src="#">
</details>

&nbsp;

## Python
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check if the Python code is PEP 8 compliant. The code was successfully processed by the linter with no errors found.

<details><summary>Python Linting</summary>
<img src="#">
</details>

&nbsp;

## Colour Contrast
The colour contrast accessibility validator [a11y](https://color.a11y.com/) was used to verify that the colour contrast across the site adhered to the [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/).

<details>
<summary>colour Contrast Validation</summary>

![colour Contrast Validation](#)
</details>

&nbsp;

[Back to top &uarr;](#GotNoBeans)

# Deployment

## Creating a Gitpod Repository

A GitHub repository is used to store your project, with Git and GitHub used for version control. The following steps outline how to create a GitHub repository.
  1. Log in to GitHub.
  2. In the upper-right corner of any page, use the '+' drop-down menu and select 'New repository'.
  3. Give your repo a short, memorable name.
  4. Choose your repository visibility; 'Public' or 'Private'.
  5. Select Initialize this repository with a README.
  6. Click Create repository.

&nbsp;

## Forking the GitHub Repository

Forking the GitHub Repository makes a copy of the original repository on our GitHub account; allowing you to view and/or make changes without affecting the original repository and can be done by using the following steps.
  1. Log in to GitHub and locate the repository: [GotNoBeans](https://github.com/davecoll3/GotNoBeans).
  2. Once in the repository, navigate to the "Fork" button at the top right of the page; just above the settings button on the menu.
  3. You should now have a copy of the original repository in your GitHub account.

&nbsp;

## Making a Local Clone
  1. Log in to GitHub and locate the repository: [GotNoBeans](https://github.com/davecoll3/GotNoBeans).
  2. Under the repository name, click "Clone or download".
  3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
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

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Heroku Deployment: Project Setup

If you don't have a Heroku account, or if you have yet to install the Heroku CLI, see [How to Install the Heroku CLI](https://coding-boot-camp.github.io/full-stack/heroku/how-to-install-the-heroku-cli) before you proceed.

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

[Back to top &uarr;](#GotNoBeans)

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

  [Back to top &uarr;](#GotNoBeans)

[TESTING.md]: TESTING.md