#function setting choices
def get_menu_choice():
    print("*** Menu ***")
    print()
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")
    print()
    user_choice()
#Function prompts and validates a user choice    
def user_choice():

    menu_choice = input("What would you like to do[1, 2, 3, 4]? ")
    #If user chooses 1 runs the encrypt function
    if menu_choice == "1":
        print("String encription")
        print()
        encrypt()
    # if user chooses 2 runs decryption function
    elif menu_choice == "2":
        print("String decryption")
        print()
        decrypt()
    #If user chooses 3 runs brute force decryption
    elif menu_choice == "3":
        print("BRUTE FORCE")
        print()
        brute_force()
    #if user chooses 4 the program closes
    elif menu_choice == "4":
        print()
        print("Goodbye")
        print()
    #loop to check if user choice is in valid range or starts function again if user choice is not valid
    elif menu_choice not in range(1,4):
        print("Invalid choice, Please enter either 1,2,3 or 4.")
        print()
        user_choice()

#defines encrypt function
def encrypt():
    original_string = input("Please enter a string to encrypt: ")
    result = ""
    offset = offset_value()
    #Iterates over input and swaps characters then saves to a new variable "result"
    for let in range(len(original_string)):
        char = original_string[let]
        result += chr((ord(char) + offset)) if (ord(char) + offset) <= 127 and (ord(char) + offset) >= 32 else chr((ord(char) +  offset - 95) % 125)
    print()
    print("Encrypted string:\n" + result)
    print()
    #calls get_menu_choice function to prompt for choice
    get_menu_choice()
#defines offset_value function to validate a offset for integer
def offset_value():
    offset = int(input("Please enter an offset value (1 to 94): "))
    while offset not in range(1,95):
        offset = int(input("Please enter an offset value (1 to 94): "))
    
    return offset
    
#defines decrypt function
def decrypt():
    cypher_text = input("What would you like to decrypt: ")
    result = ""
    offset = offset_value()#calls offset_value function and returns to offset variable
    #iterates over cypher text and undoes encryption with offset_value
    for let in range(len(cypher_text)):
        char = cypher_text[let]
        result += chr((ord(char) - offset)) if (ord(char) - offset) <= 127 and (ord(char) - offset) >= 32 else chr((ord(char) - offset + 95) % 125)
    print()
    print("Decrypted:\n" + result)
    print()
    #calls get_menu_choice function to prompt for choice
    get_menu_choice()
    
#defines the brute_force function
def brute_force():
    offset = 1
    encrypted_string = input("Please enter a string to decrypt: ")
    result = ""
    #loops over string for value of position with offset value 1 through 94
    while offset in range(1,95):
        
        for let in range(len(encrypted_string)):
            char = encrypted_string[let]
            result += chr((ord(char) - offset)) if (ord(char) - offset) >= 32 and (ord(char) - offset) <= 127 else chr((ord(char) - offset + 95) % 125)

        print("Offset: " + str(offset) + "= Decrypted string: " + result)
        result = ""
        offset += 1
    print()
    get_menu_choice()

#define my_details function to print my information
def my_details():
    print("File: 'welcome.py'")
    print("Author: Ty Hancock")
    print("Email Id: hanty027@mymail.unisa.edu.au")
    print("Description: Programming Assignment 2 - Caesar Cipher.")
    print("This is my own work as defined by the University's")
    print("Academic Misconduct Policy.")
    print()
    print()





my_details()#calls my_details function only when program is run the first time 
get_menu_choice()#driving function starts program
