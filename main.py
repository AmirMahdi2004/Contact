import csv

import Contacts
while (True):
    name = input("Enter your name : ")
    last_name = input("Enter your last name : ")
    phone = input("Enter phone number 1 : ")
    phone2 = input("Enter phone number 2 : ")
    home_phone = input("Enter home phone : ")
    address = input("Enter address home : ")
    postal_code = input("Enter postal code : ")
    contact = Contacts.Contact(name, last_name, phone, phone2, home_phone, address, postal_code)
    if contact.full_name() == "f1" or contact.full_name() == 0:
        print(" Your name is not valid")
    elif contact.phone_number1() == "f2" or contact.phone_number1() == 0:
        print("The mobile number 1 is not valid")
    elif contact.phone_number2() == "f3":
        print("The mobile number 2 is not valid")
    elif contact.home_phone() == "f4" or contact.home_phone() == 0:
        print("The house number is not valid")
    elif contact.postal_code() == "f5":
        print("The postal code is not valid")
    else:
        with open("contact.csv", 'a', newline='') as my_file:
            file = csv.writer(my_file)
            file.writerow([contact.full_name(), contact.phone_number1(), contact.phone_number2(), contact.home_phone(),
                           contact.postal_code(), contact.address_home()])
    the_end = input("Will you add someone else? n/y")
    if the_end == "n":
        break
