import PySimpleGUI as sg
import pandas as pd
import re

def serch_human_name(value):


    df = pd.read_excel('data.xlsx', sheet_name=None)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df1[df1["患者名"].str.contains(str(value))]
    print(sdf)
    sdf = sdf[sdf["来局状態"].str.contains("未")]
    print(sdf)
    suggestion = {}
    for x in range(len(sdf["患者名"])):
        suggestion[x] = sdf["患者名"].values[x]
    print(suggestion)
    return suggestion

def decision_human_name(event , suggestion_dic):
    # 何番目の薬品決定ボタンが押されたのかを把握する
    print(event)
    print(suggestion_dic)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(suggestion_dic[int(number)])

    return suggestion_dic[int(number)]