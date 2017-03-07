#!/usr/bin/env bash

set -e

bash wait-for-it.sh --timeout=10 ${DB_ADDRESS}:5432

python3.5 /src/api/api/manage.py db_create_all
uwsgi --socket 0.0.0.0:8000 --protocol=http -w api.wsgi:app --processes 2