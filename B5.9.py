import time


def time_this(num):
    def run(func):
        start = time.time()
        for _ in range(num):
            func()
        stop = time.time()
        print('Среднее время {} попыток: {} секунд'.format(num, (stop - start)/num))
        return func
    return run


@time_this(num=1000)
def main():
    for i in range(1000000):
        pass
    return False


if __name__ == '__main__':
    main()
