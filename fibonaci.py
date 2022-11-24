f=[0,1]
i=1
s=0
k=1
n=int(input("ban muon tiem so thu may trong day fibonaci? "))
for i in range (1,n):
    s=f[i-1]+f[i]
    f.insert((k+1),s)
    i=i+1
    k=k+1 #de so tiep theo duoc gan vao vi tri tiep theo o trong day
print(f[n-1])
print(f)

