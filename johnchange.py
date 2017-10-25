print(" ")
print(" ")
print(" ")
print("enter ammount of dollars,(input it as  a whole number, a.k.a $24.63 = 2463)")

"print(""Enter the amount of cents"")"
print(" ")
cents= int(input())
print(" ")
dollars= cents // 100
dollarss= 100 * dollars
centss= cents - dollarss
print("Dollars" , dollars)
quarters= centss // 25
quarterss= 25 * quarters
new_cents= centss - quarterss
print("Quarters" , quarters)
dimes= new_cents // 10
print("Dimes" , dimes)
dimess= 10 * dimes
neww_cents= new_cents - dimess
nickles= neww_cents // 5
print("Nickles" , nickles)
nickless= 5 * nickles
newww_cents=  neww_cents - nickless
pennies= newww_cents / 1
total= newww_cents - pennies
print("Pennies" , pennies)
print(" ")
print(" ")
print(" ")
print(" ")

print("Total Remaining" , total)





("divide by 25")
("divide by 10")
("divide by 5")
("divide by 1")
