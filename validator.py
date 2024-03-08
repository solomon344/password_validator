from string import (digits,ascii_lowercase,ascii_uppercase,punctuation)



def Validate_Password(letters):
    is_greate_or_8 = len(letters) >= 8
    has_lowercase = False
    has_uppercase = False
    has_digits = False
    has_punctuation = False
    for letter in letters:
        if letter in digits:
            has_digits = True
        elif letter in ascii_lowercase:
            has_lowercase = True
        elif letter in ascii_uppercase:
            has_uppercase = True
        elif letter in punctuation:
            has_punctuation = True
    if all([has_punctuation,has_digits,has_lowercase,has_uppercase,is_greate_or_8]):
        print('password is valid')
    else:
        print('invalid password \npassword must be 8 characters with upper,lower,digits and punctiations')


password = input('enter your password to be validated: ')
Validate_Password(password)