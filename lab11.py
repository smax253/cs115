"""
    Max Shi
    Lab 11: Quadratic Eq Class
    11/14/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

class QuadraticEquation:
    def __init__(self, a,b,c):
        if a==0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        else: self.a = a*1.0
        self.b = b*1.0
        self.c = c*1.0
    def discriminant(self):
        return self.b**2-4*self.a*self.c
    def root1(self):
        if(self.discriminant()<0): return None
        return (self.b*-1+(self.discriminant()**(1/2)))/(2*self.a)
    def root2(self):
        if(self.discriminant()<0): return None
        return (self.b*-1-(self.discriminant()**(1/2)))/(2*self.a)

    def __str__(self):
        stra = ""
        op1 = ""
        if self.a<0: op1 = "-"
        if abs(self.a) != 1: stra += str(abs(self.a))
        if self.a != 0: stra += "x^2"
        op2 = ""
        strb = ""
        if self.b<0: op2 = " - "
        elif self.b>0: op2 = " + "
        if abs(self.b) != 1 and self.b != 0: strb += str(abs(self.b))
        if self.b != 0: strb += "x"
        op3 = ""
        strc = ""
        if self.c<0: op3 = " - "
        elif self.c>0: op3 = " + "
        if abs(self.c) != 0: strc = str(abs(self.c))
        return op1+stra+op2+strb+op3+strc + " = 0"