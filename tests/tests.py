"""test validate_plist_xml"""

import argparse
import os.path
#import site
import sys

# check for --test_pip arg
parser = argparse.ArgumentParser()
parser.add_argument("--test_pip", help="to test package installed with pip",
                    action="store_true")
args = parser.parse_args()

if not args.test_pip:
    # add module folder to import paths for testing local src
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
    )
    # reverse the order so we make sure to get the local src module, not pip package
    sys.path.reverse()

import validate_plist_xml  # pylint: disable=import-error,wrong-import-position

# run the script
num_errors = validate_plist_xml.validate_plist_xml.validate_plist_files()

try:
    assert num_errors == 2
except AssertionError:
    print("Error: Tests failed")
    sys.exit(num_errors)

# tests pass, return 0:
print("Success: Tests pass")
sys.exit(0)
