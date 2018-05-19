
# Using docker images from Jupyter Development Team's jupyter/datascience-notebook
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Ubuntu 16.04 (xenial) from 2018-02-28
# https://github.com/docker-library/official-images/commit/8728671fdca3dfc029be4ab838ab5315aa125181
FROM jupyter/datascience-notebook

# Checking for SUDO:
# docker run -it -p 8888:8888 -e GRANT_SUDO="yes" --user root jupyter/datascience-notebook

# Installing Mongodb from instructions:

## https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

## (For Ubuntu 16.04) https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#create-a-list-file-for-mongodb
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

## https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#reload-local-package-database
sudo apt-get update

## https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-the-mongodb-packages
sudo apt-get install -y mongodb-org