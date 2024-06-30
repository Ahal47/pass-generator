import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "@#$%?"

upper, lower, nums, sys = True, True, True,True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums :
    all += digits
if sys:
    all += symbols

length = 20
amount = 5

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)