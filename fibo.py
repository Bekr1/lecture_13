
def recursive_nth_fibo(n):
    """
    Fce vrátí Fibonacciho posloupnosti pomocí D&C
    :param n: (int) n-tý prvek, který chceme zjistit
    :return: (int) n-tý prvek posloupnosti
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    n = int(input("Zadejte počet prvků posloupnosti: "))
    posl = [recursive_nth_fibo(i) for i in range(n)]
    print(posl)


if __name__ == '__main__':
    main()
