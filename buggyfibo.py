"""
 Funcao fibonnaci teste0 pdb
"""


def fibo(value):
    res = list()
    a, b = 0, 1

    while b < value:
        res.append(b)
        a, b = b, a + b

    return res



def main():
    num = int(input("Digite o numero para a sequencia de fibonacci: "))
    import pdb; pdb.set_trace()
    fib = fibo(num)
    print(fib)


if __name__ == "__main__":
    main()
