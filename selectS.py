
def mx(a):
    max = a[0]
    ind = 0
    l = len(a)
    for i in range(1,l):
        if a[i] < max:
            max = a[i]
            ind = i
    return ind        



def ss(a):
    n = []
    for k in range(len(a)):
        n.append(a.pop(mx(a)))
    return n








if __name__ == '__main__':
    l = [8,11,5,33,26]
    print(ss(l))
