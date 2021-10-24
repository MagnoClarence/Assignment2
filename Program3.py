print("program 3")
money = int(input("How much money do you have?: "))
apple_cost = int(input("How much is an apple?: "))
print(f"you can buy {int(money / apple_cost)} apples and your change is P{money - (int((money / apple_cost)) * apple_cost)}")