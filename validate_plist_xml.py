#!/usr/local/python
"""
- https://stackoverflow.com/questions/15798/how-do-i-validate-xml-against-a-dtd-file-in-python
"""

import io
import os
import sys

import lxml.etree

# https://docs.python.org/3/library/io.html
# https://www.apple.com/DTDs/PropertyList-1.0.dtd
DTD_PLIST = lxml.etree.DTD(io.StringIO(
    """<!ENTITY % plistObject "(array | data | date | dict | real | integer | string | true | false )" >
<!ELEMENT plist %plistObject;>
<!ATTLIST plist version CDATA "1.0" >

<!-- Collections -->
<!ELEMENT array (%plistObject;)*>
<!ELEMENT dict (key, %plistObject;)*>
<!ELEMENT key (#PCDATA)>

<!--- Primitive types -->
<!ELEMENT string (#PCDATA)>
<!ELEMENT data (#PCDATA)> <!-- Contents interpreted as Base-64 encoded -->
<!ELEMENT date (#PCDATA)> <!-- Contents should conform to a subset of ISO 8601 (in particular, YYYY '-' MM '-' DD 'T' HH ':' MM ':' SS 'Z'.  Smaller units may be omitted with a loss of precision) -->

<!-- Numerical primitives -->
<!ELEMENT true EMPTY>  <!-- Boolean constant true -->
<!ELEMENT false EMPTY> <!-- Boolean constant false -->
<!ELEMENT real (#PCDATA)> <!-- Contents should represent a floating point number matching ("+" | "-")? d+ ("."d*)? ("E" ("+" | "-") d+)? where d is a digit 0-9.  -->
<!ELEMENT integer (#PCDATA)> <!-- Contents should represent a (possibly signed) integer number in base 10 -->"""
))


def validate_plist_xml(file_pathname):
    """This will validate the plist XML file against the DTD"""
    # parse xml
    try:
        doc = lxml.etree.parse(file_pathname)
        #print('XML well formed, syntax ok.')

    # check for file IO error
    except IOError:
        print('Invalid File: %s' % file_pathname)
        return False

    # check for XML syntax errors
    except lxml.etree.XMLSyntaxError:
        print('XML Syntax Error in: %s' % file_pathname)
        return False

    # check if xml is valid to DTD spec
    is_valid = DTD_PLIST.validate(doc)

    if not is_valid:
        print('Failed DTD Validation: %s' % file_pathname)
        return False

    return is_valid


def main(folder_path=".", file_extensions=('.recipe', '.plist', '.profile')):
    """Run this function by default"""
    # https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

    count_errors = 0
    count_files = 0

    for root, dirs, files in os.walk(folder_path):  # pylint: disable=unused-variable
        for file in files:
            # do not scan within .git folder
            if not root.startswith(('.git', './.git')):
                # process all files ending with `file_extensions`
                if file.lower().endswith(file_extensions):
                    count_files = count_files + 1
                    file_path = os.path.join(root, file)
                    result = validate_plist_xml(file_path)
                    if not result:
                        count_errors = count_errors + 1

    print("%d errors found in %d plist xml files" % (count_errors, count_files))
    sys.exit(count_errors)


if __name__ == '__main__':
    main()
