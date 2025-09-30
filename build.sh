#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# 1. Install System Dependencies (libpq-dev for PostgreSQL driver)
apt-get clean
apt-get update
apt-get install -y postgresql-client libpq-dev

# 2. Install Python Dependencies
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu