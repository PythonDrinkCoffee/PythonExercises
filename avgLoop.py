# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sums = 0
length = 0

for heights in student_heights:
    sums += heights
    length += 1
    
avg = sums / length

print(f"{int(avg)}")