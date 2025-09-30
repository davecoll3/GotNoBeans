#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "--- Installing OS Dependencies (PostgreSQL libraries) ---"

# Attempt a clean install by first manually creating a temporary directory
# that is writable, if necessary, and installing core packages.
# NOTE: In Render's environment, apt-get may need a specific location for cache.
# We will rely on the default apt-get behavior and hope it works now that 
# the build command is executed via a script.
apt-get clean
apt-get update
apt-get install -y postgresql-client libpq-dev

echo "--- Installing Python Dependencies ---"

# Install all Python packages, including the PostgreSQL driver
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

echo "--- Build Script Complete ---"