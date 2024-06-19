#!/usr/bin/env python3
def linear_search(list, key):
   steps=0
   for _, item in enumerate(list):
       steps += 1
       if item == key:
           break
   return steps
def binary_search(list, key):
   list.sort()
   steps=1
   left = 0
   right = len(list) - 1
   while left <= right:
       steps += 1
       middle = (left + right) // 2
       if list[middle] == key:
           break
       if list[middle] > key:
           right = middle - 1
       if list[middle] < key:
           left = middle + 1
   return steps
def best_search(list, key):
   steps_linear = linear_search(list, key)
   steps_binary = binary_search(list, key)
   results = "Linear: " + str(steps_linear) + " steps, "
   results += "Binary: " + str(steps_binary) + " steps. "
   if (steps_linear < steps_binary):
       results += "Best Search is Linear."
   elif (steps_linear > steps_binary):
       results += "Best Search is Binary."
   else:
       results += "Result is a Tie."
   return results
print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))