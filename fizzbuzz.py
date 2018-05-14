

def fizzbuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    else:
        return str(num)


if __name__ == '__main__':

    for num in range(1, 21):
        print(fizzbuzz(num))
