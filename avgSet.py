from __future__ import division

def average(array):
    # your code goes here
    st = set(array)
    rt = round(float(sum(st)/len(st)),3)
    return rt
		    

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
