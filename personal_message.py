# Adding method lower() to receive inputs without capital letters to storage them
name = input('What is your name? ').lower().strip().title()
last_name = input('What is your last name?').lower().strip().title()
full_name = name + ' ' + last_name

greeting = f'Hello, welcome back {full_name}! Do you want to study Python again?'

print(greeting)