# Testing 

## Table of Contents   
* [User Stories](#user-stories)
* [Lighthouse](#lighthouse)
* [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Colour Contrast](#colour-contrast)
* [Browser Compatibility](#browser-compatibility)
* [Responsiveness](#responsiveness)
* [Bugs](#bugs)
* [Unresolved Bugs](#unresolved-bugs)

## User Stories

### Site Admin
#### ID 1
* Expected
  * Site owner has access to store backend so that they can manage products, recipes and events.

* Testing
    <details><summary>Site Owner Testing: Backend Access</summary>
      <img src="documentation/testing_images/backend.png">
      <img src="documentation/testing_images/edit_delete.png">
    </details>

* Result
  * The site owner or admins(superusers) have access to an additional 'Admin' menu in the navbar when they login. This is in addition to edit and delete options connected to individual products, recipes and events.

&nbsp;

#### ID 2
* Expected
  * Site owner privliges are restriced to admins only.

* Testing
    <details><summary>Site Owner Testing: Restricted Access</summary>
      <img src="documentation/testing_images/access.png">
    </details>

* Result
  * Only admins have access to full CRUD functionality for site products, recipes and events.

&nbsp;

#### ID 3
* Expected
  * Site admins can add, edit and delete products on the site.

* Testing
    <details><summary>Site Owner Testing: Products</summary>
      <img src="documentation/testing_images/add_product.png">
      <img src="documentation/testing_images/edit_product.png">
      <img src="documentation/testing_images/delete_product.png">
    </details>

* Result
  * Only admins have access to full CRUD functionality for site products.

&nbsp;

#### ID 4
* Expected
  * Site admins can add, edit and delete recipes on the site.

* Testing
    <details><summary>Site Owner Testing: Recipes</summary>
      <img src="documentation/testing_images/add_recipe.png">
      <img src="documentation/testing_images/edit_recipe.png">
      <img src="documentation/testing_images/delete_recipe.png">
    </details>

* Result
  * Only admins have access to full CRUD functionality for site recipes.

&nbsp;

#### ID 5
* Expected
  * Site admins can add, edit and delete events on the site.

* Testing
    <details><summary>Site Owner Testing: Events</summary>
      <img src="documentation/testing_images/add_event.png">
      <img src="documentation/testing_images/edit_event.png">
      <img src="documentation/testing_images/delete_event.png">
    </details>

* Result
  * Only admins have access to full CRUD functionality for site events.

&nbsp;

### Viewing & Navigation
#### ID 6
* Expected
  * Site user can easily see the purpose of the site and be informed as to whether it meets their needs.

* Testing
    <details><summary>Site User Testing: Purpose</summary>
      <img src="documentation/testing_images/purpose.png">
    </details>

* Result
  * The homepage navbar, image, text, and 'Shop Now' button combine to inform the user of the site purpose.

&nbsp;

#### ID 7
* Expected
  * Site user can browse the full range of products, view the selection and make a purchase.

* Testing
    <details><summary>Site User Testing: Product Browsing</summary>
      <img src="documentation/testing_images/products.png">
    </details>

* Result
  * The products page lists a selection of products to all users which can be clicked for further information and to make a purchase.

&nbsp;

#### ID 8
* Expected
  * Site user can view individual product details and identify the price, description and image.

* Testing
    <details><summary>Site User Testing: Product Details</summary>
      <img src="documentation/testing_images/product_details">
    </details>

* Result
  * The product detail page displays such as price, description and an image to the use.

&nbsp;

#### ID 9
* Expected
  * Site user can see a running total for their basket and be informed as to how much they're spending.

* Testing
    <details><summary>Site User Testing: Basket Total</summary>
      <img src="documentation/testing_images/basket_total.png">
    </details>

* Result
  * The basket total, on the navbar, is highlighted in blue when there's something in the basket and auto-updates the price as items are added or removed.

&nbsp;

#### ID 10
* Expected
  * Site user can browse the full selection of recipes.

* Testing
    <details><summary>Site User Testing: Recipe Browsing</summary>
      <img src="documentation/testing_images/recipes.png">
    </details>

* Result
  * The recipes page lists a selection of recipes to all users which can be clicked for further information.

&nbsp;

#### ID 11
* Expected
  * Site user can view individual recipe details to see the recipe method and find linked products.

* Testing
    <details><summary>Site User Testing: Recipe Details</summary>
      <img src="documentation/testing_images/recipe_details.png">
    </details>

* Result
  * The recipe detail page displays the recipe method and links to related products.

&nbsp;

#### ID 12
* Expected
  * Site user can browse the full range of events and find any local events that interest them.

* Testing
    <details><summary>Site User Testing: Events Browsing</summary>
      <img src="documentation/testing_images/events.png">
    </details>

* Result
  * The events page lists a selection of events to all users which expand to expose further information.

&nbsp;

### Sorting & Searching
#### ID 13
* Expected
  * Site user can easliy sort the list of products available and find products by price or name.

* Testing
    <details><summary>Site User Testing: Sort Products</summary>
      <img src="documentation/testing_images/sort_products.png">
    </details>

* Result
  * The sort dropdown, on the products page, allows users to sort products by price or name.

&nbsp;

#### ID 14
* Expected
  * Site user can easily sort products by category and narrow products down to the most relevant.

* Testing
    <details><summary>Site User Testing: Sort Categories</summary>
      <img src="documentation/testing_images/sort_cats.png">
    </details>

* Result
  * The catagories badges, under the header on the products page, allows users to sort products by category.

&nbsp;

#### ID 15
* Expected
  * Site user can search products by name or description and find a specific product.

* Testing
    <details><summary>Site User Testing: Search Bar</summary>
      <img src="documentation/testing_images/search_bar.png">
    </details>

* Result
  * The search bar allows the user to search all products by name or description.

&nbsp;

#### ID 16
* Expected
  * Site user can view a filtered products list based on their search.

* Testing
    <details><summary>Site User Testing: Search Results</summary>
      <img src="documentation/testing_images/search.png">
    </details>

* Result
  * The search results are shown as a filtered list on the products page.

&nbsp;

### Basket & Checkout
#### ID 17
* Expected
  * Site user can easliy add products to their basket and compile a selection of products to purchase.

* Testing
    <details><summary>Site User Testing: Add to Basket</summary>
      <img src="documentation/testing_images/add_basket.png">
    </details>

* Result
  * The 'Add to Basket' button, on the products page, allows users to add one or multiple products to their basket.

&nbsp;

#### ID 18
* Expected
  * Site user can view the products in their basket to see what they have selected and adjust if needed.

* Testing
    <details><summary>Site User Testing: Basket</summary>
      <img src="documentation/testing_images/basket.png">
    </details>

* Result
  * Clicking on the basket icon, in the navbar, brings the user to the basket page where they can view and adjust the items in their basket and totals.

&nbsp;

#### ID 19
* Expected
  * Site user can easily enter their delivery and payment details allowing for a quick and hassel free purchase.

* Testing
    <details><summary>Site User Testing: Checkout</summary>
      <img src="documentation/testing_images/checkot.png">
    </details>

* Result
  * The checkout page contains a form in which a guest user can enter their delivery details. Registered users can save their default information to negate the need to enter it each time they make a purchase.

&nbsp;

#### ID 20
* Expected
  * Site user can see their order confirmation after checkout and verify that the order details are correct.

* Testing
    <details><summary>Site User Testing: Order Confirmation</summary>
      <img src="documentation/testing_images/order_confirmation.png">
    </details>

* Result
  * The checkout success page confirms that the order has been placed and provides an order summary. A success toast message is also displayed to the user.

&nbsp;

#### ID 21
* Expected
  * Site user will recieve an order confirmation email to keep order details for their records.

* Testing
    <details><summary>Site User Testing: Order Confirmation Email</summary>
      <img src="documentation/testing_images/order_email.png">
    </details>

* Result
  * Upon completion of the purchase, and email is sent to the user to confirm that it has been successfully placed and provides a summary.

&nbsp;

### Registration & User Accounts
#### ID 22
* Expected
  * Site user can easliy register for a new account and	have a personal profile.

* Testing
    <details><summary>Site User Testing: Register</summary>
      <img src="documentation/testing_images/register.png">
    </details>

* Result
  * By selecting the 'Profile' dropdown, in the navbar, users will have the option of registering which will bring them to a sign-up page.

&nbsp;

#### ID 23
* Expected
  * Registered users recieve a verification email during registration so that they can be confident that their registration was successful.

* Testing
    <details><summary>Site User Testing: Email Verification</summary>
      <img src="documentation/testing_images/verification.png">
    </details>

* Result
  * When a valid sign-up form has been submitted, an email verification email is sent to the user allowing them to complete their registration.

&nbsp;

#### ID 24
* Expected
  * Registered users can easliy sign in and out of their accout.

* Testing
    <details><summary>Site User Testing: Sign in & Out</summary>
      <img src="documentation/testing_images/sign_in.png">
    </details>

* Result
  * Sign in and out buttons are easily available at all times form the 'Account' dropdown in the navbar.

&nbsp;

#### ID 25
* Expected
  * Registered users can recover their email if they forget it.

* Testing
    <details><summary>Site User Testing: Password Recovery</summary>
      <img src="documentation/testing_images/password.png">
    </details>

* Result
  * Under the 'Sign In' button on the sign in page, there is a link to a password recovery page which sends a recovery email to the user's email address.

&nbsp;

#### ID 26
* Expected
  * Registered users have a personal user profile which shows their order history and default delivery details.

* Testing
    <details><summary>Site User Testing: Profile</summary>
      <img src="documentation/testing_images/profile.png">
    </details>

* Result
  * The user's profile is easily accessible at all times form the 'Account' dropdown in the navbar. This contains their order history and default delivery information, which they can update.

&nbsp;

#### ID 27
* Expected
  * Registered users can keep a list of their favourite products.

* Testing
    <details><summary>Site User Testing: Favourites</summary>
      <img src="documentation/testing_images/favourites.png">
    </details>

* Result
  * The user's favourites list is easily accessible at all times form the 'Account' dropdown in the navbar. This contains basic information on each product and links to it. They can also remove products from thir favourites here.

&nbsp;




&nbsp;

[Back to top &uarr;](#testing)

## Lighthouse
[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit performance, accessibility, best practices and SEO.

  * Desktop
    * [Lighthouse Report: Desktop](/documentation/testing_docs/lighthouse_desktop.pdf)
    * [Lighthouse Report: Mobile](/documentation/testing_docs/lighthouse_mobile.pdf)

&nbsp;

[Back to top &uarr;](#testing)

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

[Back to top &uarr;](#testing)

## Browser Compatibility

[LambdaTest](https://www.lambdatest.com/) was used to test the site across a number of browsers, including:

### Chrome: Windows
  <details><summary>GotNoBeans on Chrome.</summary>
  <img src="#">
  </details>
  
  &nbsp;

  ### Chrome: Android
  <details><summary>GotNoBeans on Chrome (Android).</summary>
  <img src="#">
  </details>

  &nbsp;

  ### Safari: MacOS
  <details><summary>GotNoBeans on Safari.</summary>
  <img src="#">
  </details>

  &nbsp;

  ### Safari: iOS
  <details><summary>GotNoBeans on Safari (iOS).</summary>
  <img src="#">
  </details>

  &nbsp;

  ### MS Edge: Windows
  <details><summary>GotNoBeans on MS Edge.</summary>
  <img src="#">
  </details>

  &nbsp;

  ### Firefox: Windows
  <details><summary>GotNoBeans on Firefox.</summary>
  <img src="#">
  </details>

  &nbsp;

  ### Opera: Windows
  <details><summary>GotNoBeans on Opera.</summary>
  <img src="#">
  </details>

  &nbsp;

  ### Brave: Windows
  <details><summary>GotNoBeans on Brave.</summary>
  <img src="#">
  </details>

&nbsp;

[Back to top &uarr;](#testing)

## Responsiveness

&nbsp;

[Back to top &uarr;](#testing)

## Bugs

### Function: get_terms
  During the development of the project the get_terms function was causing a type error

  <details><summary>Type Error Screenshot</summary>
  <img src="#">
  </details>

  After researching TypeError: object of type 'Cursor' has no len(), it was discovered that the use of terms = mongo.db.terms.find() was causing the bug; as shown below.
  ```
    @app.route("/get_terms")
    def get_terms():
        terms = mongo.db.terms.find()
        return render_template("terms.html", terms=terms)


    @app.route("/search", methods=["GET", "POST"])
    def search():
        query = request.form.get("query")
        terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
        return render_template("terms.html", terms=terms)
  ```

  This was resolved by changing terms to equal list(mongo.db.terms.find()); as below.
  ```
    @app.route("/get_terms")
    def get_terms():
        terms = list(mongo.db.terms.find())
        return render_template("terms.html", terms=terms)
  ```

&nbsp;

[Back to top &uarr;](#testing)

## Unresolved Bugs
 
 ### Navbar Menu Items Not Active
   Materialize allows for an active class to be added to the menu < li > elements to highlight, on the navbar, which page the user is currently on. However, due to the navbar code only appearing on the base.html file, it is not as simple to implement as is shown in the Materialize documentation and requires further jinja or JavaScript code to achieve this. In order to mitigate the effects of this, page headers are used to help signpost the current page to users.

&nbsp;

[Back to top &uarr;](#testing)

[Back to README.md doc](README.md)