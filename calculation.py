def square(a):
    return a*a
def perimeter(l,w):
    return 2(l+w)
def area(l,w):
    return l*w

if __name__ =="__main__":
    a=int(input("enter a value"))
    l=int(input("enter l value"))
    w=int(input("enter w value"))

    s1=square(a)
    print(s1)
    s2=perimeter(l,w)
    print(s2)
    s3=area(l,w)
    print(s3)