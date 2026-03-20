#take input of user records
n = 5
name_list = []
age_list = []
score_list = []
for i in range(n):
  name = input("Enter your name:")
  age = int(input("Enter your age:"))
  score = float(input("Enter your score:"))
  name_list.append(name)
  age_list.append(age)
  score_list.append(score)

#printing the values in csv syle
print(f"Name,Age,Score")
for i in range(n):
  print(f"{name_list[i]},{age_list[i]},{score_list[i]}")