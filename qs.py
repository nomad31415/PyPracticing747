
def qs(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]

        left = [i for i in a[1:] if i <= pivot]
        right = [i for i in a[1:] if i > pivot]


        return qs(left) + [pivot] + qs(right)



if __name__ == '__main__':
    a = [8,2,4,17,11,2]
    print(qs(a))
    
