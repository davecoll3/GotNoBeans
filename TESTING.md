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
* Expected
  * Site owner has access to store backend so that they can manage products, recipes and events.

* Testing
    <details><summary>Site Owner Testing: Backend Access</summary>
      <img src="documentation/testing_images/backend.png">
      <img src="documentation/testing_images/edit_delete.png">
    </details>

* Result
  * The site owner or admin has access to an additional 'Admin' menu in the navbar when they login. This is in addition to edit and delete options connected to individual products, recipes and events.

&nbsp;

* Expected
  * Site owner privliges are restriced to admins/superusers only.

* Testing
    <details><summary>Site Owner Testing: Restricted Access</summary>
      <img src="documentation/testing_images/backend.png">
      <img src="documentation/testing_images/edit_delete.png">
    </details>

* Result
  * Only admins/superusers have access to full CRUD functionality for site products, recipes and events.

&nbsp;

[Back to top &uarr;](#testing)

## Lighthouse
[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit performance, accessibility, best practices and SEO across the website.

  * Desktop
    * [Lighthouse Report: Home](#)
    * [Lighthouse Report: Profile](#)
    * [Lighthouse Report: Add Term](#)
    * [Lighthouse Report: Log In](#)
    * [Lighthouse Report: Sign Up](#)

    &nbsp;

  * Mobile
    * [Lighthouse Report: Home](#)
    * [Lighthouse Report: Profile](#)
    * [Lighthouse Report: Add Term](#)
    * [Lighthouse Report: Log In](#)
    * [Lighthouse Report: Sign Up](#)

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