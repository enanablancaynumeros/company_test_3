#!/usr/bin/env bash

set -e

if [[ "$@" == *--flower* ]]; then
    flower -A workers.celery_app --port=5555
else
    celery -A workers.celery_app worker --loglevel=INFO
fi