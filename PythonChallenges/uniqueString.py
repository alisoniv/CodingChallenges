#Written by Alison I
# Assumes Ascii characters and lowercase and uppercase are equal.

def uniqueString(inString):
    alphabet = [0] * 26
    lowerString = inString.upper()
    for letter in lowerString:
        
        if (ord(letter) != 32):
            alphabet[ord(letter) - 65] += 1
            
            if (alphabet[ord(letter) - 65] > 1):
                return False
    
    return True
    
print(uniqueString("Hello"))