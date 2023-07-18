# Jacob Ramos COP3502C

"""
take an 8-digit password in string format containing only integers
takes the encoded password and assigns it to a new variable
each digit shifted up by 3 numbers
"""


# password encoder

def encoder(password):  # encoder function
    encoded_password = ""  # open string format
    for num in password:  # for loop checks each integer in the string
        digit = str((int(num) + 3) % 10)  # adds the value by 3
        encoded_password += digit

    return encoded_password


# password decoder
"""
takes the encoded password and returns the original password 
opposite of encoder function
"""


def decoder():
    pass


def main():
    while True:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)  # encoder function takes password and encodes it
            print("Your password has been encoded and stored!", encoded_password)  # encoded password stored

        if option == "2":
            pass

        if option == "3":
            return False


if __name__ == '__main__':
    main()
