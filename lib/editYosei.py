import PySimpleGUI as sg
import pandas as pd
import re

def serch_human_name(value):


    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
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

def use_yosei_serch(value):

    if value[0] == '':
        sg.popup("空欄での決定はサポートされていません")
        return value

    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df1[df1["患者名"].str.contains(str(value[0]))]

    print(sdf)
    df1.at[str(value[0]), "来局状態"] = "済"

    with pd.ExcelWriter('data.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Sheet1', index='name', )
        df2.to_excel(writer, sheet_name='Sheet2', index='index', header="name")

    sg.popup("来局状態を「済」にしました")