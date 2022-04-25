import pandas as pd
import os
import json

dir_ = os.getcwd()

malig_path = dir_ + '/malignant'
malig_desc_path = dir_ + '/m_desc'

ben_path = dir_ + '/benign'
ben_desc_path = dir_ + '/b_desc'

data = {}

all_files = []

for f in os.listdir(malig_desc_path):
    if os.path.isfile(os.path.join(malig_desc_path, f)):
        all_files.append(f)

for f in os.listdir(ben_desc_path):
    if os.path.isfile(os.path.join(ben_desc_path, f)):
        all_files.append(f)

for f in all_files:
    with open(f) as json_file:
        file = json.load(json_file)
        data[file['name']] = file['meta']['clinical']['benign_malignant']


