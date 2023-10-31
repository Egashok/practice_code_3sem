import random
import numpy as np
from  numpy.linalg import matrix_power,det,solve

from snippet import show,showList

def solution_1():
    my_array=np.arange(10, 70,2)
    return my_array

print("#1")
a=solution_1()
showList(a)

def solution_2():
    matrix=np.reshape(a,(6,5))
    matrix=np.transpose(matrix)

    return matrix
print("#2")
a=solution_2()
show(a)

def solution_3():
    matrix=np.multiply(a,2.5)
    nrow=random.randint(0,4)
    matrix[nrow]=matrix[nrow]-5
    return matrix

print("#3")
show(solution_3())

def solution_4():
    matr=np.random.uniform(0,11,(6,3))
    return matr
print("#4")
b=solution_4()
show(b)

def solution_5():

    asum=np.sum(a,axis=0)
    print(len(asum))
    bsum=np.sum(b,axis=1)
    print(len(bsum))



    return asum,bsum
print("#5")
show(solution_5())


def solution_6():
    return np.matmul(a,b)
print("#6")
show(solution_6())


def solution_7():

    A=np.delete(a,2,1)
    B=np.concatenate([b,np.random.rand(6,3)*10+10],axis=1)
    return A,B
print("#7")

ar,br=solution_7()
show(ar)
show(br)

def solution_8():

    ar,br=solution_7()

    adet=np.linalg.det(ar)
    bdet=np.linalg.det(br)

    print(adet)
    print(bdet)

    if not adet == 0:
        show(np.linalg.inv(ar))
    if not bdet == 0:
        show(np.linalg.inv(br))
print("#8")
solution_8()

def solution_9():


    a6=np.power(ar,6)
    b14 = np.power(br, 14)


print("#9")
solution_9()

def solution_10():


    a=np.array([[3,-1.2,-8,8],
             [21,-19,0.5,0],
                [7,-4.9,0,-2],
                [1,-2,13,9]])
    b = np.array([20,-8,11,3])
    x = np.linalg.solve(a, b)

    return x

print("#10")
showList(solution_10())