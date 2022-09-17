#Checks if a selected character is in the alphabet and its casing


def isAlphabet(a):
    #return True if alphabetic
    a = str(a)      #Convert input to a string for processing

    if ((a >= 'a') or (a >= 'A')) and (len(a) == 1):
        return True
    return False

def itsUpper(a):
    #Return True if uppercase
    if (a <= 'Z') and (len(a) == 1):
        return True
    return False

def itsLower(a):
    #Return True if lowercase
    if (a >= 'a') and (len(a) == 1):
        return True
    return False

