print("Welcome To AIB Bank")
name = input("Enter Your Name:")
acc_no = input("Enter The Account Number:")
while True:
    pin = (input("Enter A 4-digit Pin Number:"))
    if len(pin)!=4 or not pin.isdigit():
        print("Please Enter A Pin With Exactly 4-digits")
    else:
        print("Your Account Has Been Successfully Created")
        break
            