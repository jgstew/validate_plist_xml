"""
To support validate_plist_xml as module
"""
import os

from .validate_plist_xml import main

def _init_get_version():
    """
    This function gets the contents of VERSION.txt
    - Get directory of this file __init__.py
    - Get `VERSION.txt` path in same directory
    - Read first line of VERSION.txt
    - Trim whitespace characters from the first line
    """
    init_dir = os.path.dirname(os.path.realpath(__file__))
    ver_file = os.path.join(init_dir, 'VERSION.txt')
    with open(ver_file) as f:
        first_line = f.readline().strip()
    return first_line

# read by `python .\setup.py --version`
# read in `setup.cfg` by `version = attr: src.validate_plist_xml.__version__`
__version__ = _init_get_version()
VERSION = __version__
