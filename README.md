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
    * [Color Contrast](#color-contrast)
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
* Color choices for links and buttons should be familar and logical.
* A reactive site that is user friendly and well presented on all types of device and screen sizes.
* Adequate levels of color contrast across the site that presents content in an accessible and easy to read manner.

&nbsp;

## Design

### Image
* A large colorful image showing a selection of coffee brewers is used as a background for the site homepage. The image itself is visually appealing while also making a direct link to the products sold on the site. This immediately demonstrates to the user the purpose of the site and is ovelayed with a 'Shop Now' which encourages them to view the products on offer. The tagline of "You do the brew, we'll do the beans" is used to convey that the site specailses in brewing equipment rather than coffee itself. 

### Color Scheme
* Black (#000)...

### Fonts

* The Google font of...
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

  ... was chosen as the database for this project.
  <summary>GotNoBeans Data Model</summary>

  ![Data Model](#)

  </details>

&nbsp;

[Back to top &uarr;](#GotNoBeans)

# Features 

## Existing Features

* Navigation Bar

  * Featured on all pages, the full responsive navigation bar includes...

    ![Navbar: Desktop](#)

    <details>
    <summary>Navbar: Mobile</summary>

    ![Navbar: Mobile](#)

    </details>
    
    <details>
    <summary>Sidenav: Mobile</summary>

    ![Sidenav: Mobile](#)

    </details>

* Homepage Carousel

  * A carousel...

    ![Homepage Carousel](#)

  * The carousel also contains...

    ![Homepage Carousel](#)

* Profile: Header

  * The profile header contains...

    ![Profile: Header](#)

* Edit Item Form

  * A page header sits above the edit term form...

    ![Add Item Form](#)

* Delete Item Modal

  * Should the admin, select the 'Delete' button...

    ![Delete Item Modal](#)

* Add Item Form

  * A page header sits above the...

    ![Add Item Form](#)

* Log-In Page

  * A page header sits...

    ![Log In](#)

* Sign-Up Page

  * A page header sits...

    ![Log In](#)

* Flash Message

  * The flash messages...

    ![Flash Message](#)

* Back to Top Button

  * A floating back to top button was used...

    ![Back-to-Top Btn](#)

* Footer

  * The footer consists of...

    ![Footer](#)


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
    * The a11y Color Contrast Accessibility Validator was used to verify that the colour contrast across the site adhered to the WCAG 2.1 Guidelines.
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

## Color Contrast
The color contrast accessibility validator [a11y](https://color.a11y.com/) was used to verify that the colour contrast across the site adhered to the [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/).

<details>
<summary>Color Contrast Validation</summary>

![Color Contrast Validation](#)
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