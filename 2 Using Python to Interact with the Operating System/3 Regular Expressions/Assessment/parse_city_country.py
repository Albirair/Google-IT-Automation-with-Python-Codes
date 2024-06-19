#!/usr/bin/env python3
import re
def parse_city_country(text):
    pattern = r"[,.]"
    result = re.split(pattern, text)
    if len(result) != 2:
        return ""
    return result[0]
print(parse_city_country("Paris, France"))
print(parse_city_country("Mumbai, India"))
print(parse_city_country("Rio de Janeiro. Brazil"))
print(parse_city_country("Tokyo! Japan"))