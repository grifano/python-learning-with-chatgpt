# 1️⃣ Conditional Statements (if, elif, else)
print("---Conditional Statements (if, elif, else)---")

num = int(input("Provide number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("The number is zero")

# 2️⃣ Loops: for and while
# 🔹 for Loop (Iterating Over a Range)
print("---for Loop (Iterating Over a Range)---")

for i in range(1, 6): # Loops from 1 to 5
    print(f"Iteration: {i}")

# 🔹 while Loop (Repeats Until a Condition is False) 
print("---while Loop---")

count = 1
while count <= 2:
    print("Increment: ", count)
    count += 1

# 3️⃣ Loop Control Statements
# 🔹 break (Stop the loop early)
print("---break (Stop the loop early)---")

for i in range(1,5):
    if i >= 5:
        print("Stoping when rich 5")
        break
    else:
        print("Increment: ", i);
# 🔹 continue (Skip to the next iteration)
print("---continue (Skip to the next iteration)---")

for i in range(1,5):
    if i == 2:
        print("Skiped 2")
        continue
    print("Looping Numbers: ", i)

# 4️⃣ Mini Project: Even or Odd Checker
print("---Mini Project: Even or Odd Checker---")

number = int(input("Provide a number: "))
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# 5️⃣ Bonus Project: Print only even numbers
print("---Bonus Project: Print only even numbers---")

for i in range(1,10):
    if i % 2 != 0:
        continue
    else:
        print("Even number: ", i)

# using while loop
print("---Bonus Project: Using while loop---")

some_count = 0
while some_count <= 10:
    some_count += 1
    if some_count % 2 != 0:
        continue
    print("Some count: ", some_count)