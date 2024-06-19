#!/usr/bin/env python3
import re
def find_productID(report):
    pattern = r"1\d{3}-[A-Z]{2}-\d{2}"
    result = re.findall(pattern, report)
    return result
print(find_productID(
    "Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30"))
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29."))