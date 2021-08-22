def bs(ar, tgt):

    low = 0
    high = len(ar) - 1



    while low <=  high:

        m = (low + high ) // 2


        if ar[m] == tgt:
            return m



        if ar[m]  >  tgt:
            high = m - 1
        else:
            low = m + 1





    return None        


if __name__ == '__main__':

    a = [1,2,3,4,5,6,7,8]
    tgt = 8
    print(bs(a,tgt))



    a = [1,3,5,7,9]
    tgt = 3
    print(bs(a,tgt))



    a = [1,2,3,4,5,6,7,8]
    tgt = -1
    print(bs(a,tgt))
