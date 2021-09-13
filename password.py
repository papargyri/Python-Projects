import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlength = int(input("Enter the password length\n"))

    s = []    # Created a empty list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4)) # Appended all the letters, digits, and special characters in the list

    random.shuffle(s)
    password = ("".join(s[0:passlength]))
    
    print(password)

gen()
