Parse CSS Colors
import sys
import math
# Complete the function below.

def  css_string_to_color(colorString):
    #check that it starts with # 
    if colorString[0] != '#':
        #return 'Error'
        raise Exception('Error')
    
    string = colorString[1:]

    #handle short version
    if len(string) == 3:
        string = duplicateShortVer(string)
    #handle everything as long version
    if len(string)==6:
        red = string[0:2]
        green = string[2:4]
        blue = string[4:6]
        
        return getValues(red, green, blue)
    else:
        raise Exception('Error')
    
def hexToDec(string):
    #convert Hex to Dec
    #decimal values of Hex characters
    hexVals = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    total=0
    power=0
    #start from the end so that the power is incremental
    for c in reversed(string):
        value=0
        
        if(c.isalpha()):
            #get value from dictionary
            value=int(hexVals[c.upper()])
        elif c.isdigit():
            value = int(c)
        else:
            #raise an exception if it is not a valid character
            raise Exception('Error')
        
        total = total + (value * int(math.pow(16, power)))
        power+=1
        
    return int(total)
            

def getValues(red, green, blue):
    #get the int values
    string = ""
    #ignore zeroes
    if blue != "00":
        string += blue
    if not (green == "00" and blue == "00"):
        string += green
    if red != "00":
        string += red
    
    string = hexToDec(string)
    
    return string
     
def duplicateShortVer(string):
    return "".join([c*2 for c in string])