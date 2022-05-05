#https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c


A=[[1,2,3],[4,5,6],[7,8,9]]
print("#もとのリスト")
for i in A:
    print(i)
print("===============")
for i in A:
    print(i[::-1])

print("====================")
for i in reversed(A):
    print(i)
print("=================")
print("180 度回転")
for i in reversed(A):
    print(i[::-1])

print("=================")
for x in zip(*A):
    print(x)
print("===============")
print("右に90 度")
for x in zip(*A):
    print(list(x[::-1]))