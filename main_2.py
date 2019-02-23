import sys
import csv
import pandas as pd

def get_csv(filename):
    f = open(filename)
    line = f.readline()

    df = []
    while line:
        line = f.readline()
        df.append(line.replace('\n','').split(","))
    f.close()
    return df

def get_dataframe(csv_filename):
    data_list = get_csv("input/0.csv")
    df = pd.DataFrame(index=[], columns=["ID","Mathematics","Science","English","Japanese","History","Geography"])

    for num in range(len(data_list)-1):
        series = pd.Series(data_list[num], index=df.columns)
        df = df.append(series, ignore_index=True)
    return df

def check_dropout(df):
    df.loc[(df["Mathematics"] <= 49)]

def main(argv):

    df = get_dataframe("input/0.csv")

    print(df)


if __name__ == '__main__':
    main(sys.argv[1:])
