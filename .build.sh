#!/usr/bin/env bash

# to run: `bash .build.sh`
echo "-- run build and publish to public pypi.org pip --"

# delete old dist files
echo "-- deleting old dist files --"
rm dist/*

# build
echo "-- run build --"
python3 -m build

# publish new version to pip - requires configured creds
echo "-- publishing --"
python3 -m twine upload dist/*

echo "-- finished --"
