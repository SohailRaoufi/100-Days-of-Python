import math
def paint_calc(height , width , cover):
    res = (height * width) / cover
    res = math.ceil(res)
    print(f"you'll need {res} cans of paint.")






test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)