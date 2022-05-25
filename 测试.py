class test:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __del__(self):
        del self

    def add(self):
        for i in range(2):
            lista.append(test(2))

    def delete(self):
        del self


if __name__ == "__main__":
    lista = []
    a = test(3)
    a.add()
    print(len(lista))
    for i in lista:
        print(i)
    for i in lista:
        i.delete()
        print("现在剩下：", len(lista))
    print(len(lista))
    for i in lista:
        print("现在：", i)
