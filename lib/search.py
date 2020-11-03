import PySimpleGUI as sg
import pandas as pd
import re


def suggestion_medicines_name_searchPage(data):
    # データベースを読み込む
    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    # 入力されているデータの文字列をデータベースから検索し該当するデータだけのテーブルを作る
    print(data["medicines_name"])
    sdf = df2[df2["name"].str.contains(data["medicines_name"])]
    suggestion = {}
    for x in range(len(sdf["name"])):
        suggestion[x] = sdf["name"].values[x]
    return {
        "data": data,
        "suggestion": suggestion,
    }


def decision_medicines_name_searchPage(event, data_dic):
    # 何番目の薬品決定ボタンが押されたのかを把握する
    print(event)
    print(data_dic)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(data_dic["suggestion"][int(number)])

    # 辞書型のデータから予製データを切り出す処理
    data = data_dic["data"]
    # 入力されたデータを元にサーチで渡された予製薬剤番号 number に サジェストナンバーから薬品名を予製データに上書きする処理
    data["medicines_name"] = data_dic["suggestion"][int(number)]
    print("更新されたデータ")
    print(data)

    return data


def serch_human_name_searchPage(data):
    # データベースを読み込む
    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    # 入力されているデータの文字列をデータベースから検索し該当するデータだけのテーブルを作る
    print(data["human_name"])
    sdf = df1[df1["患者名"].str.contains(data["human_name"])]
    sdf = sdf[~sdf["患者名"].duplicated()]
    suggestion = {}
    for x in range(len(sdf["患者名"])):
        suggestion[x] = sdf["患者名"].values[x]

    print(suggestion)

    return {
        "data": data,
        "suggestion": suggestion,
    }

def decision_human_name_searchPage(event, data_dic):
    # 何番目の薬品決定ボタンが押されたのかを把握する
    print(event)
    print(data_dic)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(data_dic["suggestion"][int(number)])

    # 辞書型のデータから予製データを切り出す処理
    data = data_dic["data"]
    # 入力されたデータを元にサーチで渡された予製薬剤番号 number に サジェストナンバーから薬品名を予製データに上書きする処理
    data["human_name"] = data_dic["suggestion"][int(number)]
    print("更新されたデータ")
    print(data)

    return data