#!/bin/bash

python manage.py dumpdata --indent=4 accounts > accounts/fixtures/initial_data.json

rm -rf init_data
cp -R media init_data
