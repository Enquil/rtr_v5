# RTR V5

## Table of Contents

1. [Description](#description)
2. [Technologies Used](#technologies-used)
3. [Planning](#planning)
4. [Models and Schema](#models-used-and-schema)
5. [Design](#design)
6. [Testing](#testing)
7. [Known Issues](#known-issues)
8. [Future implementations](#future-implementations)

## Description

Welcome to rtr_v5, This is a reddit-style newspage where users are supposed to be able to share whatever thoughts ideas or news they want.  

### Observe

All posts are made by chatGPT  

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
  
* Comment reply system (currently only post author can reply to comments)
* News-api, have not recieved a reply about extra requests still
* Removed cloudinary image fields for posts, this is due to switching to function views and i did not have time to learn the differences in how forms are tested

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

### Responsiveness

Responsiveness testing on https://responsivedesignchecker.com/
Below is the home view tested in small, medium and large screen sizes  
See the folder images/responsiveness in repo for full details and images  



### Lighthouse Test

### JShint

I used https://jshint.com/ for JavaScript testing  
There are basically 2 functions for the whole site  
One is for putting an overlay when submitting forms, where the only thing changing is the name of the form  
The other one is for messages present in base.html  
Results For each function/view:

#### create_post js

![create_post jshint](./images/jshint/create_post_js.png)

#### edit_post js

![edit_post jshint](./images/jshint/edit_post_js.png)

#### post_detail_js

![post_detail jshint](./images/jshint/post_detail_js.png)

#### profiles_js

![profiles jshint](./images/jshint/profiles_js.png)

#### messages_js

![profiles jshint](./images/jshint/messages_js.png)

### pep-8

I tested all files that i've edited in some way  
Results from https://pep8ci.herokuapp.com/ by app:  

#### create_post

forms.py  
![create post pep8 forms](./images/pep8ci/create_post/create_post_forms.png)
test_forms.py  
![create post pep 8 test forms](./images/pep8ci/create_post/create_post_test_forms.png)
test_views.py  
![create post pep 8 test views](./images/pep8ci/create_post/create_post_test_views.png)
urls.py  
![create post pep 8 urls](./images/pep8ci/create_post/create_post_urls.png)
views.py  
![create post pep 8 views](./images/pep8ci/create_post/create_post_views.png)

#### delete_actions

test_views.py  
![delete actions pep 8 test views](./images/pep8ci/delete_actions/delete_actions_test_views.png)
urls.py  
![delete actions pep 8 urls](./images/pep8ci/delete_actions/delete_actions_urls.png)
views.py  
![delete actions pep 8 views](./images/pep8ci/delete_actions/delete_actions_views.png)

#### edit_post

test_views.py  
![edit post pep 8 test views](./images/pep8ci/edit_post/edit_post_test_views.png)
urls.py  
![edit post pep 8 urls](./images/pep8ci/edit_post/edit_post_urls.png)
views.py  
![edit post pep 8 views](./images/pep8ci/edit_post/edit_post_views.png)

#### home

admin.py  
![home pep 8 admin](./images/pep8ci/edit_post/edit_post_test_views.png)
context_processors.py  
![home pep 8 context processors](./images/pep8ci/home/home_context_processors.png)
models.py  
![home pep 8 models](./images/pep8ci/home/home_models.png)
test_admin.py  
![home pep 8 test_admin](./images/pep8ci/home/home_test_admin.png)
test_models.py  
![home pep 8 test_admin](./images/pep8ci/home/home_test_models.png)
test_views.py  
![home pep 8 test views](./images/pep8ci/edit_post/edit_post_test_views.png)
urls.py  
![home pep 8 urls](./images/pep8ci/edit_post/edit_post_urls.png)
views.py  
![home pep 8 views](./images/pep8ci/edit_post/edit_post_views.png)

#### main_project (rtr_v5)

settings.py  
![rtr_v5 pep 8 settings](./images/pep8ci/main_project/main_project_settings.png)

#### post_detail

forms.py  
![post detail pep8 forms](./images/pep8ci/post_detail/post_detail_forms.png)
test_forms.py  
![post detail pep 8 test forms](./images/pep8ci/post_detail/post_detail_test_forms.png)
test_models.py  
![post detail pep 8 test models](./images/pep8ci/post_detail/post_detail_test_models.png)
test_views.py  
![post detail pep 8 test views](./images/pep8ci/post_detail/post_detail_test_views.png)
urls.py  
![post detail pep 8 urls](./images/pep8ci/post_detail/post_detail_urls.png)
views.py  
![post detail pep 8 views](./images/pep8ci/post_detail/post_detail_views.png)

#### profiles

admin.py  
![admin pep 8 admin](./images/pep8ci/profiles/profiles_admin.png)
models.py  
![admin pep 8 models](./images/pep8ci/profiles/profiles_models.png)
test_models.py  
![admin pep 8 test models](./images/pep8ci/profiles/profiles_test_models.png)
urls.py  
![admin pep 8 urls](./images/pep8ci/profiles/profiles_urls.png)
views.py  
![admin pep 8 views](./images/pep8ci/profiles/profiles_views.png.png)

### Unit testing

I used 2 different unit test libraries/modules:

* Coverage
* Django Nose

I basically just used 2 because i wanted to compare the libraries  
I did notice a slight difference in how they test for apps

#### Django Nose report

Nose, part 1  
![Django Nose test p1](./images/unittest/django_nose_pt1.png)

Part 2  
![Django Nose test p2](./images/unittest/django_nose_pt2.png)

#### Coverage Reports

Coverage, part 1  
![Coverage test p1](./images/unittest/coverage_pt1.png)

Part 2  
![Coverage test p2](./images/unittest/coverage_pt2.png)

### Testing from a user perspective

First, let's visit the deployed site:
![home anon user 1](./images/user_exp_tests/home_anon_user_1.png)

Nice, and there's a footer as well
![home anon user 2](./images/user_exp_tests/home_anon_user_2.png)

Lets click 'next page and see what happens'
![pagination 1](./images/user_exp_tests/pagination_before.png)

Great, takes us to the next page as expected
![pagination 2](./images/user_exp_tests/pagination_before.png)

Im more interested in specific topic, art and entertainment to be more precise
![category 1](./images/user_exp_tests/category_test_before.png)

Great, only 2 posts in here but i can read something at least
![category 2](./images/user_exp_tests/category_test_after.png)

Lets click the home button and see what happens
![home button](./images/user_exp_tests/home_button.png)

Okay it takes us home, makes sense!
Now, lets click a post:
![post_detail anon](./images/user_exp_tests/sign_up_navigation.png)

Okay now i can read the whole thing, but nothing happens when i click the like button.  
Is it broken? Let's let the site owner know by leaving a comment  
![comment anon](./images/user_exp_tests/comment_anon_user.png)

Oh okay, seems you cant leave comments without being an account holder
Lets click the sign up button (or in this case, the blue sign up link)
![comment anon](./images/user_exp_tests/comment_login_redirect.png)

Fill in the form and click, sign up  
(Email is technically not required, but it helps a lot if you would want to enable it later)
![signup page](./images/user_exp_tests/sign_up.png)

Great! We can create users, notice there is an option for us to create posts in the navbar as well as a dropdown with our username  
![signup success](./images/user_exp_tests/sign_up_success.png)

But first, lets go back to the post and leave a comment
![comment logged in](./images/user_exp_tests/comment_logged_in.png)

It works! Lets try clicking the like-button as well  
And it works!  
![like logged in](./images/user_exp_tests/like_logged_in.png)

Now lets go and create a post of our own, click the 'create post' button in the navbar  
![create post1](./images/user_exp_tests/create_post1.png)

And fill in the form, excerpt can be left blank, but it's nice to give a preview  
![create post2](./images/user_exp_tests/create_post2.png)

And we have a successful post, and somebody already left us a comment!  
There's a weird button there now, that wasnt present on our own comment that we left  
Lets click it
![create post success](./images/user_exp_tests/create_post_success.png)

Okay, seems we can leave replies to users who comment on our posts,  
That button structure is bad, let's add that to issues for now since it's not breaking anything  
![comment reply modal](./images/user_exp_tests/comment_reply_modal.png)

And we've left a response, now let's see what that navbar item with our username does  
Seems we have the options to visit our profile, or log out, we're gonna visit the profile  
![reply success](./images/user_exp_tests/reply_success.png)

Alright, looks like we have the option to view some of our previous actions by clicking the related 'button'  
![profile1](./images/user_exp_tests/profile1.png)

Alright, it shows our post as well as some actions we can take to modify it, lets try and edit it
![profile posts](./images/user_exp_tests/profile_posts.png)

Okay, the form looks a bit wonky, but at least it's obvious what to do
Notice the use of 2 html linebreaks, the standard textfield supports a limited use of html elements  
![edit post](./images/user_exp_tests/edit_post.png)

Now let's find our post, note that we cant actually access the post from the profile  
This should be fixed, so lets add that to known issues
Let's find the post and leave a comment, adn then back toour profile
![edit post sucess](./images/user_exp_tests/edit_post_success.png)

Seems we cant edit any comments, but we can delete them in case we made some error, or spoke too soon etc.  
Lets delete the comment we just left on our post  
![profile comments](./images/user_exp_tests/profile_comments.png)

And it seems to work! Let's also visit the post just to make sure  
![delete comment success](./images/user_exp_tests/delete_comment_success.png)

And it's gone, now lets see what the 'likes' button does  
![profile likes](./images/user_exp_tests/confirm_comment_delete.png)

It shows a list of the posts that we've liked, and we have the option to visit the post
![profile likes post detail](./images/user_exp_tests/profile_likes.png)

And here we are, now lets log out and make sure that works properly  
![logout 1](./images/user_exp_tests/logout1.png)

So we get taken to the logout screen  
![logout confirm](./images/user_exp_tests/logout_confirm.png)

And we have a successful log out  
![logout success](./images/user_exp_tests/logout_success.png)

### Anonymous and Malicious User Tests

This section is mean to test safeguards when a user tries to take an action or access something they shouldnt be able to  

#### Tests undertaken and expected outcome in order of tests

* Accessing profiles as anonymous user, redirect to login
* Creating a post as anonymous user, redirect to login
* Editing a post as anonymous user, redirect to login
* Editing a post as wrong user, 403 forbidden
* Deleting a post as anonymous user, redirect to login
* Deleting a post as wrong user, 403 forbidden
* Deleting a comment as anonymous user, redirect to login
* Deleting a comment as wrong user, 403 forbidden

Tests were done towards objects created by test_user3, and the malicious user was admin

Results:  

Create Post as anonymous user, cannot produce a 403 since all users can access it  
![create post anon user](./images/malicious_user_tests/create_post_not_logged_in.png)
Redirects as expected  
![create post redirect](./images/malicious_user_tests/create_post_redirect.png)
And we get a successful login  
![create post anon user](./images/malicious_user_tests/create_post_redirect_success.png)

Edit post as anonymous user  
![edit post anon user](./images/malicious_user_tests/edit_post_not_logged_in.png)
Redirects as expected  
![edit post redirect](./images/malicious_user_tests/edit_post_redirect.png)
And a 403 is presented  
![edit post forbidden](./images/malicious_user_tests/edit_post_wrong_user_403.png)

Delete post as anonymous user  
![delete post anon user](./images/malicious_user_tests/delete_post_not_logged_in.png)
Redirect  
![delete post redirect](./images/malicious_user_tests/delete_post_redirect.png)
Forbidden 403  
![delete post forbidden](./images/malicious_user_tests/delete_post_wrong_user_403.png)

Delete comment as anonymous user  
![delete comment anon user](./images/malicious_user_tests/delete_comment_not_logged_in.png)
Delete comment redirect  
![delete comment redirect](./images/malicious_user_tests/delete_comment_redirect.png)
Forbidden 403  
![delete comment forbidden](./images/malicious_user_tests/delete_post_wrong_user_403.png)

## Known Issues

### Settings, ALLOWED_HOSTS

Cannot use 'localhost' or the heroku general app-name as allowed hosts, the urls must be specific or django returns an error.  
I need to confirm it's not a chrome problem since it seems to be a problem across all apps i currently have deployed.  

### README, general improvements

While the file content is readable just fine and covers the site, it could do with better navigation at the very least  

### "Remember me" on forms

The checkbox that lets django remember users seems to not work.  
I thought this was out-of-the-box function but it seems you need to enable it.  
medium-high priority since it does hamper user experience a little bit, if not in a major way.

### Form submitting multiple times (HOTFIX, REPLACE ASAP)

When spam-clicking a form submit button (comment-form specifically), the form submits multiple times  

Temporary Fix: Added a js function to prevent default and put an overlay on top of the page until form is handled.  
This should be switched to a function that disables the button instead, or even straight python could possibly work.
form is replaced by id for relevant form on the corresponding page.  
If a user really wants to bypass this, they can, so this has a really priority to be changed and tested in jest.

### Edit Post Form

Not rendering as expected, should be wider, keeping as is for now, because nothing critical is broken

### Sign-in redirect from comment, anonymous user

When commenting and not logged in, user is not redirected to the post in question  

### No message when trying to comment as anonymous user

It's kinda obvious you cant comment without logging in because of the redirect  
But there still should be a message

### Cannot access posts directly from profile

You can for the posts you've liked, but ideally you want quick access to you own posts in another way  

## Future Implementations

I chose to sort them by some urgency measure  

* Comment Reply System HIGH
* Post Images, HIGH
* Edit comment view, LOW/MEDIUM, i think twitter/X w/e might've gotten this one right actually
* News API, LOW/MEDIUM
* Financial API, MEDIUM
* User Settings, HIGH
  * Change email, password etc.
