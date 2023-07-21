# RTR V5

## Table of Contents

## Description
Welcome to rtr_v5, This is a reddit-style newspage where users are supposed to be able to share whatever thoughts ideas or news they want

## Technologies Used

Data modeling - DBSchema

## Planning

Decided for 3*1 week sprints, with some keywords in mind for each sprint  
This plan was made for rtr_v3 originally, so the dates are not exactly matching for this final version.  
Last day of each sprint, i took some time to re-assess next phase based on progress during the previous one, without any major changes.

### Sprint Planning

See [Kanban Board](https://github.com/users/Enquil/projects/6/views/1 "Kanban Board") for a more detailed view of issues/tasks, it's set to public

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

### Omitted functionality

Due to time-constraints, i chose to omit the following functionality that was originally planned:
  
* Comment reply system
* News-api, have not recieved a reply about extra requests still
* Removed cloudinary image fields for posts, this is due to switching to function views and i did not have time to learn the differences in how forms are handled

## Models

### Model used and Schema

https://dbdiagram.io/d/649b270a02bd1c4a5e274ea3
![Data Models](./images/model_schema.png)

Standard Django User Model @ https://docs.djangoproject.com/en/4.2/ref/contrib/auth/

I consider all models to be sourced somewhat from CodeInstitute

## Design

## Testing

### Unit testing

I used 2 different unit test libraries/modules:

* Coverage
* Django Nose

This was because coverage says it wants me to test the test.py files as well,  
I realize i might make a mistake here because i didnt test them,  
but all topics i can find about it says that is not something you should/need to do.  
Also, i wouldnt have a clue where to begin.  
Find results below ->

#### Django Nose overall report

![Nose Overall](./images/unittest/django_nose_overall.png)  
Main project report:

![Nose Main Project Test](./images/unittest/main_project_test.png)

#### Django Nose detailed report

However, running coverage in tandem with django nose produces the following 'detailed' overall result:  
  
![coverage/nose error](./images/unittest/django_nose_coverage_error.png)

Did some research about this, and it turns out that coverage and django nose always have been incompatible, there are some ways to 'solve' this, but they are all described as very hacky.

#### Coverage Reports

When you compare the 2, Nose and Coverage does not quite agree on what should be tested:

![Coverage test p1](./images/unittest/coverage_test_p1.png)
![Coverage test p2](./images/unittest/coverage_test_p2.png)

#### Testing as a user

I started from the homepage and went from there, i took a screenshot on each page to document the navigation process etc.  
On each page, i also refreshed with shift + f5 to make sure there was no issues with cache for example.  

Inital Setup:  

Set Up categories  
![Manual test categories](./images/manual_view_testing/categories_manual_testing.png)  

Set up 2 users, admin is superuser  
![Manual test users](./images/manual_view_testing/users_manual_testing.png)

Set up a couple of posts in different categories  
![Manual test posts](./images/manual_view_testing/posts_manual_testing.png)

Homepage when not logged in:
![Homepage](./images/manual_view_testing/homepage_and_filtering/homepage_not_logged_in.png)

Pagination:
![Pagination](./images/manual_view_testing/homepage_and_filtering/test_pagination.png)

Back to homepage:
![Homepage](./images/manual_view_testing/homepage_and_filtering/homepage_not_logged_in.png)

Now to filter 2 separate categories for good measure:
![business_filter](./images/manual_view_testing/homepage_and_filtering/test_filter_business.png)
![opinions_filter](./images/manual_view_testing/homepage_and_filtering/test_filter_opinions.png)

Now, let's try creating a post when not logged in:
(Note the URL)
![create post while not logged in](./images/manual_view_testing/redirection_when_not_logged_in/test_create_post_not_logged_in.png)

Okay, let's check out the post_detail_view, also added a comment to test:
![create post while not logged in](./images/manual_view_testing/post_detail_tests/test_post_detail_not_logged_in.png)

Comment did not post, but something is wrong:
![create post while not logged in](./images/manual_view_testing/post_detail_tests/uh_oh.png)

## Known Issues

## Future Implementation
