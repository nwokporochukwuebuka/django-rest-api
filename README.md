# The Django RESTAPI 
This project seeks to explain concepts about creation of APIs, using complex queries to optimize the time for our djaango project and reduce the SQL calls.

> PS: In this project, we used the PostgreSQL database

## Authentication For Users

### Registering a User
In this project for the user to create an account, the user need to provide the email, password (and name which is optional) as opposed to the default way of creating users in using the django admin. 

Also it allows us to create a superuser using this endpoint `http://127.0.0.1:8000/gateway/register` and selecting the following variables `is_active`, `is_staff` and `is_superuser`

### Logging In 
To log a user in use the endpoint `http://127.0.0.1:8000/gateway/login`. This will lolog the user in ans ong as the correct email and password is supplied (and name which is optional).

Once the user logs in, two tokens are generated automatically, viz `access` token and the `refresh` token this tokens grants authorization for that user 

> Note
> After 5 minutes the access token will expire, hence the refresh token is supplied at this endpoint `http://127.0.0.1:8000/gateway/refresh` to regenerate a new `access` and `refresh` token 

## Authorization 
For a user to access the endpoint `http://127.0.0.1:8000/gateway/secure` using Postman to get a secured message, the user must send an authorized message from Postman using the `access` token as the bearer token. In our case here the secured the message is an ZeroDivisionError message

## Updating the User Profile
This involves uploading of pictures to properly identify the users. This can be done using the endpoint `http://127.0.0.1/user-main/user-profile`. This will push the imageb to a cloud storage known as CLOUDINARY. The setup can be seen in the sertings file.

## Creating an Event
We created an API that allows a user to create an even that will allow the user set the following variable such as 
    *   `address`: The address of the event
    *   `city`
    *   `country`
    *   `state`
    *   `author_id`
    *   `title`
    *   `description`
    *   `date`
    *   `time`
    *   `max_seat`
    *   `features` which has a dictionary attribute `feature_name`

> PS: This can only be done with the Postman and not the default Django REST Framework page

In creating this, if the previous instance of an address exist for a user it will be deleted and the newly inputted address will override the initial one. This was possible because we overrode the create method 