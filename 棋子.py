


def setdanger(chess, x, y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col == x:
                chess[col][row] += 1
            elif row == y:
                chess[col][row] += 1
            elif col + row == x + y:
                chess[col][row] += 1
            elif col - row == x - y:
                chess[col][row] += 1
            else:
                pass


def erasedanger(chess, x, y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col == x:
                chess[col][row] -= 1
            elif row == y:
                chess[col][row] -= 1
            elif col + row == x + y:
                chess[col][row] -= 1
            elif col - row == x - y:
                chess[col][row] -= 1
            else:
                pass


def judgedanger(chess, col, row):
    if chess[col][row] != 0:
        return True
    else:
        return False


def judgecol(chess, col):
    for row in range(len(chess[col])):
        if judgedanger(chess, col, row):
            continue
        else:
            return True
    return False


def tryqueen(chess, col, flag, result):
    flag = True
    if col == 8:
        print(result)
        result = []
        flag = False
    else:
        if judgecol(chess, col):
            for row in range(len(chess[col])):
                if judgedanger(chess, col, row):
                    continue
                else:
                    setdanger(chess, col, row)
                    result.append((col, row))
                    tryqueen(chess, col + 1, flag, result)
                    if flag == True:
                        erasedanger(chess, col, row)
                        result.pop()
        else:
            pass


def main():
    chess = [[0 for x in range(8)] for x in range(8)]
    result = []
    flag = True
    tryqueen(chess, 0, flag, result)


if __name__ == "__main__":
    main()
