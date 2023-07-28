from datetime import date
someone = input('Name: ')
year = int(input('Birthyear: '))

today = date.today().year

print(f'hello, {someone} you are {today - year} years old')