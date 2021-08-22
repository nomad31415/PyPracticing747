
def gcd(a,b):

   if a < b:
      a,b = b,a

   while ( a % b  > 0):
       r = a % b
       a = b
       b = r

   return b     



if __name__ == '__main__':
    print(gcd(42,285))

