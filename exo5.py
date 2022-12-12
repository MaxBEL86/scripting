import sys
def Maj(string):
    maj_count=0
    for i in range (4):
        if string[i].isupper():
            maj_count=maj_count+1'
    if maj_count >=2:
        return string.upper()
    else:
        return string
        
print(Maj("HEllo world")) 