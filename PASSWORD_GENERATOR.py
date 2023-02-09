
# PASSWORD GENERATOR


import random

def passwordGenerator(n):
  
    lowerchar=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    upperchar=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    specialchar=['!','&','$', '%', '#']

    numericchar=['0','1','2','3','4','5','6','7','8','9']
    
    Characters = lowerchar + upperchar + specialchar +  numericchar
    
# Initializing an empty string to store the password.
    password = ""
    
    for i in range(n):
        
# Randomly selecting one character and appending it to the resultant password string
        password += random.choice(Characters)

    return password

if __name__ == "__main__":
    n = 8
    password = passwordGenerator(n)
    print(password)