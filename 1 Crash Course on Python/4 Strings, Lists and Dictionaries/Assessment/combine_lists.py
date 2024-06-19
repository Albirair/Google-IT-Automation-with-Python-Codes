#!/usr/bin/env python3
def combine_lists(list1, list2):
    combined_list = []
    list1.reverse()
    list2.extend(list1)
    combined_list = list2
    return combined_list
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]
print(combine_lists(Jaimes_list, Drews_list))