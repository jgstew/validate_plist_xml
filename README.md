# validate_plist_xml
This python module will validate Apple XML Plist files

By default configured to check files with the following extensions: `('.recipe', '.plist', '.profile')`

By default, runs in the current working directory against all files in that directory and all subdirectories.

This module depends upon the `lxml` module. (which is handled by pip automatically)

The code is found within `src/validate_plist_xml/validate_plist_xml.py` within the [git repo](https://github.com/jgstew/validate_plist_xml/blob/main/src/validate_plist_xml/validate_plist_xml.py).

This module checks that the plist is valid XML and meets the Apple Plist DTD here: https://www.apple.com/DTDs/PropertyList-1.0.dtd


## Examples:

### Run as module:
```
$ python3 -m validate_plist_xml
XML Syntax Error in: ./tests/bad/example-bad-xml-tags.recipe
Opening and ending tag mismatch: BAD_TAG line 4 and dict, line 15, column 8 (example-bad-xml-tags.recipe, line 15)
Failed DTD Validation: ./tests/bad/example-bad-dtd.recipe
Element dict content does not follow the DTD, expecting (key , (array | data | date | dict | real | integer | string | true | false))*, got (key astring key string key dict key string key array ), line 4
2 errors found in 3 plist xml files
```

### Run as Python Script:
```
$ python3 src/validate_plist_xml/validate_plist_xml.py 
XML Syntax Error in: ./tests/bad/example-bad-xml-tags.recipe
Opening and ending tag mismatch: BAD_TAG line 4 and dict, line 15, column 8 (example-bad-xml-tags.recipe, line 15)
Failed DTD Validation: ./tests/bad/example-bad-dtd.recipe
Element dict content does not follow the DTD, expecting (key , (array | data | date | dict | real | integer | string | true | false))*, got (key astring key string key dict key string key array ), line 4
2 errors found in 3 plist xml files
```

### Use as GitHub Action:

- https://github.com/jgstew/jgstew-recipes/blob/main/.github/workflows/plistlint.yaml

```
---
name: plistlint

on:
  push:
    paths:
      - "**.plist"
      - "**.recipe"
      - ".github/workflows/plistlint.yaml"
  pull_request:
    paths:
      - "**.plist"
      - "**.recipe"
      - ".github/workflows/plistlint.yaml"

jobs:
  plistlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install validate-plist-xml
        run: pip install validate-plist-xml

      - name: Lint Plist files
        run: python3 -m validate_plist_xml
```
