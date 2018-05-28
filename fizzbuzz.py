# Author      : sasaki k
# reference   : http://inokara.hateblo.jp/entry/2017/10/01/153513


def fizzbuzz(num):

    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


if __name__ == '__main__':

    for num in range(1, 21):
        print(fizzbuzz(num))
