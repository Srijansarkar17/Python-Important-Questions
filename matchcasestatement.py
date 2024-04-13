#similar to switch case in C++
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("X is xero")
    case 4:
        print("X is four")
    case _ if x!=90: #if the input is 90 then the next case is executed.
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:  #default case
        print(x)