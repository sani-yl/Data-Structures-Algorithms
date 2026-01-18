#exercise_1:
a = input()
print("".join(sorted(a)))

#exercise_2:
a = int(input())
b = int(input())

print(f"{a} + {b} is {a + b}")
print(f"{a} - {b} is {a - b}")
print(f"{a} * {b} is {a * b}")
print(f"{a} / {b} is {a / b}")
print(f"{a} % {b} is {a % b}")
print(f"{a} ^ {b} is {a ** b}")

#exercise_3:
N = int(input())

#create dictionary with keys 1.. N and values as squares
squares_dict = {i: i**2 for i in range(1, N+1)} 
print(squares_dict)

#exercise_4:
n = int(input())

sum = n * (n + 1) // 2 #using the formula: sum = n * (n + 1) // 2

print("The sum of the first", n, "positive integers is", sum)


#exercise_5:
s = input() #read input string
vowels = "aeiou" #valid vowels
count = 0

#count vowels in the string
for char in s.lower(): #convert to lowercase to handle capital letters
    if char in vowels:
        count += 1

print("Number of vowels:", count)


#exercise_6:
total = 0.0  # Initialize sum as a floating-point number

while True:
    user_input = input()  # read input from user

    if user_input == "0":  # exit condition
        break

    try:
        number = float(user_input)  # try to convert input to a number
        total += number
        print(f"The total is now {total}")
    except ValueError:
        print("That wasn’t a number.")

print(f"The grand total is {total}")


#exercise_7:
def custom_encoder(text):
    reference_string = "abcdefghijklmnopqrstuvwxyz"
    positions = []
    
    for char in text.lower():  # convert to lowercase
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    
    return positions

#exercise_8:
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")


#exercise_9:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name      
        self.cuisine_type = cuisine_type 
    
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


#exercise_10:
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back {self.username}!")



#exercise_11:
def combine_lists(list1, list2):
    combined = []
    i = 0  # pointer for list1
    j = 0  # pointer for list2
    
    # merge the two lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # add any remaining elements from list1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    # add any remaining elements from list2
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined



