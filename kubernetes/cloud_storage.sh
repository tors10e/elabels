#!/usr/bin/env bash
gsutil mb gs://vessel-energy # To make bucket, only do this first time.
gsutil rsync -R /tmp/veat/static/ gs://vessel-energy/static # Pull from where your static files are.
# Set default access to all users.
gsutil defacl ch -u AllUsers:R gs://vessel-energy
# Set access to existing items in the bucket.
gsutil acl ch -u AllUsers:R gs://vessel-energy/static/**
gsutil cors set cors.json gs://vessel-energy