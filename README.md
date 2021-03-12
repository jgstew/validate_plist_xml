# validate_plist_xml
This python module will validate Apple XML Plist files

By default configured to check files with the following extensions: `('.recipe', '.plist', '.profile')`

## Example:

```
$ python3 validate_plist_xml
XML Syntax Error in: ./test/bad/example-bad-xml-tags.recipe
Opening and ending tag mismatch: BAD_TAG line 4 and dict, line 15, column 8 (example-bad-xml-tags.recipe, line 15)
Failed DTD Validation: ./test/bad/example-bad-dtd.recipe
Element dict content does not follow the DTD, expecting (key , (array | data | date | dict | real | integer | string | true | false))*, got (key astring key string key dict key string key array ), line 4
2 errors found in 3 plist xml files
```
