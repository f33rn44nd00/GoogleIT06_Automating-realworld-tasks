#! /usr/bin/env python3

import os
import requests

source_dir = "/data/feedback"
feed_dict = {}
feed_file_list = [f for f in os.listdir(source_dir)]

for fl in feed_file_list:
    with open("/data/feedback/"+fl) as f:
        lines = f.readlines()
        feed_dict.update({"title":lines[0], "name":lines[1], "date":lines[2], "feedback":lines[3]})
    req = requests.post("http://34.173.40.21/feedback/",data=feed_dict)
    if req.ok:
        continue
    else:
        print(req.request.body)
        break
