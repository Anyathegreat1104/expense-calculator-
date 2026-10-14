pocketmoney=int(input("Enter your monthly pocket money : "))
food=int(input("Enter your food expense : "))
travel=int(input("Enter your travel expense : "))
shopping=int(input("Enter your shopping expense : "))
other=int(input("Enter your other expense : "))
total=food+travel+shopping+other
remaning=pocketmoney-total 
print("total expense", total )
print("remaning money", remaning)
if remaning>0:
    print("You have saved money")
    saving=(remaning/pocketmoney*100) 
    print("saving percentage", saving)
elif remaning==0:
    print("you have spent all of your money")
else:
    print("You have overspent your money")
