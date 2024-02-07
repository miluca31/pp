# chicken has 2 legs x = chicken
# rabbit has 4 legs  y = rabbit
heads = 35
legs = 94

def solve(numheads, numlegs):
    rabbit = (numlegs / 2) - numheads
    chicken = numheads - rabbit
    print("chickens : ", int(chicken))
    print("rabbits : ", int(rabbit))

solve(heads, legs)