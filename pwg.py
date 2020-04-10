#!/usr/bin/python3

import random, string, pyperclip

## User Input for length of password between 8 - 40 characters  ✅ 



def main():
    while True:
        pwd_length = input('How long would you like the password to be?\n(Mut be between 8-40 characters long): ')
## DONE Generate password ✅
        while int(pwd_length) < 8 | int(pwd_length) > 40:
            pwd_length = input('How long would you like the password to be? \n (Mut be between 8-40 characters long): \n')


        if int(pwd_length) in range (8,40):
# Random password Generator
                password = str(passwordGenerator((pwd_length)))
                pyperclip.copy(password)
                print ('\nYour password is:' + password)
                print ('It has already been copied to your clipboard! \n')
                break

        else:
            print('Please choose a number between 8 and 40 to create a secure password. \n')

def passwordGenerator(stringLength):
            letters = (string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation)
            pwd = ''.join(random.choice(letters) for i in range(int(stringLength)))
            return pwd



if __name__ == '__main__':
    main()
