due = int (50)
change = int (0)
paid = int (0)
coin = int (0)

while paid < 50:
    print ("Amount Due: ",due)
    coin = int (input ("Insert Coin: "))
    if coin in [25, 10, 5]:
        paid += coin
        print ("Amount Due:",due - paid)

if paid > 50:
    change = paid - due
    print ("Change Due:",change)
