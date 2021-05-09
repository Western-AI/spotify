#FinalModels/FinishedModels/ModelEquations/SummingModelEquation.txt
#f = open("../FinishedModels/ModelEquations/SummingModelEquation.txt","w")
#f.write("Hello World")
#f.close()
import numpy as np

class Equation:
    class Equation:

        def applyEquation(self, x_vals):
            print("\n x:", x_vals, "\n powers: ")
            print(self.powers, "\n\n", self.powers.ndim, self.powers[0])
            if self.powers.shape[1] == 1:
                # if x_vals.shape[0] != self.powers.shape[0]:
                #   print("ERROR X not the same size as Powers")
                #  return
                y = self.intercept
                for termsNum in range(0, self.powers.shape[0]):
                    termVal = self.slopes[termsNum]
                    # for power_ in range(0, len(self.powers[termsNum])):
                    termVal = pow(x_vals, self.powers[termsNum]) * termVal
                    print(termVal)
                    y += termVal
            else:
                if self.powers.ndim == 2:
                    if len(x_vals) != len(list(self.powers[0])):
                        print("ERROR X not the same size as Powers")
                        return
                y = self.intercept
                for termsNum in range(0, len(self.powers)):
                    termVal = self.slopes[termsNum]
                    for power_ in range(0, len(self.powers[termsNum])):
                        termVal = pow(x_vals[power_], self.powers[termsNum][power_]) * termVal
                    print(termVal)
                    y += termVal
            return y

slopes =np.array( [ 5.41576048e-04,  7.62133467e-03,  9.50158356e-03, -2.16971503e-04,
 -2.72624148e-05,  1.36804908e-06, -1.19087921e-08, -4.92829579e-10,
  1.20870733e-11, -7.88943563e-14])
powers = np.array([[ 1.] [ 2.] [ 3.] [ 4.] [ 5.] [ 6.] [ 7.] [ 8.] [ 9.] [10.]])
x_vals= np.array([50,50,50,50,50,50,50,50,50,50,50,50,50])
e = Equation(powers,slopes)
print("ans: ", e.applyEquation(x_vals))




"""
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
"""