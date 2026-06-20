# Problem 1
# Write a program that receives an integer "n", calculates the sum from 1 to n, and then displays the total sum.
# n = int(input("Enter a number"))
num = 1
sum = 0

while num <= n:
    sum = sum + num
    # print(sum)
    num += 1

# print(f"Total Summation{sum}")


# Problem 2
# Write a program that continuously takes numbers as input until it encounters zero (0). Then, display the multiplication result of all the numbers entered before the zero.


total_production = 1
has_input = False

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break
    
    has_input = True
    total_production *= num  # total_production = total_production * num এর shorthand

if has_input:
    print(f"Total Product: {total_production}")
else:
    print("No numbers entered!")
    

# Problem 3: Shopping List Manager
# Create a shopping list manager where the user can add items to a list one by one. When the user types "done", the input system should stop, and the program must display the entire shopping list along with the total number of items added.