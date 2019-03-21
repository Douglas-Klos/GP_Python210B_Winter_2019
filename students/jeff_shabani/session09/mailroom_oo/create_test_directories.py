#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# create_test_directories.py

import os
import platform
from pathlib import Path

# current working directory
base_path = Path.cwd()

# check system type & set path to letter testing folders
def set_test_path_one():
    if platform.system() == 'Windows':
        new_dir = f'{base_path}\letter_tests'
    else:
        new_dir = f'{base_path}/letter_tests'
    return new_dir

def set_test_path_two():
    if platform.system() == 'Windows':
        new_dir2 = f'{base_path}\letter_tests2'
    else:
        new_dir2 = f'{base_path}/letter_tests2'
    return new_dir2


#create letter test folders
if os.path.exists(set_test_path_one()):
    pass
else:
    os.makedirs(set_test_path_one())

if os.path.exists(set_test_path_two()):
    pass
else:
    os.makedirs(set_test_path_two())