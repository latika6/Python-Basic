# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole numbr = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
# Example Input 1
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
# Example Output 1
# total height = 857
# number of students = 5
# average height = 171

# Input a Python list of student heights
student_heights = input().split()

# Convert each input string into an integer
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Calculate total height
total_height = sum(student_heights)

# Calculate the number of students
num_students = len(student_heights)

# Calculate the average height
average_height = round(total_height / num_students)

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {average_height}")

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
