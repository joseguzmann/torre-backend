#!/bin/sh

exec gunicorn --bin 0.0.0.0:$PORT "app:create_app()"