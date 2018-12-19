def ex1():
    import numpy as np
    import matplotlib.pyplot as plt
    cy = []
    date = []
    d = 1
    with open('ex1.txt') as f:
        for item in f:
            date.append(d)
            cy.append(float(item))
            d += 1
    plt.plot(date, cy)
    plt.show()


def ex2():
    import numpy as np
    import matplotlib.pyplot as plt
    c1 = []
    c2 = []
    c3 = []
    date = []
    d = 1
    with open('ex2.txt') as ff:
        for item in ff:
            date.append(d)
            a, b, c = item.split()
            c1.append(float(a))
            c2.append(float(b))
            c3.append(float(c))
            d += 1
    plt.plot(date, c1, date, c2, date, c3)
    plt.show()


def ex3():
    import numpy as np
    import matplotlib.pyplot as plt
    c1 = []
    c2 = []
    c3 = []
    date = []
    d = 1
    with open('ex2.txt') as ff:
        for item in ff:
            date.append(d)
            a, b, c = item.split()
            c1.append(float(a))
            c2.append(float(b))
            c3.append(float(c))
            d += 1
    plt.plot(date, c1, date, c2, date, c3)
    plt.show()

    import numpy as np
    import matplotlib.pyplot as plt
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
    plt.xlabel(r'$date$')
    plt.ylabel(r'$course$')
    plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
    plt.grid(True)
    plt.show()


def ex4():
    print()

def ex5():
    print()

def ex6():
    print()

def ex7():
    print()

def ex8():
    print()

def ex9():
    print()

def ex10():
    print()

def ex11():
    print()

def ex12():
    print()

def ex13():
    print()

def main():
    num = int(input('Введите номер задачи: '))
    if num == 1:
        ex1()
    if num == 2:
        ex2()
    if num == 3:
        ex3()
    if num == 4:
        ex4()
    if num == 5:
        ex5()
    if num == 6:
        ex6()
    if num == 7:
        ex7()
    if num == 8:
        ex8()
    if num == 9:
        ex9()
    if num == 10:
        ex10()
    if num == 11:
        ex11()
    if num == 12:
        ex12()
    if num == 13:
        ex13()


if __name__ == "__main__":
    main()