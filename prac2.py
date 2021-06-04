genres=['rock','R&B','Jazz','Metal','soul']
b=[]
i=0
a=genres[i]
while(a!="soul"):
    print(a)
    b.append(genres[i])
    i=i+1
    a=genres[i]


print("we are now outside loop")
print("The vale of b is", b)