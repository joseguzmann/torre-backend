# DEVELOPMENT

## How to run the Dockerfile with bind mounts locally

```
docker run -dp 80:80 --mount type=bind,src=$(pwd),target=/app IMAGE-NAME sh -c "flask run"
```
