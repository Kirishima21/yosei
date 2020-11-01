import PySimpleGUI as sg
import pandas as pd
import re

def add_yosei(data):

    #必要な関数の初期化
    count = 0
    index_count = 1
    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    #重複登録を防ぐ為の処理
    if not any(df1["患者名"].str.contains(str(data["personal_name"]))):
        #新患者の登録をするときの処理
        sg.popup("新患でまちがいないですか？")
    else:
        #ヒットした患者のみのテーブルを作る処理
        sdf = df1[df1["患者名"].str.contains(data["personal_name"])]

        if any(sdf["来局状態"].str.contains('未')):
            #ヒットした患者名のうち来局状況が未の物があるときは登録させない。
            sg.popup("重複登録の可能性があります。")
            return

    print("\n\n\n読み込まれたデータ")
    print(df1)

    #データを登録する為の加工処理 患者名、来局予定日、来局状態
    df_add = pd.DataFrame({'患者名': [data["personal_name"]],
                           '来局予定日': [data["date"]],
                           '処方日数': [data["days"]],
                           '来局状態': ['未']},
                          index=[data["personal_name"]])

    #ループ処理を使って 医薬品名 錠数 分幾つ の3つの情報を一つの辞書型にする処理
    while count < 40:
        name = "calculation_" + str(count + 1)
        medicine = '"' + data[count] + '", ' + '"' +  data[count + 1] + '", ' + '"' +  data[name] + '"'
        index_name = "薬剤" + str(index_count)
        s = pd.DataFrame({index_name: str(medicine)}, index=[data["personal_name"]])
        df_add = pd.concat([df_add, s], axis=1)
        index_count += 1
        count += 2

    #加工したデータ群をテーブルに乗せる
    df1 = df1.append(df_add)

    #上乗せされたデータを保存する
    with pd.ExcelWriter('data.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Sheet1', index='name', )
        df2.to_excel(writer, sheet_name='Sheet2', index='index', header="name")

    sg.popup("予製を登録しました")


def search_medicines_name(event, data):

    #何番の検索ボタンが押されたのかを把握する
    print(event)
    print(data)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(data[int(number)])

    #データベースを読み込む
    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    #入力されているデータの文字列をデータベースから検索し該当するデータだけのテーブルを作る
    sdf = df2[df2["name"].str.contains(data[int(number)])]
    suggestion = {}
    for x in range(len(sdf["name"])):
        suggestion[x] = sdf["name"].values[x]
    return {
        "data": data,
        "suggestion": suggestion,
        "number": number
    }

def decision_medicines_name(event, data_dic):

    #何番目の薬品決定ボタンが押されたのかを把握する
    print(event)
    print(data_dic)
    number = re.findall('\d+', event)
    number = number[0]
    print(number)
    print(data_dic["suggestion"][int(number)])

    #辞書型のデータから予製データを切り出す処理
    data = data_dic["data"]
    #入力されたデータを元にサーチで渡された予製薬剤番号 number に サジェストナンバーから薬品名を予製データに上書きする処理
    data[int(data_dic["number"])] = data_dic["suggestion"][int(number)]
    print("更新されたデータ")
    print(data)

    return data

def calculation(data):

    count = 1

    if data["days"] == '':
        sg.popup("空欄のままでの実行はできません")
        return data

    while count < 41:
        key = "calculation_" + str(count)
        print(key)
        print(data[str(key)])

        if data[str(key)] == '':
            count += 2
        else:
            data[count] = int(data[str(key)]) * int(data["days"])
        print(data[count])
        count += 2

    return data