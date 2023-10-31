import scipy
import math
import sympy
import scipy.misc
from sympy import *
import numpy as np
from scipy.optimize import Bounds, minimize, LinearConstraint



def f(x):
    return math.sin(math.sqrt(2 * x))

def solution_1():

    print(scipy.misc.derivative(f,3.5,n=1))
    print(scipy.misc.derivative(f, 3.5,n=2))

print("#1")
solution_1()

def solution_2():
    x = Symbol('x')
    f= sin(sqrt(2 * x))
    print(f.diff(x))
print("#2")
solution_2()

def solution_3():


    result = scipy.integrate.quad(f, 0.0, 1.0)
    print(result)

print("#3")
solution_3()
def solution_4():
    x = Symbol('x')
    f = sin(sqrt(2 * x))
    print(f.integrate(x))

print("#4")
solution_4()
def opt(x):
    return (x[0]+3)**3+(x[1]-3)**2
def constraint(x):
    return x[0]-4*x[1]-12

def solution_5():
    b =(0,np.inf)
    bnds=(b,b)
    constr={'type':'ineq','fun': constraint}
    x0=np.zeros(2)
    solution=scipy.optimize.minimize(opt,x0,method='SLSQP',bounds=bnds,constraints=(constr))
    x=solution.x
    print(solution)
    print('Final:'+str(opt(x)))
    print('x1='+str(x[0]))
    print('x1=' + str(x[1]))


print("#5")

solution_5()