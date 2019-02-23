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

def type_check(num):
    # stringをintに変換する
    if type(num)=="str":
        return int(num)
    else:
        return num


def fizzbuzz_prod(num, cond_fizz=3, cond_buzz=5):

    num = type_check(num)

    cond_fizz = (num % cond_fizz ==0)
    cond_buzz = (num % cond_buzz ==0)
    cond_fizzbuzz = cond_fizz and cond_buzz

    if cond_fizzbuzz:
        return 'FizzBuzz'
    elif cond_buzz:
        return 'Buzz'
    elif cond_fizz:
        return 'Fizz'
    else:
        return num


if __name__ == '__main__':

    for num in range(1, 21):
        print(fizzbuzz_prod(num))
