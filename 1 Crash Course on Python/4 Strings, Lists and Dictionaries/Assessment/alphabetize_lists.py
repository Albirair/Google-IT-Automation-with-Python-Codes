#!/usr/bin/env python3
def alphabetize_lists(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list
Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]
print(alphabetize_lists(Aniyahs_list, Imanis_list))