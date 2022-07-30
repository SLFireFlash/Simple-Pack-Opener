from fun import *

probOut()
packSize =int(input("\nhow many pack You want to open:-"))
for num in range(0,packSize):
    packOpen()

summ =input("Do you want full summery of opened pack(yes or no)")

if (summ == "yes"):
    itemSum()
else:
    print("Thank You")