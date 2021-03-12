# validate_plist_xml
This python module will validate Apple XML Plist files

By default configured to check files with the following extensions: `('.recipe', '.plist', '.profile')`

## Example:

```
$ python3 validate_plist_xml.py 
XML Syntax Error in: ./test/bad/example-bad-xml-tags.recipe
Failed DTD Validation: ./test/bad/example-bad-dtd.recipe
2 errors found in 3 plist xml files
```
