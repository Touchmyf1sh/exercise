class Infectors:
    def __init__(self, Infected_day, days):
        self.Infected_day = Infected_day
        self.days = days
        self.heal_day = 0

    def infect(self):
        if self.days - self.Infected_day < 14:
            if int(int(self.days - self.Infected_day) % 5) == 0 and int(self.days - self.Infected_day) != 0:
                Infect(self.days, self.days)
        else:
            pass
        pass

    def heal(self):
        global infected_people
        global healer_people
        if int(self.days - self.Infected_day) == 14:
            self.heal_day = self.days
        elif self.days - self.Infected_day > 14:
            if self.days - self.heal_day == 10:
                infected_people -= 1
                healer_people += 1
            else:
                pass
        else:
            pass


def Main_Loop(target_day):
    global infected_people
    global healer_people
    global days
    infected_list.append(Infectors(1, 1))
    for i in range(target_day + 1):
        for c in infected_list:
            c.days = days
            c.infect()
            c.heal()
            if c.days - c.heal_day == 10:
                del c
        for d in temp_list:
            infected_list.append(d)
        temp_list.clear()
        days += 1
    print("现有感染人数： ", infected_people)
    print("现已治愈人数： ", healer_people)
    print(len(infected_list))


def Infect(Infected_day, days):
    global infected_people
    infected_people += 2
    for i in range(2):
        temp_list.append(Infectors(Infected_day, days))


if __name__ == "__main__":
    days = 1
    infected_people = 1
    healer_people = 0
    infected_list = []
    temp_list = []
    Main_Loop(29)
