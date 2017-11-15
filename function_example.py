import random

def calc_road_trip_time(miles, mph):
    """
    takes in miles and mph, divides to return trip duration
    """
    return miles / mph

# output = calc_road_trip_time(150, 25)
#
# print(output)

def randomscream():
    """
    creates a scream based on random elements
    """
    Atext = "a" * random.randint(1,16)
    Htext = "h" * random.randint(1,16)
    msg = Atext + Htext
    return msg

def main():
    output = randomscream()
    print(output)

main()
