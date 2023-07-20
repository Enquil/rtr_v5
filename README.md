# RTR V5

## Table of Contents

## Description


## Technologies Used

Data modeling - DBSchema

## Planning

Decided for 3*1 week sprints, with some keywords in mind for each sprint  
This plan was made for rtr_v3 originally, so the dates are not exactly matching for this final version.  
Last day of each sprint, i took some time to re-assess next phase based on progress during the previous one, without any major changes.

### Sprint Planning

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
    * Delete Functionality for users
    * Style templates
    * Tests

### Omitted functionality
Due to time-constraints, i chose to omit the following functionality that was originally planned:
  
* Comment reply system
* News-api, have not recieved a reply about extra requests still
* 

## Models

### Model used and Schema

https://dbdiagram.io/d/649b270a02bd1c4a5e274ea3
![Data Models](./images/model_schema.png)

### User

Standard Django User Model @ https://docs.djangoproject.com/en/4.2/ref/contrib/auth/

### Post

### Comment

### UserProfile

## Design

## Known Issues

## Future Implementation
