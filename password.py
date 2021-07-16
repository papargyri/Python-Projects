# A password, sometimes called a passcode, is a memorized secret, typically a string of characters, usually used to confirm the identity of a user.

# Random module is used to perform the random generations. 

import string
import random

def gen():
    s1 = string.ascii_uppercase  # All Upper case letters
    s2 = string.ascii_lowercase  # All Lower case letters
    s3 = string.digits
    s4 = string.punctuation  # String of ASCII characters which are considered punctuation characters in the C locale.

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
