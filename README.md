# RTR V5

## Table of Contents

## Description

Welcome to rtr_v5, This is a reddit-style newspage where users are supposed to be able to share whatever thoughts ideas or news they want

## Technologies Used

### Languages, frameworks and libraries

* Python
* HTML
* CSS
* Javascript

* SQL database: ElephantSQL
* Jquery
* Bootstrap

### Planning Tools

* Data modeling - DBSchema
* Kanban: Github

### Installed dependencies (requirements.txt)

* asgiref==3.7.2
* cloudinary==1.33.0
* coverage==7.2.7
* dj-database-url==2.0.0
* dj3-cloudinary-storage==0.0.6
* Django==3.2.19
* django-allauth==0.41.0
* django-nose==1.4.7
* django-summernote==0.8.20.0
* gunicorn==20.1.0
* iniconfig==2.0.0
* nose==1.3.7
* oauthlib==3.2.2
* pluggy==1.2.0
* psycopg2==2.9.6
* pytest==7.4.0
* python3-openid==3.2.0
* pytz==2023.3
* requests-oauthlib==1.3.1
* sqlparse==0.4.4
* urllib3==1.26.16

## Planning

Decided for 3*1 week sprints, with some keywords in mind for each sprint  
This plan was made for rtr_v3 originally, so the dates are not exactly matching for this final version.  
Last day of each sprint, i took some time to re-assess next phase based on progress during the previous one, without any major changes.

### Sprint Planning

