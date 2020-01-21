#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    stage_1 = load_from_json_file(filename)
except:
    stage_1 = []

arg = sys.argv[1:]
stage_1 += arg
save_to_json_file(stage_1, filename)
