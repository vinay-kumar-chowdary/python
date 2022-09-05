print("enter the marks of subjects:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=a+b+c+d+e
avg=total/5
print("avg ",avg)


if avg>=91:
    print("a grade")
elif avg>=81 and avg<=90:
    print("b grade")
elif avg>=71 and avg<=80:
    print("c grade")
elif avg>=61 and avg<=70:
    print("d grade")
elif avg>=50 and avg<=60:
    print("e grade")
else:
    print("fail")
            
