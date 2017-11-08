print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("I can convert distances")
print(" ")
print("enter a unit")
print(" ")
unit1 = input()
print(" ")
print("enter the distance")
num = int(input())
print(" ")
print("enter a unit to convert to")
print(" ")
unit2 = input()
if unit1 == 'miles' or unit1 == 'mi' and unit2 == 'kilometers' or unit2 == 'km':
    dist=(num * 1.62137)

elif unit1 == 'miles' or unit1 == 'mi' and unit2 == 'feet' or unit2 == 'f':
    dist=(num * 5280)

elif unit1 == 'miles' or unit1 == 'mi' and unit2 == 'meters' or unit2 == 'm':
    dist=(num * 1,609.344)

elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'miles' or unit2 == 'mi':
    dist=(num * 0.62137119)

elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'feet' or unit2 == 'f':
    dist=(num * 3280.84)

elif unit1 == 'kilometers' or unit1 == 'km' and unit2 == 'meters' or unit2 == 'm':
    dist=(num * 1000)

elif unit1 == 'feet' or unit1 == 'f' and unit2 == 'miles' or unit2 == 'mi':
    dist=(num / 5280)

elif unit1 == 'feet' or unit1 == 'f' and unit2 == 'kilometers' or unit2 == 'km':
        dist=(num * 0.0003048)

elif unit1 == 'feet' or unit1 == 'f' and unit2 == 'meters' or unit2 == 'm':
        dist=(num / 3.28 )

elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'feet' or unit2 == 'f':
        dist=(num * 3.28 )

elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'miles' or unit2 == 'mi':
        dist=(num / 1,609.344)

elif unit1 == 'meters' or unit1 == 'm' and unit2 == 'kilometers' or unit2 == 'km':
        dist=(num / 1000)

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

print(dist , unit2)
print("conversion complete")
