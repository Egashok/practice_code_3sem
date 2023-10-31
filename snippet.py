def show(m):
    for i in m:
        for z in i:
            print(f'{round(z,2)}\t',end=' ')
        print()
def showList(m):
    a=''
    for i in m:
        a=a+str(i)+" "
    print(a)