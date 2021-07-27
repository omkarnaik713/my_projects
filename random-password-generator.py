import random
import math
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
special = '@#$%&*'

# inputting the length of the password
length = int(input('Enter the lenght of the password : '))
password = []

len_alpha = length // 2
len_num = math.ceil(length * 30 / 100)
len_special = length - len_alpha - len_num

def password_generator(string , l):
    for i in range(l):
        index = random.randint(0, len(string))
        if string[index].isalpha():
            c = random.randint(0,1)
            if c == 1 :
                password.append(string[index].upper())
        password.append(string[index])

    return password


# calling the function for alpha
password_generator(alpha, len_alpha)
# calling for num
password_generator(num, len_num)
# calling for special
password_generator(special, len_special)
# shuffling the list
random.shuffle(password)

#converting the password to string
password_string = ''.join(password)
print(password_string)
