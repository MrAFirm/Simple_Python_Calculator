print("Welcome to my calculator!")

print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

operator = input("Please Select the number# of operator for calculation.\n")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

if operator == "1":
	result = num1 + num2
	print(f"Total after addition is: {result}")
elif operator == "2":
	result = num1 - num2
	print(f"Total after subtraction is: {result}")
elif operator == "3":
	result = num1 * num2
	print(f"Total after multiplication is: {result}")
elif operator == "4":
	result = num1 / num2
	print(f"Total after division is: {result}")
else:
	print("\nWrong input!\n")
