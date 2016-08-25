#!/bin/bash
# Build
middleman build
# Deploy everything to S3
aws s3 sync ./build/ s3://istrumpprez.com
# Invalidate
aws cloudfront create-invalidation --distribution-id EWJT7RJQU1ZA3 --invalidation-batch file://scripts/invbatch.json
