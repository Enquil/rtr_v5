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
![Data Models](./images/model_schema.png)

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

### Lighthouse Test

### JShint

At the moment, there is only one function using JavaScript in this projec, the message timeout function
![jshint test](./images/jshint/jshint_test.png)

### pep-8

I tested all files that i've edited in some way (i hope)  
Results from https://pep8ci.herokuapp.com/ by app:  

#### create_post

![create_post forms](./images/pep8ci/create_post_forms_result.png)
![create_post urls](./images/pep8ci/create_post_urls.png)
![create_post views](./images/pep8ci/create_post_views.png)

#### delete_actions

![create_post forms](./images/pep8ci/delete_actions_urls.png)
![create_post urls](./images/pep8ci/delete_actions_views.png)

#### 

### Unit testing

I used 2 different unit test libraries/modules:

* Coverage
* Django Nose

This was because coverage says it wants me to test the test.py files as well,  
I realize i might make a mistake here because i didnt test them,  
but topics i can find about it says that is not something you should not do/need to do.  
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

#### edit_post

#### home

#### post_detail

#### profiles

#### Testing from a user perspective

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
![create post while not logged in](./images/manual_view_testing/anonymous_user_testing/test_create_post_not_logged_in.png)

Okay, let's check out the post_detail_view, also added a comment to test:
![create post while not logged in](./images/manual_view_testing/post_detail_tests/test_post_detail_not_logged_in.png)

Comment did not post, but something is wrong, this should redirect to login:  
![create post while not logged in](./images/manual_view_testing/post_detail_tests/uh_oh.png)

Bad statement in post_detail.views.py, let's try again:
![retry commenting when not logged in](./images/manual_view_testing/post_detail_tests/test_retry_comment_anon_user.png)
![create post while not logged in](./images/manual_view_testing/post_detail_tests/test_fixed_anon_user.png)
Fixed, note that the redirection is not handle by djangos @login_required decorator

Now let's try and edit a post when not logged in, just change the url from post_detail to edit_post:
![edit post when anon user](./images/manual_view_testing/anonymous_user_testing/test_edit_post_anon_user.png)

Redirects as it should, let's try logging in with a user that has not created the post in question:
![edit post redirect anon user](./images/manual_view_testing/anonymous_user_testing/test_edit_post_anon_user_redirect.png)

And we get a 403 response, as expected  
![edit post wrong user](./images/manual_view_testing/edit_post_tests/test_edit_post_wrong_user.png)

Last 2 tests when Anonymous User (Not logged in), delete a comment, and delete a post:  
![delete comment anon user](./images/manual_view_testing/anonymous_user_testing/test_deleting_comment_not_logged_in.png)
![delete comment redirect](./images/manual_view_testing/anonymous_user_testing/test_delete_comment_redirect.png)

Looks ok, now let's try it with a post:
![delete post anon user](./images/manual_view_testing/anonymous_user_testing/test_delete_post_anon.png)
![delete post redirect](./images/manual_view_testing/anonymous_user_testing/test_delete_post_redirect.png)

Okay, everything redirects as it should, Now, lets create a user:
![sign up test](./images/manual_view_testing/signup_tests/test_signup.png)

And we get a good response, user is created, also notice you now have an option to create posts in the navbar and some user options
![sign up success](./images/manual_view_testing/signup_tests/test_signup_success.png)

Lets create a post straight away:
![test create post](./images/manual_view_testing/create_post_testing/test_create_post_user.png)

Okay, looks good, leave a like for successful post!
![test create post](./images/manual_view_testing/create_post_testing/test_create_post_success.png)

Let's leave a comment while we're at it
![test create post](./images/manual_view_testing/comment_test/test_comment.png)

Okay, comment is posting as it should
![test create post](./images/manual_view_testing/comment_test/test_comment_success.png)

however, pressing shift + f5 prompts me to resend the form, let's do that
![test create post](./images/manual_view_testing/comment_test/test_comment_uh_oh.png)
![test create post](./images/manual_view_testing/comment_test/test_comment_double_comment.png)

Okay, now it's posting the comment again, we dont want that, let's investigate

