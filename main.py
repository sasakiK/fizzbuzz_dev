import sys

def split_input(args):

    arg = args.split(":")
    return arg[0], arg[1]

def main(argv):

    # check restrinctions
    # rest1 1≤m≤5, 整数
    if len(argv) >6 or len(argv) <= 0:
        raise ValueError("invalid input")

    # store input pairs
    arg_list = []
    for input in range(len(argv)-1):
        arg_list.append(split_input(argv[input]))

    # store input num
    input_num = argv[-1]

    # check restrinctions
    # rest2 1≤s[i].length≤50, 文字列
    for num in range(len(argv)-1):
        if len(arg_list[num][1]) >= 50:
            raise ValueError("invalid input")

    # check restrinctions
    # rest3,4 1≤a[i]≤100, 整数
    for num in range(len(argv)-1):
        spec_num = arg_list[num][0]
        if spec_num[0]=="0":
            raise ValueError("invalid input")
        if (int(spec_num) > 100 or int(spec_num) <= 0):
            raise ValueError("invalid input")

    # check restrinctions
    # rest5 全ての a[i]a[i] は異なる
    a_list = []
    for num in range(len(argv)-1):
        a_list.append(arg_list[num][0])
    a_list_unique = list(set(a_list))
    if len(a_list_unique) != len(a_list):
        raise ValueError("invalid input")

    # check restrinctions
    # rest6 a[i] と s[i]s[i] には:とを含まない






if __name__ == '__main__':
    main(sys.argv[1:])
