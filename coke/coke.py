due = int (50)
change = int (0)
print ("Amount Due: ",due)
coins = int (input ("Insert Coin: "))

while coins < 50:
    print ("Amount Due: ",due - coins)
    coins += int (input ("Insert Coin: "))

if coins > 50:
    change = coins - due

print ("Change Due: ",change)
