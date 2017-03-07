#!/usr/bin/env bash

set -e

bash wait-for-it.sh --timeout=10 ${DB_ADDRESS}:5432

behave tests/features --capture --summary