# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91


# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_score = 0 
for score in student_scores:
  max_score = max(student_scores)
print(f"The highest score in the class is: {max_score}")

# Input a Python list of student scores
student_scores = input().split()



# Convert each input string into an integer
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the highest score variable
highest_score = 0

# Iterate through the list to find the highest score
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
