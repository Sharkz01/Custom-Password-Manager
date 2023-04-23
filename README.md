# Custom_Password_Manager
_Steps to perform:_            

Implement the following design
class BasePasswordManager

    members

        old_passwords: is a list that holds all of the user's past passwords.

                       he last item of the list is the user's current password.

    methods

        get_password: is a method that returns the current password as a string.


        is_correct: is a method that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not.

 

class PasswordManager

    _This class inherits from BasePasswordManager_

    methods

        set_password: is a method that sets the user's password.

             Password change is successful only if:

                    - Security level of the new password is greater.

                    - Length of new password is minimum 6

             However, if the old password already has the highest security level:

                    - new password must be of the highest security level for a successful password change.

 

        get_level: is a method that returns the security level of the current password. It can also check and return the security level of a new password passed as a string.

        Security levels:

           level 0 - password consists of alphabets or numbers only.

           level 1 - Alphanumeric passwords.

           level 2 - Alphanumeric passwords with special characters.

# Test
* To test all unittest run 'python -m unittest test_custom_password_manager'
* To test a specific test run 'python -m unittest test_custom_password_manager.TestCustomPasswordManager.test_old_password'
* _Note_: Follow the logic to run all the unittests in the project
