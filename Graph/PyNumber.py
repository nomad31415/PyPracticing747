# put your python code here

n = input().strip()
res = ''
num = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
for s in n:
    res += num[s] + ' '
print(res)
