import sys
import numpy


def calc(t, s):
    t = float(t)
    s = float(s)
    q = 2822 / pow(2*t + 22.8, 0.77)
    float(q)
    Q = q * 0.25 * s
    print('q为',q,"\n")
    print("计算流量为：", Q,"\n")


def times(cal, time):
    for i in range(20):
        a = sys.argv[1]


if __name__ == "__main__":
    while True:
          t = input("输入t2,单位为分钟")
          s = input("输入汇水面积")
          calc(t, s)

