#!/usr/bin/env python3
def countries(countries_dict):
    result = ""
    for countries in countries_dict.values():
        result += "{}\n".format(countries)
    return result
print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia": [
      "China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))