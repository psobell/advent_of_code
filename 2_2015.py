# Part 1: The elves need to order exactly enough wrapping paper based on length(l),
# width (w), and height (h) of each present.
# For each present, they need 2*l*w + 2*w*h + 2*h*l + (area of the
# smallest side) square feet of paper.  How much should they order?
# Part 2: the elves need to order exactly enough ribbon.  The amount they will
# need is equal to the perimeter of the smallest face of each present, plus
# the volume of each present.


def create_lst():
    presents = [[]]
    ind = 0
    cur_num = ''
    with open('input_2.txt') as fle:
        inp = fle.read()  # lxwxh on each line
    for char in inp:
        if char != '\n' and char != 'x':
            cur_num += char
        if char == 'x':
            presents[ind].append(cur_num)
            cur_num = ''
        if char == '\n':
            presents[ind].append(cur_num)
            presents.append([])
            ind += 1
            cur_num = ''
    presents.pop()
    for pres in presents:
        for ind in range(len(pres)):
            pres[ind] = int(pres[ind])
    return presents


def find_total(presents):
    paper = 0
    ribbon = 0
    for pres in presents:
        l = pres[0]
        w = pres[1]
        h = pres[2]
        smallest_area = (l * w * h)/max(l,w,h)
        smallest_peri = (l + w + h - max(l,w,h)) * 2
        paper += (2*l*w + 2*w*h + 2*h*l + smallest_area)
        ribbon += smallest_peri + l*w*h
    return (paper, ribbon)

print('paper: ' + str(find_total(create_lst())[0]) + '\nribbon: '
      + str(find_total(create_lst())[1]))
