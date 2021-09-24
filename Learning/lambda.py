#def double(x):
 #   return x*2

double = lambda x: x * 2

multiply = lambda x, y: x * y

full_name = lambda first_name, last_name: first_name + " " + last_name

age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(5, 7))
print("Bro", "Code")
print(age_check(12))