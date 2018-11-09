import math
import numpy as np
print(math.floor(np.pi))
class Circle:
    
    
    def __init__(self,p,d):
        if p <= 0:
            p = 2
        self.precision = p
        self.diameter = d
        self.radius = d/2


    def CalcCircumference(self):
        Circumferences = []
        Circ_percent_changes = []
        for i in range(self.precision+1):
            pi = math.floor(np.pi*10**i)/10**i
            C = pi*self.diameter
            Circumferences.append(C)
            print("For a precision of ", i)
            print("The value of pi is ", pi)
            print("The circumference of this circle is : ", Circumferences[i])
            if len(Circumferences) > 1:
                Circ_percent_changes.append(round((abs(Circumferences[i-1]-Circumferences[i])/Circumferences[i])*100,3))
                print("% change in Circumference: ", round((abs(Circumferences[i-1]-Circumferences[i])/Circumferences[i])*100,3),'%')
            print('\n')
        return Circumferences, Circ_percent_changes
     
    def CalcArea(self):
        Areas = []
        Area_percent_changes = [] 
        for i in range(self.precision+1):
            pi = math.floor(np.pi*10**i)/10**i
            A = pi*(self.radius**2)
            Areas.append(A)
            print("For a precision of ", i)
            print("The value of pi is ", pi)
            print("The Area of this circle is: ", Areas[i])
            if len(Areas) > 1:
                Area_percent_changes.append(round((abs(Areas[i-1]-Areas[i])/Areas[i])*100),3)
                print("% change in Area: ", round((abs(Areas[i-1]-Areas[i])/Areas[i])*100),3)
            print('\n')

        return Areas, Area_percent_changes

diameter = input("Enter the diameter of a circle ")
precision = input("Enter the precision value for pi ")


C = Circle(precision,diameter)
Areas,percent_change_area = C.CalcArea()
Circumferences, percent_change_circumferences = C.CalcCircumference()
