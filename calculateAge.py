# take input the birth year and calculate age
birth_year = input("Enter your birth year: ")
# by default whatever input we take from console , are in string. We need to convert it to int before integer operation.

age = 2022-int(birth_year)
# print("Age = " + age) is not possible because "str + int" is not possible
print(f"Age = {age}")

