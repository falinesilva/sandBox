due = 50
change = 0
paid = 0

while paid < 50:

    print ("Amount Due:",due - paid)
    coin = int (input ("Insert Coin: "))

    if coin in [25, 10, 5]:
        paid += coin
    
    if paid >= due:
        break
        

if paid >= 50:
    change = paid - due
    print ("Change Owed:",change)
