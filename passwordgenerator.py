import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols= [
    '!', '@', '#', '$', '%', '&', '*', '(', ')'
]
digit=['1','2','3','4','5','6','7','8','9','0']

print("Welcome to Password Generator !!!")

n_letters=int(input("How many letters u want in your password ?"))
n_symbols=int(input("How many symbols u want in your password ?"))
n_digit=int(input("How many digit u want in your password ?"))

password=[]

for i in range(n_letters):
    char=random.choice(letters)
    password+=char
for x in range(n_symbols):
    sym=random.choice(symbols)
    password+=sym
for y in range(n_digit):
    dig=random.choice(digit)
    password+=dig

random.shuffle(password)

password_str=""

for char in password:
    password_str+=char
print(f"Your Generated password is :{password_str}")

