import PySimpleGUI as sg
import pandas as pd

# 各種設定ファイルのロード
from layout.layout import layout_master


def simple_gui():

    # 各種設定の初期化
    sg.theme('DarkTeal7')
    page_name = "first"
    data = ""

    # レイアウトの設定を呼び出す
    layout = layout_master(page_name, data)

    # 初期ウィンドの生成
    window = sg.Window('予製を管理するツール', layout)

    #イベントループ
    while True:
        event, values = window.read()

        # ウィンドウのXボタンを押したときの処理
        if event == sg.WIN_CLOSED:
            break


    # 初期ページ関連の処理

        # 初期ページで薬品名を登録するボタンを押したときの処理
        if event == "add_medicines_name_page":
            page_name = "add_medicines_name_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名を登録するページ', layout)

        # 初期ページで予製を登録するボタンを押したときの処理
        if event == "add_yosei_page":
            page_name = "add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を登録するページ', layout)

        # 初期ページで検索を押したときの処理
        if event == "search_page":
            page_name = "search_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('検索ページ', layout)


    # 医薬品登録ページ関連の処理

        # 医薬品登録ページで医薬品名を入力後確認ボタンを押した時の処理
        if event == "check_add_medicines_name":
            data = values[0]
            page_name = "check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        # 確認ページから再度編集画面に戻る為の処理
        if event == "back_check_add_medicines_name_page":
            page_name = "re_check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        # 医薬品名の登録をしたときの処理
        if event == "add_medicines_name":
            df = pd.read_excel('data.xlsx', sheet_name=None)
            bool = not any(df["Sheet2"]["name"].str.contains(str(data)))
            if bool:
                df_add = pd.DataFrame([data], columns=['name'])
                df1 = df["Sheet1"]
                df2 = df["Sheet2"].append(df_add)
                with pd.ExcelWriter('data.xlsx') as writer:
                    df1.to_excel(writer, sheet_name='Sheet1', index = False)
                    df2.to_excel(writer, sheet_name='Sheet2', index=False, header="name")
                sg.popup("登録が完了しました。")
            else:
                sg.popup("登録済みの医薬品名です")


    # 前ページ共通の処理

        # 最初のページに戻る為の処理
        if event == "back_first_page":
            page_name = "first"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するツール', layout)

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simple_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
