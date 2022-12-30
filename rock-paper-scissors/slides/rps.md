# [fit] KPMG: Code
## Intro to Coding
#### Rock, Paper, Scissors with Python

---

# [fit] What is programming?

---

# [fit] What is Python?

---

# [fit] What's it used for?

---

# [fit] Who uses it?

---

# Text Editor

---

# [fit] trinket.io

---

# Hello, World!

---

# Hello, World!

```python
print("Hello, World!")
```

---

# Link 1 - Hello World

---

# Putting it all together 1 

```python
print("Welcome to Rock, Paper, Scissors")
```

---

# Link 1 - Rock, Paper, Scissors Intro

---

# Variables

---

# Variables

```python
<variable_name> = <value>
```

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Variables

- Any mix of letters, numbers and some special characters
- Must start with a letter
- Keep lowercase
- Use underscore where there are spaces

---

# Writing Python

- You are not writing an essay...
- Keep things lowercase
- Don't use punctuation
- Replace spaces with underscores

---

# Data Types

---

# Strings

---

# Strings

Characters surrounded by quotes

```python
name = "Safia"
address = "123 Station Road"
favourite_food = "Pizza"
```

---

# Escaping

---

# Escaping

```
\n = New line
\t = Tab
\" = Double Quote
```

---
# Escaping

```python
favourite_food = "Pizza from \"Dough N' Sauce\""
shopping_list = "Apples\nBread\nMilk\nEggs"
```

---

# Link 2 - Escaping

---

# Integer

---

# Integer

A whole number

```python
age = 17
days_in_january = 31
bottles_sitting_on_the_wall = 99
```

----

# Float

----

# Float

A decimal number

```python
price = 12.99
percent = 34.57
pi = 3.1415
```

---

# Numerical Operators

---

# Numerical Operators

| Operator | Action | Example |
| --- | --- | --- |
| + | Addition | `1 + 2` |
| - | Subtraction | `3 - 1` |
| * | Multiplication | `3 * 7` |
| / | Division | `9 / 3` |
| ** | Exponent | `4 ** 2` |
| % | Modulus (remainder) | `10 % 3` |

---

# Numerical Operators

```python
print(1 + 2)
print(5 - 3)
print(3 * 7)
print(49 / 7)
print(4 ** 2)
print(10 % 3)
```

--- 

# Numerical Operators

```python
x = 3
y = 6
area = x * y
```

---

# Link 3 - Numerical Operators

---

# Concatenation

---

# Concatenation

```python
first_name = "Lisa"
last_name = "Henegan"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Link 4 - Concatenation

---

# Input

---

# Input

```python
name = input("What's your name? ")

print("Hello " + name)
```

---

# Link 5 - Input

---

# Putting it all together 2

```python
print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
print("You picked " + user_choice)
```

---

# Link 6 - Rock, Paper, Scissor Input 

---

# Conditionals

---

# If

```python
if 1 == 1:
    print("This is always shown")

if 3 == 5:
    print("This is never shown")    
```

---

# Indenting

```python
name = "Lisa"

if name == "Lisa":
    print("Hello Lisa")
```

---

# Comparators

| Comparator |  Description | Example |
|--- | --- | --- |
| == | Equals | "Lisa" == "Lisa"
| != | Does not equal | "Bill" != "Catherine"
| < | Less than | 4 < 10
| > | Greater than | 12 > 8
| <= | Less than or equal to | 7 <= 7
| >= | Greater than or equal to | 8 >= 5

---

# Else

```python
if 1 == 1:
    print("Yes")
else:
    print("No")    
```

---

# Else

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
```

---

# Link 7 - If/Else

---

# Elif

```python
user_choice = input("What is your move? (rock, paper, scissors) ")

if user_choice == "paper":
    print("You picked paper")
elif user_choice == "scissors":
    print("You picked scissors")
else:
    print("You picked rock")
```

---

# Putting it all together 3

```python
print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
print("You picked " + user_choice)

if user_choice == "rock":
    print("You picked rock")
elif user_choice == "paper":
    print("You picked paper")
else:
    print("You picked scissors")
```

---

# Link 8 - Rock, Paper, Scissors Conditionals

---

# Random Module

---

# Random Module

```python
import random

# Gets a random number between 1 and 10
number = random.randint(1, 10)
print(number) # 7

print(random.choice(["Alia", "Bill", "Catherine", "Dharmesh", "Eve"]))
```

---

# Link 9 - Random Module

---

```python
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
print("The computer picked " + computer_choice)
```

---

# Link 10 - Rock, Paper, Scissors Random Module

---

# Putting it all together 4 

```python
import random

print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
computer_choice = random.choice(["rock", "paper", "scissors"])

print("You picked " + user_choice)
print("The computer picked " + computer_choice)

if user_choice == "rock":
    print("You picked rock")
elif user_choice == "paper":
    print("You picked paper")
else:
    print("You picked scissors")
```

---

# Playing the game 

---

# Playing the game
```python
if user_choice == "rock":
    if computer_choice == "scissors":
        print("You Win")
    elif computer_choice == "paper":
        print("You Lose")
    else:
        print("It's a draw")
elif user_choice == "paper":
    print("You picked paper")
else:
    print("You picked scissors")
    
```

---

# Putting it all together 5

---

```python
import random

print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
computer_choice = random.choice(["rock", "paper", "scissors"])

print("You picked " + user_choice)
print("The computer picked " + computer_choice)

if user_choice == "rock":
    if computer_choice == "scissors":
        print("You Win")
    elif computer_choice == "paper":
        print("You Lose")
    else:
        print("It's a draw")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You Win")
    elif computer_choice == "scissors":
        print("You Lose")
    else:
        print("It's a draw")
else:
    if computer_choice == "paper":
        print("You Win")
    elif computer_choice == "rock":
        print("You Lose")
    else:
        print("It's a draw")
```

---

# Link 11 - Rock, Paper, Scissors Full Game

---

# [fit] Want to learn more?

---

# [fit] Take the full course today
- It's free!
- 10 sessions
- Watch on YouTube in your own time
- Learn to make more games
- Get a KPMG certificate of completion

---

# Thanks :)
