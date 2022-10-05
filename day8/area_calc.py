import math
def paint_calc(test_h,test_w,coverage):
    test_h=int(input("enter the height"))
    test_w=int(input("enter the width"))
    coverage=5
    number_of_can=math.ceil((test_h*test_w)/coverage)
    print(f'you will need {number_of_can} cans of paint')
paint_calc("test_h","test_w","coverage")