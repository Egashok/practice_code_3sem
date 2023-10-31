import numpy as np
from scipy import linalg, stats
from snippet import show,showList
def solution_1():
    M=np.array([[3,-1.2,-8,8],
                [21,-19,0.5,0],
                [7,-4.9,0,-2],
                [1,-2,13,9]])
    return M
print('#1')
M=solution_1()
print("M:")
show(M)

def solution_2(M):
    P,L,U=linalg.lu(M)
    print("L:")
    show(L)
    print("U:")
    show(U)
    print("P:")
    show(P)

    return L,U,P

print('#2')
L,U,P=solution_2(M)
def solution_3():
    print("det U:")
    print(U.diagonal().prod())
    print("det L:")
    print(L.diagonal().prod())
    print("det P:")
    print(np.linalg.det(np.linalg.inv(P)))

    u1 = U.diagonal().prod()
    l1 = U.diagonal().prod()
    p1 = np.linalg.det(np.linalg.inv(P))


    print(u1*l1*p1)






print('#3')
solution_3()


def solution_4():
    print("s1:")
    sample1 = stats.norm.rvs(size=100)
    showList(sample1)
    print("s2:")
    sample2 = stats.uniform.rvs(size=100)
    showList(sample2)
    return sample1,sample2

print('#4')
sample1,sample2=solution_4()



print('#5')

def solution_5(sample1,sample2):
    print("mean:")
    print(np.mean(sample1), '\t', np.mean(sample2))
    print("mode:")
    print(stats.mode(sample1, keepdims=True), '\t', stats.mode(sample2, keepdims=True))
    print("median:")
    print(np.median(sample1), '\t', np.median(sample2))
    print("min:")
    print(min(sample1), '\t', min(sample2))
    print("max:")
    print(max(sample1), '\t', max(sample2))
    print("std:")
    print(np.std(sample1), '\t', np.std(sample2))

solution_5(sample1,sample2)

def solution_6(sample1,sample2):
    print(stats.chisquare(sample1))
    print(stats.chisquare(sample2))

print('#6')
solution_6(sample1,sample2)



