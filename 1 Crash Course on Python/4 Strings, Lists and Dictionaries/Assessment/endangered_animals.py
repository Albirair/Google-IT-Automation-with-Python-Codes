#!/usr/bin/env python3
def endangered_animals(animal_dict):
    result = ""
    for animal in animal_dict:
        result += animal + '\n'
    return result
print(endangered_animals({"Javan Rhinoceros": 60,
      "Vaquita": 10, "Mountain Gorilla": 200, "Tiger": 500}))