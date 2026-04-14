# ===================================
# Topic: Python Basics
# Author: Kalyan
# Description: Beginner to loops concepts with examples
# ===================================

print("Welcome to beginner coding program!\n")

# ==============================
# 1. STRINGS
# ==============================

a = 'Hi rookie coder'
b = "It's a great day to learn coding"

print(a)
print(b)

# Multiline string
c = ("Hi rookie coder "
     "Now you're learning Python "
     "You will be a pro in meantime")
print(c)

# ==============================
# 2. VARIABLES & PRINTING
# ==============================

name = "Ladlee"
age = 30
work = '"Ghop Ghop Ghop"'

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My work is {work}")

# ==============================
# 3. STRING OPERATIONS
# ==============================

x = "dna is "
y = "essential for life"

print(x + y)
print("Length:", len(x))
print("Slice:", x[5:6])
print("Safe slice:", x[5:100])

# ==============================
# 4. DNA EXAMPLE (BIO)
# ==============================

dna = "ATGCTAGCTAGCTAGCTAGUUU"

print("Start codon:", dna[0:3])
print("Next codon:", dna[3:6])
print("Reverse:", dna[::-1])
print("Last codon:", dna[-3:])

# ==============================
# 5. INPUT & TYPE CASTING
# ==============================

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Without casting:", num1 + num2)

num_sum = float(num1) + float(num2)
print(f"With casting: {num_sum}")

# ==============================
# 6. TYPE CONVERSION PRACTICE
# ==============================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

loyalty_input = input("Are you in loyalty program? (yes/no): ")
loyalty = loyalty_input.lower() == "yes"

print(type(name), type(age), type(height), type(loyalty))

# ==============================
# 7. BILL CALCULATOR
# ==============================

coffee = float(input('1 coffee @: $ '))
sandwich = float(input('1 sandwich @: $ '))
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

print(f"Total bill: $ {bill_total:.2f}")

# ==============================
# 8. CONDITIONS
# ==============================

bill_total = 114
discount = 10

if bill_total > 100:
    bill_total -= discount

print(f"Final bill: $ {bill_total:.2f}")

# ==============================
# 9. LOYALTY PROGRAM LOGIC
# ==============================

loyalty_program = True
bill_amount = float(input('Enter bill amount: '))

discount_amount = 0
penalty_amount = 0

if loyalty_program and bill_amount > 1500:
    discount_amount = bill_amount * 0.10

elif loyalty_program and bill_amount > 1000:
    discount_amount = bill_amount * 0.05

else:
    penalty_amount = bill_amount * 0.05

total = bill_amount - discount_amount + penalty_amount

print(f"Final bill: $ {total:.2f}")

# ==============================
# 10. MATCH CASE
# ==============================

http_status = 400

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case _:
        print("Unknown")

# ==============================
# 11. LOOPS
# ==============================

# For loop
for i in range(5):
    print("Loop:", i)

# Loop through tuple
foods = ('idli', 'dosa', 'vada')
for food in foods:
    print("I like", food)

# While loop
games = ['chess', 'soccer', 'basketball']
i = 0
while i < len(games):
    print("Playing", games[i])
    i += 1

# ==============================
# 12. LOOP CONTROL
# ==============================

# break
cities = ['Mumbai', 'Delhi', 'Bangalore']
for city in cities:
    if city == 'Delhi':
        print("Found Delhi!")
        break

# continue
diseases = ['Diabetes', 'Asthma', 'Cancer']
for d in diseases:
    if d == 'Asthma':
        continue
    print("Concern:", d)

# pass
for i in range(3):
    if i == 1:
        pass
    print(i)