![image]()

# Waste Not Want Not
> ## To help households reduce food waste

[View the website here](https://mgreenberry.github.io/MS2-Smart-Associates/)

## About

This is my MS3 Backend Development Milstone Project website created as part of a Full Stack Software Development in Code Institute by [Michael Greenberry](https://www.linkedin.com/in/michael-greenberry-637299108/).

I created this website to provide a easy and simple website for a food waste app.

The app targets users that would like to manage their food waste either at home or in a small corner shop.

![Mockup]()

## Table of contents
1. [UX - User Experience](#ux-user-experience)
   * [Project Goals](#project-goals)
   * [User Stories](#user-stories)
   * [Design Choices](#design-choices)
     1. [Typography](#typography)
     2. [Colours](#colours)
     3. [Imagery](#imagery)
     4. [Icons](#icons)
     5. [Layout](#layout)
   * [Wireframes](#wireframes)
2. [Features](#features)
   * [Existing Features](#existing-features)
     1. [All Pages](#all-pages)
     2. [index.html](#index)
     3. [services.html](#services)
     4. [projects.html](#projects)
     5. [contact-us.html](#contact-us)
     6. [404.html](#404)
   * [Features Left To Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Framework Library](#framework-library)
   * [Tools](#tools)
   * [Testing Tools](#testing-tools)
4. [Testing](TESTING.md)
5. [Deployment](#deployment)
   * [Project creation](#project-creation)
   * [Deployment of existing site](#deployment-of-existing-site)
   * [Forking](#forking)
   * [Cloning and Implementing Locally](#cloning-and-implementing-locally)
6. [Credits](#credits)
   * [Content](#content)
   * [Media](#media)
   * [Icons](#icons)
   * [Code](#code)
     1. [HTML](#html)
     2. [CSS](#css)
     3. [JavaScript](#javascript)
7. [Acknowledgements](#acknowledgements)
8. [Author Information](#author-information)

## UX (User Experience)

### Project Goals
* To provide a simple, clean and easy website for the user
* To provide an easy to use food stock that would highlight the order that food needs to be used by
* To provide an 'About Us' page to explain the concept
* To provide a 'Log In' page for users to access their account, which will allow them to edit food lists, delete and create food lists.
There would also be a 'Log Out' section for the user so that no one else can change food lists.
* To provide a 'Register' to allow users to register for an account.
* To provide a contact form which when filled in would send an email to the company.

### User Stories

* As a user visiting the site for the first time:
  1. I want to be able to use the website on any device they own or use
  2. I want to able to learn and easily understand what the website is about
  3. I want to easily understand about how the app works
  4. I want to easily understand what each section of the app does
  5. I want to click on navigation links to be taken to the correct page/section and to be able to return to the home page or another page without using the brower forward/backward buttons
  6. I want these navigation links to include user friendly menus which are easy to uderstand and use
  7. I want the content to be easy to read and have a predictable layout so that each page can be navigated easily
  8. I want to access contact information, such as address, phone numbers and location
* Technical User Stories
    1. I want to be able to register for an account and log in wihtout difficulty
    2. I want to be able to add food bought to a stock list
    3. I want to be able to see a list of food listed by 'use by date' with the earliest date shown first
    4. I want to be able to manipulate this list by doing the following: -
      1. edit items on the stock list
      2. delete items from this list
    5. I want to be able to add expired or used food products to a shopping list
    6. I want to be able to add expired food products to a waste list if items are thrown away

* This app will do this by:-
  1. Design a responisive website focussed for mobile devices and responsive to larger screens.
  2. Design a home page with an 'about' section
  3. Include instructions on the home page
  4. Design navigation tabs which clearly display each section link
  5. Design and impliment a navigation bar which contains links to different pages and sections in the website 
  6. Design and label the navigation bar with clear and understandable text to direct users to the correct page  
  7. Design the website to have good readability throughout
  8. Design a contact us page with contact details
* Technical solutions
    1. Create a registration page which will store user details such as username as password safely
    2. To link users inputs to a database to store food that user enters as bought
    3. To use a sort function on the stock list to display food items in a 'use by date' list, with the earliest date first
    4. To create buttons and modals which allow the user to edit and/or delete food items
    5. To allow user to add used or thrown food to a shopping list
    6. To allow user to add expired/thrown food to a waste list if they require to track their waste

TO BE IMPLEMENTED!
* As a user returning to the site:
  1. To send an email with suggestions, complaints, etc.
  2. To search for a food item in any list - food stock, shopping and waste and to then edit/delete/add to lists.

* The owner/creator will do this by:
  1. Create a form in a contact us section
  2. Create a fuction which will allow user to search and edit/delete/add food to lists

[Back to content](#table-of-contents)
### Design Choices

#### Typography

For fonts, I used [Google Fonts](https://fonts.google.com) for my website. 

I have chosen the font-family: [](), sans-serif; for the Headings and Menu sections of the website as it is easy to read and has a nice cursive font which matches the style of the website. I also felt this fitted in well with the design of the website.

#### Colours

For this website I chose a colour pallette that matched similar websites that are professional and clean. The background colour is black, the Nav bar and button text is Navy Blue and menus, some text and buttons are based on the blue and red logo.

The colours I picked are as follows: -
![Coolors Palette]()

From: [Coolors Palette]()

#### Imagery

All images and photographs were added by the creator/owner

* Favicom:
  * Waste Bin: [Hero Image]()

* index.html
  1. Cover Images: [The main Image](assets/images/index/wastebin.jpg)

* log-in.html & register.html
  1. 

* food-stock.html
  * [Image 1]()
  * [Image 2]()
  
* contactUs.html

  1. 

### Icons

LIST ICONS

### Layout

This website is designed with access from the home page to all other pages from the navigation bar. The error 404.html page also includes links to other pages, i.e. index.html.

However, the 404.html is not accessed from the navigation bar or from any of the pages of the website. The 404.html page only displays when a user enters or searches for a page that doens't exist. The 404.html page allows the user to navigate to the main website.

[]() 

This blueprint was then used to design the navigation and call-out buttons featured in the website.

[Back to content](#table-of-contents)
## Wireframes
I used Balsamiq to create my wireframes. I chose to do a mobile version first with the pages I wanted and then create a desktop version after. I did this as this was going to be the way I designed my website, mobile first.

As I wanted to include this on all formats and devices I created my wireframes again for all pages and added the following to show mobile, tablet and desktop:

**Mobile**
* [Home](docs/mobile-home-page.pdf)
* [Log In]()
* [Register]()
* [Food List]()
* [Shopping List]()
* [Waste List]()
* [Contact-Us]()

**Tablet**
* [Home Page]()
* [Log In]()
* [Register]()
* [Food List]()
* [Shopping List]()
* [Waste List]()
* [Contact-Us]()

**Desktop**
* [Home Page]()
* [Log In]()
* [Register]()
* [Food List]()
* [Shopping List]()
* [Waste List]()
* [Contact-Us]()

I then added a '404.html. page for when the user enters an incorrect page address in the browser. I didn't create a wireframe for this page.

[Back to content](#table-of-contents)
## Features

### Existing Features

#### All Pages

Every page contains the following features at the top of the website as standard: -
* Text as a header reading "Waste Not Want Not" which also acts as a clickable event to take to the home page
* A responsive navigation bar, which reduces into a 'hamburger' navigation bar on mobiles. Allows all users to click on the page they want and access said page easily. Each navigation bar has the following links: -
  1. Food List/Home page - displays food stock list in the order of use-by-date
  2. Log In - allows users to access the the editing, adding and deleting of food acitons
  3. Register - allows users to sign up for the Log In page
  4. About/Contact Us - Information on the app and it's creator

#### Log In
Once logged in the user will then see additional navigation items: -
  1. Food List/Home page - displays food stock list in the order of use-by-date
  2. Add Food - allows users to add food to a food stock list
    * Will also allow logged in users to edit food items, delete food items
    * An option to add used or thrown out/expired food to a shopping list and/or a wast food list
  3. A Log Out page

Every page contains the following features in the footer: -
* Copyright for the website
* Copyright for Michael Greenberry (creator of this website)

#### Food List
* This page contains 1 section as follows: -
  1. A list of food items currently stocked by the user in a use-by-date order (this will allow editing only when user is logged in)
#### Log In/Register
* This page contains 1 section as follows: -
  1. A form for the user to register or log in to the app/website

#### Add Food
* This page contains 1 section as follows: -
  1. A form that allows the user to add food items to the food stock list
    * Users will also be able to edit/delete items from stock list
    * Users will also be able to add food wasted to a wasted food list
    * Users will also be able to add food items from waste or used stock to a shopping list

#### Shopping
* This page contains 1 section as follows: -
  1. A list of items that a user wishes to purchase taken from food used up/wasted or added by user

#### Waste
* This page contains 1 section as follows: -
  1. A list of items that a user has had to waste taken from food used up/wasted or added by user  

#### Log Out
* Allows user to log out of current session

#### About/contact-us
* This page contains 1 section as follows: -
  1. A contact form with 'First Name', 'Last Name', 'Email Address', and 'Message' fields. This allows the user to input their information and find out more details, ask questions about the business.
* There are 2 call-out buttons under this form. The first button **Reset** resets the form in case of user input error. The second button **Submit** allows the user to send their form to the business. On doing this their email will be sent to the business. Users will need to provide information in all fields, with a valid @ email address in order to be able to submit forms. This allows the website to only recieve valid customer comments.

#### 404
* This page is not linked to any other page in the website
* This page is only accessed if a user types an incorrect web address in the browser navigation bar
* This page contains the following section: -
  * A message notifying the user of an error. This then allows the user to recognise that the web address doens't exist.
  * There is 1 call-out button in this section. This allows the user to return to the home page of the main website - []()

### Features Left to Implement


[Back to content](#table-of-contents)
## Technologies Used
### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML5) Used as the main markup language of the website content
* [CSS](https://en.wikipedia.org/wiki/CSS) Used to style the content of the website
* [JavaScript](https://www.javascript.com/) Used with Bootstrap for the Navigation menu at the top and bottom of the website and for all interactive parts of the website
* [JQuery](https://jquery.com/) Used for temperal literals in some javascript code.
* [Python]()
* [Flask]()
* [Jinga]()

### Framework Library
* [Materalize]() Used for a mobile first responsive website, display properties such as grid layout, preset css such as for containers, forms, etc
* [JQuery](https://jquery.com/) Used for temperal literals in some javascript code.
### Tools
* [Wireframes with Balsamiq](https://balsamiq.com/) To create mockups of the website to aid creation
* [Github](https://github.com/) To store and host source code
* [Gitpod](https://gitpod.io/) To write the code 
* [Google Fonts](https://fonts.google.com) for the fonts used in the website
* [Coolors](https://coolors.co/) to source the main colours for the website
* [Favicons](https://www.favicon.cc) to create a favicon for the tab and website title
* [Heroku]() 
### Testing Tools
* [hmtl validation](https://validator.w3.org) to check the html code had no errors
* [css validation](https://jigsaw.w3.org/css-validator/) to check the css code had no errors
* [JAVASCRIPT](https://jshint.com/) to check for warnings/errors
* []() to text Python code
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) an online validation tool that helps to improve performance and quality of the webpage with helpful tips to improve as each html page is scored.

[Back to content](#table-of-contents)
## Testing
Testing information can be found [here](TESTING.md)

[Back to content](#table-of-contents)
## Deployment

### Project creation
* The website project was created by going to [Github](https://github.com/), a code hosting platform, using the following steps: -
  1. Create an account using an email address and password or a google account
  2. Log in to account and create a new repository![](/assets/images/readme-images/creating-new-repository.png)
  3. Give this new repository a creative name. Then click the green Gitpod button which will take you to [Gitpod](https://gitpod.io/workspaces). Gitpod is an open source platform for code development ![](assets/images/readme-images/creating-respository-step-one.png) ![](assets/images/readme-images/ms2-smart-associates-gitpod.png)
  4. Then open this platform and start coding
  5. To save the work I had to do the following: - Click 'File', click 'auto save'
  6. To save the work to github I needed to do the following: -
    * git add (either the name of the file, i.e. index.html or '.' which adds everything that has been worked on that day)
    * git commit (either the name of the file, i.e. index.html or '-m' and then add a comment in parenthesis "" and enter)
    * It is recommended to commit daily. To complete the necessary steps to upload to github I needed to use the command - git push. This then 'pushed' all the saved work back to Github
### Deployment of existing site
* The following steps were taken to deploy this site and make it 'live': - 
  1. On Github.com go to the repository, go the the project main page ![]()
  2. Click on 'Settings' and then scroll down to the section 'GitHub Pages' ![]()
  3. Click on the 'Pages' tab and then click 'Source' and choose 'Master' under the 'Branch' tab, then 'Root' and click save ![]()
  4. The link is now available for you to publish above this. ![]()
### Forking  
* If you wish to use this repository as a starting point for your own design, or to contribute to this project, you can fork it. Follow the steps below.
  1. Navigate to the repository in [github](https://github.com/). 
  2. Choose the correct repository. In this case it is []()
  2. Click 'Fork' in the top-right corner. ![]()
  4. This will then create a copy (make sure you have already created your own github account) in your repository
  5. Now follow the steps outlined in [project creation](#project-creation) 
  6. Click 'Pull Requests' and seclect 'New Pull Request' button
### Cloning and Implementing Locally
* To clone the website please use the following steps: -
  1. Navigate to the repository in [github](https://github.com/). 
  2. Choose the correct repository. In this case it is []()
  3. Click the 'Code' button
  4. You will now be given options to make a clone of the website, to download it or to open with GitHub Desktop. You can choose to clone the 'HTTPS', the 'SSH' or 'GitHub CLI' ![]()
  5. Open Git Bash or similar
  6. Navigate to your desired directory for the cloned project.
  7. Type 'git clone' followed by the URL copied in step 3.
  8. Press 'Enter' to create your local clone.

[Back to content](#table-of-contents)
## Credits
All coding content was created by Michael Greenberry, the website creator/owner.
### Content
The text and photograph content was provided by the creator
### Media
* All pages
  * All content from creator
### Icons
All icons used were sourced form [Font Awesome](https://fontawesome.com/)
### Code


#### HTML
All HTML code was written by the creator Michael Greenberry unless stated

#### CSS
All CSS code was written by the creator Michael Greenberry unless stated

#### JavaScript/JQuery
The majority of the JavaScript code was adapted from multiple websites and sources. All is therefore credited within the JavaScript code as used. 

#### Python


[Back to content](#table-of-contents)
## Acknowledgements
Many thanks to the following people for their help with this project: -

Code Institute Slack Students for their feedback and help with my questions

[Back to content](#table-of-contents)
## Author information
Michael Greenberry is the creator and owner of this website. This is a Interactive Frontend Development Milstone Project website created as part of a Full Stack Software Development in Code Institute by [Michael Greenberry](https://www.linkedin.com/in/michael-greenberry-637299108/).

[Back to content](#table-of-contents)