See [Kanban Board](https://github.com/users/Enquil/projects/6/views/1 "Kanban Board") for a more detailed view of issues/tasks, it should be public
Including image because i thought it was public the last time as well, it was not.

#### Sprint 1, 12/6-19/6

    * Model setup, Category, Post and Comment
    * Log In/Sign Up functionality
    * Basic READ functionality for users and visitors (posts)
    * Basic Admin setup with CRUD (It's built in to django)
    * Layout and structural front-end design

In sprint 1, i focus mostly on very basic features for users specifically, like:  
    * Setting Up the home view in the form of a postlist-view with sort-functionality by category

General implementations:

* Installing relevant libraries and applications (see requirements.txt for full list)
* Structural front-end/layout (No color or decorating)
* Setting Up admin view to insert model instances for reference when developing the site
* Tests

#### Sprint 2, 19/6-26/6

    * Model Setup, UserProfile
    * CREATE functionality for users, (posts and comments)
    * Picking a color-scheme
    * Extended admin control (manipulating querysets from the admin-panel in various ways)
    * Tests

#### Sprint 3, 26/6-3/7

    * Update and Delete Functionality for users
    * Style templates
    * Tests

### Omitted functionality (Scope)

Due to time-constraints, i chose to omit the following functionality that was originally planned:
  
* Comment reply system
* News-api, have not recieved a reply about extra requests still
* Removed cloudinary image fields for posts, this is due to switching to function views and i did not have time to learn the differences in how forms are handled

## Models used and Schema

https://dbdiagram.io/d/649b270a02bd1c4a5e274ea3
![Data Models](./images/models/model_schema.png)

Standard Django User Model @ https://docs.djangoproject.com/en/4.2/ref/contrib/auth/

I consider all models to be sourced in some way from CodeInstitute, albeit modified to suit my needs.
Exception is the category model.

## Design

Same as with earlier versions, very simple and in your face about what the user can do

### Visual Structure

My only rule for the structure was very simple, everything should be accessible from the navbar and easily understandable.  
The exception are posts and comments which can be found in the actual userprofile.

### Color Scheme

* #e4ebf1, alice blue
  * background
  
* #bde0ff, a darker shade of alice-blue
  * dropdown-items:hover highlighting
  * Posts and Comments 'buttons' in user-profile
  
* #c9bfc0, a reddish version of ghost
  * Navbar
  * Footer
  
* #82d682, light-green
  * Sign Up button

## Testing

### Responsiveness Test

Responsiveness testing on https://responsivedesignchecker.com/
I could not log in due to csrf token issues, so any view that requires login, is tested through the built in chrome tool  

#### Home

![lg home](./images/html_and_css/responsiveness/lg_home.png)
![md home](./images/html_and_css/responsiveness/md_home.png)
![md home](./images/html_and_css/responsiveness/sm_home.png)
![sm home](./images/html_and_css/responsiveness/md_home.png)
![sm home](./images/html_and_css/responsiveness/sm_home_lower.png)

#### Post Detail

![lg post detail](./images/html_and_css/responsiveness/lg_post_detail.png)
![lg post detail 2](./images/html_and_css/responsiveness/lg_post_detail_lower.png)
![md post detail](./images/html_and_css/responsiveness/md_post_detail.png)
![md post detail 2](./images/html_and_css/responsiveness/md_post_detail_lower.png)
![sm post detail](./images/html_and_css/responsiveness/sm_post_detail.png)
![sm post detail 2](./images/html_and_css/responsiveness/sm_post_detail_lower.png)

#### Sign Up

![lg sign up](./images/html_and_css/responsiveness/lg_sign_up.png)
![md sign up](./images/html_and_css/responsiveness/md_sign_up.png)
![sm sign up](./images/html_and_css/responsiveness/sm_sign_up.png)

#### Login

![lg login](./images/html_and_css/responsiveness/lg_login.png)
![md login](./images/html_and_css/responsiveness/md_login.png)
![sm login](./images/html_and_css/responsiveness/sm_login.png)

#### Create Post

![lg create post](./images/html_and_css/responsiveness/lg_create_post.png)
![md create post](./images/html_and_css/responsiveness/md_create_post.png)
![sm create post](./images/html_and_css/responsiveness/sm_create_post.png)

#### Edit Post

![lg edit post](./images/html_and_css/responsiveness/lg_edit_post.png)
![md edit post](./images/html_and_css/responsiveness/md_edit_post.png)
![sm edit post](./images/html_and_css/responsiveness/sm_edit_post.png)

### Lighthouse Test

### JShint

I used https://jshint.com/ for JavaScript testing  
There are basically 2 functions for the whole site  
One is for putting an overlay when submitting forms, where the only thing changing is the name of the form  
The other one is for messages present in base.html  
Results For each function/view:




### pep-8

I tested all files that i've edited in some way  
Results from https://pep8ci.herokuapp.com/ by app:  

#### create_post

#### delete_actions

#### edit_post

#### home

#### post_detail

#### Profiles

### Unit testing

I used 2 different unit test libraries/modules:

* Coverage
* Django Nose

I basically just used 2 because i wanted to compare the libraries  
I did notice a slight difference in how they test for apps

#### Django Nose overall report


#### Coverage Reports

When you compare the 2, Nose and Coverage does not quite agree on what should be tested:

Coverage, part 1  
![Coverage test p1](./images/unittest/coverage_pt1.png)

Part 2  
![Coverage test p2](./images/unittest/coverage_pt2.png)

### Testing from a user perspective

#### Home View

#### Post Detail View


## Known Issues

### Form submitting multiple times (TEMPORARY FIX)

When spam-clicking a form submit button (comment-form specifically), the form submits multiple times, like so:
![multi submit bug](./images/manual_view_testing/test_admin_actions/confirm_comments_approved.png)

Temporary Fix: Added a js function to prevent default and put an overlay on top of the page until form is handled.  
This should be switched to a function that disables the button instead, or even straight python could possibly work.
Code snippet (form is replaced by id for relevant form):  

### Edit Post Form

Not rendering as expected, should be wider, keeping as is for now, because it works and is not critical

## Future Implementations

I chose to sort them by some urgency measure  

* Comment Reply System HIGH
* Post Images, HIGH
* Edit comment view, LOW/MEDIUM  
i think twitter might've gotten this one right actually
* News API, LOW/MEDIUM
* Financial API, MEDIUM
* User Settings, HIGH
  * Change email, password etc.
