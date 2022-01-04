import re
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class UserValidation:
    
    #Check Valid Email
    def checkValidEmail(email):
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False