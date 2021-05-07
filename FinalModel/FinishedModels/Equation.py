
import numpy as np


def toArray(string):
    string = string.strip()
    string = string[1:len(string) - 1]
    array = []
    if string.__contains__("["):
        while string.__contains__("["):
            array.append(toArray(string[string.index("["): string.index("]") + 1]))
            string = string[string.index("]") + 1:]
    else:
        s = string
        newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
        listOfNumbers = [float(i) for i in newstr.split()]
        array = listOfNumbers

    return np.array(array)

class Equation:

    def applyEquation(self, x_vals):
        print(self.powers,"\n\n", self.powers.ndim,self.powers[0])
        if self.powers.shape [1] == 1:
            #if x_vals.shape[0] != self.powers.shape[0]:
             #   print("ERROR X not the same size as Powers")
              #  return
            y = self.intercept
            for termsNum in range(0, self.powers.shape[0]):
                termVal = self.slopes[termsNum]
                #for power_ in range(0, len(self.powers[termsNum])):
                termVal *= pow(x_vals[termsNum], self.powers[termsNum])
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
                    termVal *= pow(x_vals[power_], self.powers[termsNum][power_])
                print(termVal)
                y += termVal
        return y

    def __init__(self, powers, slopes_, intercept=0):
        self.powers = powers
        self.intercept = intercept
        self.slopes = slopes_
        print(self.slopes)