Replaced this statement in post_detail.views:  
![test create fix before](./images/manual_view_testing/comment_test/test_fix_double_comment_before.png)

With this:  
![test comment fix after](./images/manual_view_testing/comment_test/test_fix_double_comment_after.png)

All good, no more double comments
![test comment fixed](./images/manual_view_testing/comment_test/test_comment_fix_success.png)

Sweet, let's go to the profile, click your username and select:  
![test profile navigation](./images/manual_view_testing/profile_test/test_navigate_profile.png)

Looks, good but where are the posts and comments?
![test profile navigation success](./images/manual_view_testing/profile_test/test_navigate_profile_success.png)

Ah, just click any of the blue 'buttons'
![test profile show user created content](./images/manual_view_testing/profile_test/test_show_user_created_content.png)

Looks decent, let's remove one of those double comments, click delete and this modal should show
![test profile remove comment](./images/manual_view_testing/profile_test/test_delete_comment.png)

It's gone from the profile page at least, but is it actually GONE?
![test profile remove comment](./images/manual_view_testing/profile_test/test_delete_comment_success.png)

And let's check the post, seems it deleted as it should
![check removed comment post detail](./images/manual_view_testing/profile_test/check_comment_delete_post_detail.png)

Let's go back to the profile and edit that post, i think it needs another lorem ipsum in there somewhere, just click edit
![test profile edit post](./images/manual_view_testing/profile_test/test_edit_post_edit_button.png)

Okay, we got in to the view at least
![test edit post view](./images/manual_view_testing/edit_post_tests/test_edit_post_view.png)

Nice, looks like it updated, let's go check it ACTUALLY DID
![test profile post edited](./images/manual_view_testing/profile_test/test_edit_post_profile_updated.png)

Lovely jovely, now, let's go delete the post
![test profile post edited post detail](./images/manual_view_testing/edit_post_tests/test_edit_post_post_detail.png)

Modal shows at least, fingers crossed this works
![test profile delete post](./images/manual_view_testing/profile_test/test_delete_post_modal.png)

Okay, post and post.comments are gone from the profile, managed to capture the message this time as well!
![test profile delete post success](./images/manual_view_testing/test_delete_post/test_delete_post_success.png)

Let's check for the models in the admin just to make sure they're actually gone
![test profile delete post success](./images/manual_view_testing/test_delete_post/test_delete_post_admin_view.png)
![test profile delete post success](./images/manual_view_testing/test_delete_post/test_delete_post_comments_admin_view.png)

Looks like they're gone, speaking of which, let's try the admin actions i created  
First, lets disable all posts
![test admin disable posts](./images/manual_view_testing/test_admin_actions/test_delete_post_comments_admin_view.png)

Well, they're disabled, but did it work?
![test admin posts disabled](./images/manual_view_testing/test_admin_actions/test_delete_post_comments_admin_view.png)

Looks like!  
![confirm posts disabled](./images/manual_view_testing/test_admin_actions/confirm_posts_disabled.png)

Alright, re-publish those posts and disable the comments for the post: testing new category instead  
![publish posts](./images/manual_view_testing/test_admin_actions/posts_published.png)
![publish posts](./images/manual_view_testing/test_admin_actions/test_disable_comments.png)

Okay, the boolean changes at least
![publish posts](./images/manual_view_testing/test_admin_actions/comments_disabled.png)
And the comments are gone, nice!
![publish posts](./images/manual_view_testing/test_admin_actions/confirm_comments_disabled.png)

And back again:
![publish posts](./images/manual_view_testing/test_admin_actions/approve_comments.png)
![publish posts](./images/manual_view_testing/test_admin_actions/comments_approved.png)
![publish posts](./images/manual_view_testing/test_admin_actions/confirm_comments_approved.png)

That concludes the manual testing of the current functions on the site, and should give you an idea of flow-control

## Known Issues

* FORMS
When spam-clicking a form submit button, the 

## Future Implementations

* Comment Reply System HIGH
* Edit comment view, MAYBE
* News API, HIGH
* Financial API, HIGH
* User Settings HIGH
  * Change email, password etc.
