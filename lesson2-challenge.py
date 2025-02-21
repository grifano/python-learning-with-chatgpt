# 🔥 Mini-Challenge: Print only even numbers
# Try writing a loop that:
# 	1.	Asks the user to enter numbers.
# 	2.	Skips numbers divisible by 3.
# 	3.	Stops when the user enters 0.

# 💡 Hint: Use continue for numbers divisible by 3 and break when 0 is entered.
number = 1
while number != 0:
    number = int(input("Enter a number: "))
    
    if number == 0: # Stop the loop when user enters 0
        break

    if number % 3 == 0: # Skip numbers divisible by 3
        continue
    print(f"You entered: {number}. To exit enter 0")