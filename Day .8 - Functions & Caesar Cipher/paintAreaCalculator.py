import math

def areaCalc(h, w, cov):
    cans = math.ceil((h*w)/cov)
    print(f"You'll need {cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

areaCalc(test_h, test_w, coverage)



