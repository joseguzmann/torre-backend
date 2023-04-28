# Torre Backend

This is my back-end application that serves as a CORS Proxy between my front-end application and Torre API

## Project info

This app is hosted on Render on the following link:

LINK

Available endpoints:

GET LINK - Retrieves user information based on the provided user ID
GET LINK - Retrieve details of a user regarding a specific skill
GET LINK - Search users based on skill and proficiency

The project is hosted on Render using a Docker container

You could get more information about endpoints through Swagger documentation:

LINK

## DEVELOPMENT

To run Docker image locally with bind mounts execute the following command:

```
docker run -dp 80:80 --mount type=bind,src=$(pwd),target=/app IMAGE-NAME sh -c "flask run"
```
