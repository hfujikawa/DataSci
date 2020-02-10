# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:01:17 2020
https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
@author: hfuji
"""

import yaml
import io
import yamlordereddictloader

# Read YAML file
fpath = r'D:\Develop\env_datasci.yaml'
with open(fpath, 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print(data_loaded)

# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)

# https://codeyarns.com/2017/11/23/how-to-read-yaml-file-in-python-with-ordered-keys/
with open(fpath) as f:
    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)