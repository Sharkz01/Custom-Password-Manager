import re

"""
Password Manger
Project 2
SHADO MAMOKETE NKOSI 
L42
"""

class BasePasswordManger:
    def __init__ (self, old_pass, current_password ):
        self.old_pass = old_pass
        self.current_password = current_password

    def old_passwords (self):
        password_list = ["012345","123shd","shado1"]
        self.old_pass = password_list[-1]  # Assign the last element to
        return self.old_pass
    
    def get_password(self):
        self.current_password = self.old_pass
        # print(f"Current password is: {self.current_password}")
        return (f"Current password is: {self.current_password}")

    def is_correct(self):
        user_input = input("Please enter password: ")
        self.password = user_input
        if self.password == self.current_password: #checks if the new password is the same as the current password 
            print("Is these Password the same as the current password? : Yes")  # if true it will print "yes"
        else:
            print("Is these Password the same as the current password? : No")  # if false it will print "no"

        return self.password


class PasswordMananger(BasePasswordManger):
    def get_level(self):
        self.security_level = 0
        check_alph = False
        check_num = False

        if self.password.isdigit() or self.password.isalpha() :
            self.security_level = 0
            print(f"Security level is {self.security_level} - Password consists of alphabets or numbers only.")

        elif check_alph == False and check_num == False and (bool(re.match('^[a-zA-Z0-9]*$', self.password)) == True):  # Used regex to check if password contains alphabets, numbers or special characters
            for i in self.password:
                if i.isalpha() or i.isnumeric():
                    check_alph = True
                    check_num = True
            if check_alph == True and check_num == True:
                self.security_level = 1
                print(f"Security level is {self.security_level} - Password is alphanumeric.")

        elif check_alph == False and check_num == False:
            for i in self.password:
                if i.isalpha() or i.isnumeric():
                    check_alph = True
                    check_num = True       
            if check_alph == True and check_num == True:
                self.security_level = 2
                print(f"Security level is {self.security_level} - Password is alphanumeric WITH special characters.")
        else:
            self.security_level = 1
            print(f"Security level is {self.security_level} - Password is alphanumeric.")

    def set_password(self):
        if len(self.password)<6:
            print("Password length must be a minimun of 6 characters.")
            print("Password Change: UNSUCCESSFUL")
        elif self.security_level<2:
            print("Password must contain special character with numbers and alphabets.")
            print("Password Change: UNSUCCESSFUL")
        elif self.password == self.current_password:
            print("Password Change: No Changes Detected")
        else:
            print("Password Change: SUCCESSFUL")


current = PasswordMananger(["012345","123shd","shado1"],"shado1" )
current.old_passwords()
current.get_password()
current.is_correct()
current.get_level()
current.set_password()

