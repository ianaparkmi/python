money=int(input("enter a amount of money"))
k100=money//100
ost=money%100
k50=ost//50
ost=ost%50
k10=ost//10
ost=ost%10
k5=ost//5
ost=ost%5
k2=ost//2
ost=ost%2
k1 = ost
print(f"for {money}  you will need: ")
print("100 BYN:",k100)
print("50 BYN:",k50)
print("10 BYN:",k10)
print("5 BYN:",k5)
print("2 BYN:",k2)
print("1 BYN:",k1)