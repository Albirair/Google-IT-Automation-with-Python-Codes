#!/usr/bin/env python3
import os
import requests
PATH = "/data/feedback"
files = os.listdir(PATH)
for review in files:
    r = open(os.path.join(PATH, review))
    title = r.readline()[:-1]
    name = r.readline()[:-1]
    date = r.readline()[:-1]
    feedback = r.read()[:-1]
    deserialized = {"title":title, "name":name, "date":date, "feedback":feedback}
    response = requests.post("http://localhost/feedback/", json=deserialized)
    print(response.status_code)