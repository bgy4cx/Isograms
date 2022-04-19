import re

def IsItEmpty(str):
    return str == ""

def IsItAlphabetStr(str):
    x = re.search("[0-9]", str)
    return x is None

def UniqueChars(str):
    str = str.casefold()
    for x in str:
        if str.count(x) > 1:
            UC = False
            break
    else:
        UC = True
    return UC
    
def IsItIsogram(str):
    return IsItEmpty(str) or IsItAlphabetStr(str) and UniqueChars(str)
