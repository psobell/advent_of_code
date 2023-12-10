# ( = up one floor
# ) = down one floor
# 1: what floor does he end up on?
# 2: at which step does he first arrive at the basement?


CUR_FLOOR = 0
NUM = 0

with open('input_1.txt') as fle:
    inp = fle.read()

entered_basement = False
for floor in inp:
    NUM += 1
    if floor == '(':
        CUR_FLOOR += 1
    elif floor == ')':
        CUR_FLOOR -= 1
    if CUR_FLOOR == -1 and entered_basement is False:
        print('the first time he enters the basement is on step ' + str(NUM))
        entered_basement = True
print('the answer is ' + str(CUR_FLOOR))
