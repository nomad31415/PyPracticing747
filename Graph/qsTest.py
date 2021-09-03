def qs(a):
    if len(a) < 2:
        return a

    pivot = a[0]

    left = [x for x in a[1:] if x < pivot]
    right =  [x for x in a[1:] if x >= pivot]

    return qs(left) + [pivot] + qs(right)



if __name__ == '__main__':

    b = [8, 1, 16, 3, 11]

    print(b)
    print(qs(b))
