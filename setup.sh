#!/bin/bash
echo "Enter project name:"
read project
cp -r $(dirname "$0") ~/Projects/$project
cd ~/Projects/$project
rm -rf .git
git init
git add .
git commit -m "Initial commit"
echo "Project '$project' created and ready!"
