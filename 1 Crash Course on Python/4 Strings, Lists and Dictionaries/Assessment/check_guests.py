#!/usr/bin/env python3
def check_guests(guest_list, guest):
    return guest_list[guest]
guest_list = {"Adam": 3, "Camila": 3, "David": 5, "Jamal": 3,
              "Charley": 2, "Titus": 1, "Raj": 6, "Noemi": 1, "Sakira": 3, "Chidi": 5}
print(check_guests(guest_list, "Adam"))
print(check_guests(guest_list, "Sakira"))
print(check_guests(guest_list, "Charley"))