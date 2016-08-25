#!/bin/bash

# Build
echo "--- Building Website"
middleman build
if [ $? -ne 0 ]
then
  echo "^^^ +++"
  exit 1
fi

# Deploy everything to S3
echo "--- Deploying Website"
s3_website push
if [ $? -ne 0 ]
then
  echo "^^^ +++"
  exit 1
fi
