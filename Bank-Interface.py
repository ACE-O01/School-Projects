print("Welcome To AIB Bank")

name = input("Enter Your Name: ")
acc_no = input("Enter The Account Number: ")

while True:
    pin = input("Enter a 4-digit PIN Number: ")
    
    # Check if PIN is exactly 4 digits AND contains only numbers
    if len(pin) != 4 or not pin.isdigit():
        print("Please enter a PIN with exactly 4 digits.")
    else:
        print("Your Account Has Been Successfully Created!")
        break
