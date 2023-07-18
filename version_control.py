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

#Alexis Jimenez
def decode(encoded_password): #takes in the encoded_password as argument
    decoded_password = "" #will contain decoded password
    for num in encoded_password:
        decoded_password += str((int(num) - 3) % 10) #subtracts 3 and ensures the number is between 0 and 9
    return decoded_password


def main():
    while True:

        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)  # encoder function takes password and encodes it
            print("Your password has been encoded and stored!", encoded_password)  # encoded password stored

        if option == "2":
            #following print statement calls the function for encoded and then for decoded password
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")

        if option == "3":
            return False


if __name__ == '__main__':
    main()
