def ex1():
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
    import matplotlib.pyplot as plt
    currency1 = []
    currency2 = []
    currency3 = []
    date = []
    d = 1
    with open('ex2.txt') as ff:
        for item in ff:
            date.append(d)
            a, b, c = item.split()
            currency1.append(float(a))
            currency2.append(float(b))
            currency3.append(float(c))
            d += 1
    plt.plot(date, currency1, date, currency2, date, currency3)
    plt.show()


def ex3():
    import matplotlib.pyplot as plt
    currency1 = []
    currency2 = []
    currency3 = []
    date = []
    d = 1
    with open('ex2.txt') as ff:
        for item in ff:
            date.append(d)
            a, b, c = item.split()
            currency1.append(float(a))
            currency2.append(float(b))
            currency3.append(float(c))
            d += 1
    plt.plot(date, currency1, date, currency2, date, currency3)
    plt.xlabel(r'$date$')
    plt.ylabel(r'$currency$')
    plt.title(r'$f_1(date)=currency1(date),\ f_2(date)=currency2(date),\ f_3(date)=currency3(date)$')
    plt.grid(True)
    plt.show()


def ex4():
    import matplotlib.pyplot as plt
    currency1 = []
    currency2 = []
    currency3 = []
    date = []
    d = 1
    with open('ex2.txt') as ff:
        for item in ff:
            date.append(d)
            a, b, c = item.split()
            currency1.append(float(a))
            currency2.append(float(b))
            currency3.append(float(c))
            d += 1

    # subplot 1
    plt.subplot(221)
    plt.plot(date, currency1)
    plt.ylabel(r'$currency$')
    plt.title(r'$f_1(date)=currency1(date)$')
    plt.grid(True)

    # subplot 2
    plt.subplot(222)
    plt.plot(date, currency2, 'g')
    plt.ylabel(r'$currency$')
    plt.title(r'$f_2(date)=currency2(date)$')
    plt.grid(True)

    # subplot 3
    plt.subplot(223)
    plt.plot(date, currency3, 'r')
    plt.ylabel(r'$currency$')
    plt.title(r'$f_3(date)=currency3(date)$')
    plt.grid(True)

    plt.show()


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
    import matplotlib.pyplot as plt

    data = [1036.4, 1500]
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Diagram', size=15)
    plt.pie(data, labels=('USD/RUB', 'EUR/RUB'))
    plt.show()


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