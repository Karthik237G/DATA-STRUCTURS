#linear search
def linsearch(n, arr):
    for i in range(len(arr)):
        if arr[i] == n:
            print(i)
    return
k=int(input())
print("enter K :",k)
arr=[]
for m in range(k):
    inp=int(input())
    arr.append(inp)
print("enter n:")
n=int(input())
linsearch(n,arr)

