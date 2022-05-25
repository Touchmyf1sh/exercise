import random


class Tcomputer:
    def __init__(self):
        self.all_possible = []
        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    for l in range(1, 10):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            ans = 1000 * i + 100 * j + 10 * k + l
                            self.all_possible.append(ans)

    def __numcheck(self, all_possible, mac_num, correct_num):
        list_mac_num = list(str(mac_num))
        re_list = []
        for every_num in all_possible:
            checknum = 0
            for ever_word in list(str(every_num)):
                if ever_word in list_mac_num:
                    checknum += 1
            if checknum == correct_num:
                re_list.append(every_num)
        return re_list

    def __positioncheck(self, all_possible, mac_num, correct_num):
        mac_str = str(mac_num)
        re_list = []
        for every_num in all_possible:
            checknum = 0
            for i in range(4):
                if str(every_num)[i] == mac_str[i]:
                    checknum += 1
            if checknum == correct_num:
                re_list.append(every_num)
        return re_list

    def getinfo(self, has_info, pos_info):
        self.has_info = has_info
        self.pos_info = pos_info

    def printnum(self):
        if self.has_info == 'ok':
            self.cur_num = random.choice(self.all_possible)
        else:
            self.all_possible = self.__numcheck(self.all_possible, self.cur_num, self.has_info)
            self.all_possible = self.__positioncheck(self.all_possible, self.cur_num, self.pos_info)
            self.cur_num = random.choice(self.all_possible)
        return self.cur_num


if __name__ == '__main__':
    computer = Tcomputer()
    print('是否准备猜数？')
    while True:
        try:
            value = input("人：")
            loop_time = 0
            if value == 'ok':
                loop_time += 1
                computer.getinfo(value, '')
                print('计算机:' + str(computer.printnum()))
            elif value == 'yes':
                print('got it')
                break
            else:
                computer.getinfo(int(value.split(',')[0]), int(value.split(',')[1]))
                print('计算机：' + str(computer.printnum()))
        except [ValueError, IndexError]:
            raise '请输入正确数字'
        except TypeError:
            raise '请输入ok以开始'
