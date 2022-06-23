from random import seed, randint

len_of_pass = int(input("Please Enter The length of your password: "))

while 9 < len_of_pass < 0:
    len_of_pass = int(input("You should Enter a number between 1 and 9: "))

password = []
seed(1)
while len(password) < len_of_pass:
    rand_num = randint(0, 9)
    if rand_num not in password:
        password.append(rand_num)

print(''.join(map(str, password)))
