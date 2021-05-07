#FinalModels/FinishedModels/ModelEquations/SummingModelEquation.txt
#f = open("../FinishedModels/ModelEquations/SummingModelEquation.txt","w")
#f.write("Hello World")
#f.close()
import numpy as np

def toArray(string,ver=0):
    string= string.strip()
    string=string[1:len(string)-1]
    array =[]
    if string.__contains__("["):
        while string.__contains__("["):
            array.append(toArray(string[ string.index("[") : string.index("]")+1 ]))
            string =string[string.index("]")+1:]
    else:
        s = string
        newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
        listOfNumbers = [float(i) for i in newstr.split()]
        array=listOfNumbers
    return array

f = open("../FinishedModels/ModelEquations/SummingModelEquation.txt","r")
#f = open("ModelEquations/SummingModelEquation.txt", "r")
text = f.read()
#r_sq = float(text[text.index("s:"):][2:])
powers = (text[:text.index("s:")][2:])
powers = np.array(toArray(powers))
slopes = text[text.index("s:"):text.index("i:")][2:]
slopes =np.array(toArray(slopes))
intercept = float(text[text.index("i:"):text.index("r")][2:])
r_sq = float(text[text.index("r:"):][2:])
print(powers)
print(type(powers))
print(type(powers[0][0]))
print(slopes)
print(slopes.shape)
print(type(powers.shape))
f.close()
