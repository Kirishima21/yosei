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


def view_yosei_medicines(data):
    print(data)
    popup_text = ""
    if data["medicines_name"] =="":
        popup_text += "空白での検索は出来ません"
        return popup_text

    # データベースを読み込む
    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df1[df1["来局状態"].str.contains("未")]
    dic = sdf.to_dict(orient='index')
    sdf_count = 0
    print("データのロードを開始します")

    while sdf_count < len(dic):
        print(sdf.iloc[sdf_count, 0])
        value = sdf.iloc[sdf_count, 0]
        print(sdf[sdf["患者名"].str.contains(value)])

        recall = {}

        recall["personal_name"] = sdf["患者名"].values[sdf_count]
        recall["date"] = sdf["来局予定日"].values[sdf_count]
        recall["days"] = sdf["処方日数"].values[sdf_count]
        if str(recall["days"]) == "nan":
            recall["days"] = ""
        count = 1
        index_count = 0

        while count < 21:
            key = "薬剤" + str(count)
            cell = sdf[key].values[sdf_count]
            count += 1
            cell = re.findall('"([^"]*)"', cell)
            recall[index_count] = cell[0]
            recall[index_count + 1] = cell[1]
            recall["calculation_" + str(index_count + 1)] = cell[2]
            index_count += 2

        print(data["medicines_name"] in recall.values())
        if data["medicines_name"] in recall.values():
            keys = [k for k, v in recall.items() if v == data["medicines_name"]]
            print(keys)
            print(data["medicines_name"] + "は" + recall["personal_name"] + "に" + str(recall[int(keys[0]) + 1]) + "入っています\n")
            popup_text += "・" + data["medicines_name"] + "は" + str(recall["date"]) + "に来局予定になっている  " + recall["personal_name"] + "  さんの予製に  " + str(recall[int(keys[0]) + 1]) + "  錠、入っています\n"

        print(recall)

        sdf_count += 1

    return popup_text

def view_yosei_human_name(data):
    print(data)
    popup_text = ""
    if data["human_name"] == "":
        popup_text += "空白での検索は出来ません"
        return popup_text

    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df1[df1["患者名"].str.contains(data["human_name"])]
    sdf = sdf[~sdf["患者名"].duplicated(keep='last')]
    recall = {}

    recall["personal_name"] = sdf["患者名"].values[0]
    recall["date"] = sdf["来局予定日"].values[0]
    recall["days"] = sdf["処方日数"].values[0]
    recall["来局状態"] = sdf["来局状態"].values[0]
    if str(recall["days"]) == "nan":
        recall["days"] = ""
    print(recall)
    count = 1
    index_count = 0

    while count < 21:
        key = "薬剤" + str(count)
        cell = sdf[key].values[0]
        count += 1
        cell = re.findall('"([^"]*)"', cell)
        recall[index_count] = cell[0]
        recall[index_count + 1] = cell[1]
        recall["calculation_" + str(index_count + 1)] = cell[2]
        index_count += 2
    print(recall)

    popup_text = recall["personal_name"] + "さんの予製には\n\n"

    count = 0
    while count < 40:
        if recall[count] == "":
            count += 2
            continue
        text = "・" + recall[count] + "  が  " + recall[count + 1] + "  錠(包)\n"
        popup_text += text
        count += 2

    text = "\n来局予定日は" + str(recall["date"]) + "になっています\n"
    popup_text += text

    if recall["来局状態"] == "未":
        popup_text += "\nこの予製は使用されていません"
    else:
        popup_text += "\nこの予製は使用済みです"

    return popup_text

def view_yosei_date(data):
    popup_text = ""
    if data["search_date"] == "":
        popup_text += "空白での検索は出来ません"
        return popup_text

    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    if type(df1["来局予定日"].values[0]) == "str":
        sdf = df1[df1["来局予定日"].str.contains(data["search_date"])]
    else:
        search = data["search_date"]
        sdf = df1[df1["来局予定日"].isin([str(data["search_date"])])]

    sdf = sdf[~sdf["患者名"].duplicated(keep='last')]
    print(sdf)
    dic = sdf.to_dict(orient='index')
    sdf_count = 0

    popup_text += str(data["search_date"]) + "には\n\n"
    while sdf_count < len(dic):
        popup_text += sdf["患者名"].values[sdf_count] + " さん\n"
        sdf_count += 1
    popup_text += "\nが来局予定になっています"

    return popup_text