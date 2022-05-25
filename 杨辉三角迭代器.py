def trans(n):
    cur_list = []
    global last_list
    if n == 0:
        cur_list = [1]
    if n == 1:
        cur_list = [1, 1]
    if n >= 2:
        for i in range(n + 1):
            if i == 0 or i == n:
                cur_list.append(1)
            else:
                cur_list.append(last_list[i] + last_list[i - 1])
    last_list = cur_list
    yield cur_list


def generator(x):
    for i in range(x):
        a = trans(i)
        print(next(a))


last_list = []
generator(10)
