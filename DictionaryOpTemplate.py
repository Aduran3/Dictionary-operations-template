# Template for dictionary operations
#
# @author     Duran, Aaron
# @date       11/11/2021

gradeCounts = { "A": 8, "D": 3, "B": 15, "F": 2, "C": 6 }
print("The grade counts are:", gradeCounts)
print()

# A
# Print all the keys
print("A) All keys in grading is: ", end="")
for key in gradeCounts:
    print(key, end=" ")
print()

# B
# Prints the values
print("B) All the values for grades are:", end=" ")
for key in gradeCounts:
    print(gradeCounts[key], end=" ")
print()

# C
# Prints Key and value pairs
print("C) All the Key and Value pairs are: ", end="")
for key, value in gradeCounts.items():
    print(key + ":" + str(value), end=" ")
print()

# D
# print the pairs in key order
print("D) All key and value pairs in key order: ", end="")
for key, value in sorted(gradeCounts.items()):
    print(key + ":" + str(value), end=" ")
print()

# E
# The average of the values
average = sum(gradeCounts.values()) / len(gradeCounts)
print("E) The average of all grade values is:", average)

# F
# print chart representing the grade values
print("F) Chart below representing the grade values")
for key, value in sorted(gradeCounts.items()):
    print("   " + key + ":", "*" * value)
