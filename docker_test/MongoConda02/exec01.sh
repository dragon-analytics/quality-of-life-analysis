#!/bin/bash

#mkdir temp
# Clone just the repository's .git folder (excluding files as they are already in
# `existing-dir`) into an empty temporary directory
git clone --no-checkout https://github.com/dragon-analytics/quality-of-life-analysis.git mediapy/notebooks/notebook.tmp # might want --no-hardlinks for cloning local repo

# Move the .git folder to the directory with the files.
# This makes `existing-dir` a git repo.
mv mediapy/notebooks/notebook.tmp/.git mediapy/notebooks/

# Delete the temporary directory
rmdir mediapy/notebooks/notebook.tmp

cd mediapy/notebooks

# git thinks all files are deleted, this reverts the state of the repo to HEAD.
# WARNING: any local changes to the files will be lost.
git reset --hard HEAD
 #mkdir /temp
 #git clone https://github.com/dragon-analytics/quality-of-life-analysis.git temp;
 #mv -r temp/* mediapy/notebooks/
 #rm -rf temp