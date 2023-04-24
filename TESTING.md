# Testing 

## Table of Contents   
* [Manual Testing](#manual-testing)
* [Lighthouse](#lighthouse)
* [Browser Compatibility](#browser-compatibility)
* [Bugs](#bugs)
* [Unresolved Bugs](#unresolved-bugs)

## Manual Testing

### Navbar
* Expected
  * The navbar should be...

* Testing
  * The navbar was tested...
    <details><summary>Navbar Testing: Unregistered User</summary>
      <img src="#">
    </details>
    <details><summary>Navbar Testing: Registered User</summary>
      <img src="#">
    </details>

* Result
  * The navbar responded...

&nbsp;

### Homepage Carousel

  * Expected
    * The homepage carousel...

  * Testing
    * The homepage carousel...
      <details><summary>Homepage Carousel</summary>
        <img src="#">
      </details>

  * Result
    * The homepage carousel...

&nbsp;

### Add New Item Form

  * Expected
    * The form heading should...

  * Testing
    * The...
      <details><summary>Add New Item Form Testing</summary>
        <img src="#">
      </details>

  * Result
    * The form heading...

&nbsp;

### Log In Page

  * Expected
    * The log in page should consist of...

  * Testing
    * The log in page was tested for responsiveness...
      <details><summary>Log In Page Testing</summary>
        <img src="#">
      </details>

  * Result
    * The log in page consists of...

&nbsp;

### Sign Up Page

  * Expected
    * The sign up page should consist of...

  * Testing
    * The log in page was tested for responsiveness...
      <details><summary>Sign Up Page Testing</summary>
        <img src="#">
      </details>

  * Result
    * The sign up page consists of...

&nbsp;

### Flash Messages

  * Expected
    * The flash messages should...

  * Testing
    * The flash message was tested...
      <details><summary>Flash Message Testing</summary>
        <img src="#">
      </details>

  * Result
    * The flash messages...

&nbsp;

### Back to Top Button

  * Expected
    * The back to top button should...

  * Testing
    * The back to top button was tested...
      <details><summary>Back to Top Button Testing</summary>
        <img src="#">
      </details>

  * Result
    * The back to top button responded...

&nbsp;

### Footer

  * Expected
    * The footer should be located...

  * Testing
    * The footer was tested...
      <details><summary>Footer Testing</summary>
        <img src="#">
      </details>

  * Result
    * The footer is located...

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