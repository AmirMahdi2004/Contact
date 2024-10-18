class Contact(object):
    def __init__(self, firstname, lastname, phonenumber1, phonenumber2, homephone, addresshome, postalcode):
        self.first_name_ = firstname
        self.last_name_ = lastname
        self.phone_number1_ = phonenumber1
        self.phone_number2_ = phonenumber2
        self.home_phone_ = homephone
        self.address_home_ = addresshome
        self.postal_code_ = postalcode
        self.negative_one = -1

    def full_name(self):
        if self.first_name_.isalpha() and self.last_name_.isalpha():
            return f"{self.first_name_} {self.last_name_}"
        elif self.first_name_ == "" and self.last_name_ == "":
            return 0
        elif self.first_name_.find(" ") != self.negative_one or self.last_name_.find(" ") != self.negative_one:
            return f"{self.first_name_} {self.last_name_}"
        else:
            return "f1"

    def phone_number1(self):
        if self.phone_number1_.isdigit() and len(self.phone_number1_) == 11 and self.phone_number1_.startswith("0"):
            return f"{self.phone_number1_}"
        elif self.phone_number1_ == "":
            return 0
        else:
            return "f2"

    def phone_number2(self):
        if self.phone_number2_.isdigit() and len(self.phone_number2_) == 11 and self.phone_number2_.startswith("0"):
            return f"{self.phone_number2_}"
        elif self.phone_number2_ == "":
            return 0
        else:
            return "f3"

    def home_phone(self):
        if self.home_phone_.isdigit():
            if len(self.home_phone_) == 8:
                if self.home_phone_.startswith("0") != True:
                    return self.home_phone_
                else:
                    return "f4"

            elif len(self.home_phone_) == 11:
                if self.home_phone_.startswith("0"):
                    return self.home_phone_
                else:
                    return "f4"
            else:
                return "f4"
        elif self.home_phone_ == "":
            return 0
        else:
            return "f4"

    def address_home(self):
        if self.address_home_ == "":
            return 0
        else:
            return self.address_home_

    def postal_code(self):
        if len(self.postal_code_) == 10 and self.postal_code_.isdigit():
            return self.postal_code_
        elif self.postal_code_ == "":
            return 0
        else:
            return "f5"
