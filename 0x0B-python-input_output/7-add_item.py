#!/usr/bin/python3
"""
Module contains some scripting code
"""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
new_list = []
for arg in sys.argv[1:]:
    new_list.append(arg)
save_to_json_file(new_list, "add_item.json")
load_from_json_file("add_item.json")
