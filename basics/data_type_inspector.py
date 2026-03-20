#take user input
data = input("Enter your data:")
data_type = type(data)
length = len(data)
print(f"The input is {data_type} type")
print(f"The length is {length}")
if int(data) == True or float(data) == True:
  print("Can be converted to int/float")
else:
  print("Cannot be converted")