def bubble(a):
    l = len(a)

    for i in range(l):
        for j in range(l - 1, i , -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a






if __name__ == '__main__':

    a = [8,3,1,15,2]

    print(a)
    print(bubble(a))


