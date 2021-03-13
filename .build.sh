# to run: `bash .build.sh`

# delete old dist files
rm dist/*
# build
python3 -m build
# publish new version to pip
python3 -m twine upload dist/*
