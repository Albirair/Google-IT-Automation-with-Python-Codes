#!/usr/bin/env python3
import re
def secure_website_domain(website):
    pattern = r"https://www\.(.+)\.co(m?)"
    result = re.search(pattern, website)
    if result is None:
        return ""
    return result[1]
print(secure_website_domain("http://www.text.com"))
print(secure_website_domain("https://www.text.com"))
print(secure_website_domain("http://www.text.co"))
print(secure_website_domain("https://www.text.co"))