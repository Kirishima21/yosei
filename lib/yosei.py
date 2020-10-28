import PySimpleGUI as sg
import pandas as pd
import re

def add_yosei(data):
    count = 0
    index_count = 1
    df = pd.read_excel('data.xlsx', sheet_name=None)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    print("\n\n\n読み込まれたデータ")
    print(df1)

    df_add = pd.DataFrame({'患者名': [data["personal_name"]],
                           '来局予定日': [data["date"]],
                           '来局状態': ['未']},
                          index=['data'])

    while count < 40:
        medicine = {data[count]: data[count + 1]}
        index_name = "薬剤" + str(index_count)
        s = pd.DataFrame({index_name: str(medicine)}, index=['data'])
        df_add = pd.concat([df_add, s], axis=1)
        index_count += 1
        count += 2

    df1 = df1.append(df_add)

    with pd.ExcelWriter('data.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Sheet1', index=False, )
        df2.to_excel(writer, sheet_name='Sheet2', index=False, header="name")

    sg.popup("予製を登録しました")


def search_medicines_name(event, data):
    print(event)
    print(data)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(data[int(number)])

    df = pd.read_excel('data.xlsx', sheet_name=None)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df2[df2["name"].str.contains(data[int(number)])]

    for x in range(len(sdf["name"])):
        print(sdf["name"].values[x])

    return data