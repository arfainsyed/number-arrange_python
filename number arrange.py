a=input('enter the number:')
num=""
n=""
for x in a:
    print(x)
    match x:
        case'0':
            print("zero")
            num="zero"
        case'1':
            print("one")
            num="one"
        case'2':
            print("two")
            num="two"
        case'3':
            print("three")
            num="three"
        case'4':
            print("four")
            num="four"
        case'5':
            print("five")
            num="five"
    n=n+num
print("final number 2 text: ",a,"->",n)