# Torre Backend

This is my back-end application that serves as a CORS Proxy between my front-end application and Torre API

## Project info

This app is hosted on Render using a Docker container. You can access it through the following link:

https://torre-backend.onrender.com

Available endpoints:

GET https://torre-backend.onrender.com/user/{user_id} - Retrieves user information based on the provided user ID <br />
GET https://torre-backend.onrender.com/user/{user_id}/skill/{skill_id}/ - Retrieve details of a user regarding a specific skill<br />
GET https://torre-backend.onrender.com/search/users/skill/{skill_name}/proficiency/{proficiency} - Search users based on skill and proficiency<br />

You could get more information about endpoints through Swagger documentation:

https://torre-backend.onrender.com/swagger-ui

## DEVELOPMENT

To run Docker image locally with bind mounts execute the following command on Windows:

```
docker run -dp 80:80 --mount type=bind,src=$(pwd),target=/app IMAGE-NAME sh -c "flask run"
```
