"""test validate_plist_xml"""

import os.path
import site
import sys

# https://stackoverflow.com/questions/34846584/whats-the-recommended-way-to-import-unittest-or-unittest2-depending-on-pyth/66616071
# try:
#    import unittest2 as unittest
# except ImportError:
#    import unittest

# add module folder to import paths
site.addsitedir(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))) , "src")
)

import validate_plist_xml  # pylint: disable=import-error,wrong-import-position

# run the script
num_errors = validate_plist_xml.validate_plist_xml.validate_plist_files()

try:
    assert num_errors == 1
except AssertionError:
    print("Error: Tests failed")
    sys.exit(num_errors)

# tests pass, return 0:
print("Success: Tests pass")
sys.exit(0)
