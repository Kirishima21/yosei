import PySimpleGUI as sg
import pandas as pd
import re

# 各種設定ファイルのロード
from layout.layout import layout_master
from lib.medicinesName import add_medicines_name
from lib.yosei import *
from lib.editYosei import *
from lib.search import *
from lib.readData import *


def simple_gui():
    # 各種設定の初期化
    sg.theme('DarkTeal7')
    page_name = "first"
    data = ""

    # レイアウトの設定を呼び出す
    layout = layout_master(page_name, data)

    # 初期ウィンドの生成
    window = sg.Window('予製を管理するツール', layout)

    # イベントループ
    while True:
        event, values = window.read()

        # ウィンドウのXボタンを押したときの処理
        if event == sg.WIN_CLOSED:
            page_name = "exit"
            data = {}
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('確認画面', layout)

        elif event == "yes_exit":
            sg.popup("data.xlsxをは全てのデータが保存されている重要なファイルです。定期的にバックアップを行ってください。")
            break

        elif event == "no_exit":
            page_name = "first"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するツール', layout)

    # 初期ページ関連の処理

        # 初期ページで薬品名を登録するボタンを押したときの処理
        elif event == "add_medicines_name_page":
            page_name = "add_medicines_name_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名を登録するページ', layout)

        # 初期ページで予製を登録するボタンを押したときの処理
        elif event == "add_yosei_page":
            page_name = "add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を登録するページ', layout)

        elif event == "edit_yosei_page":
            page_name = "edit_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するページ', layout)

        # 初期ページで検索を押したときの処理
        elif event == "search_page":
            page_name = "search_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('検索ページ', layout)

    # 医薬品登録ページ関連の処理

        # 医薬品登録ページで医薬品名を入力後確認ボタンを押した時の処理
        elif event == "check_add_medicines_name":
            data = values[0]
            page_name = "check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        # 確認ページから再度編集画面に戻る為の処理
        elif event == "back_check_add_medicines_name_page":
            page_name = "re_check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        # 医薬品名の登録をしたときの処理
        elif event == "add_medicines_name":
            add_medicines_name(data)

        # 予製登録ページ関連の処理

        # 予製を登録するボタンを押したときの処理
        elif event == "add_yosei":
            data = values
            print(values)

            add_yosei(data)

        # 予製登録関連では複数の返り値をやり取りするために辞書型の返り値を採用している
        # 混同を防ぐため変数の中身が辞書になっているものは name_dic とする事
        # 辞書型のデータ型の中身は問わないが予製データについては必ず data をキーにすること

        # 予製登録ページで薬品名をサジェストするためのボタンを押したときの処理
        elif re.match('search_\d+', event):
            number = re.findall('\d+', event)
            number = number[0]
            data = values
            if data[int(number)] == "":
                sg.popup("空欄での検索はサポートされていません")
            else:
                data_dic = search_medicines_name(event, data)
                page_name = "choosing_medicine"
                layout = layout_master(page_name, data_dic)
                window.close()
                window = sg.Window('薬品名を検索する画面', layout)

        # サジェスト画面で薬品名を選択した時の処理
        elif re.match('decision_\d+', event):
            data = decision_medicines_name(event, data_dic)
            page_name = "re_add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        # サジェスト画面で予製登録ページに戻る為の処理
        elif event == "re_back_yosei":
            page_name = "re_add_yosei_page"
            data = data_dic["data"]
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        elif event == "suggestion_human_name":
            page_name = "suggestion_human_name"
            data = values
            data_dic = suggestion_human_name(data)
            layout = layout_master(page_name, data_dic)
            window.close()
            window = sg.Window('患者名の入力を確認する画面', layout)

        elif re.match('decision_human_\d+', event):
            data = decision_human_name_yosei(event, data_dic)
            page_name = "re_add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        elif event == "do":
            data = values
            data = recall(data)
            page_name = "re_add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

    # 予製管理ページ関連の処理

        # 人名サジェストボタンの処理
        elif event == "serch_human_name":
            suggestion_dic = serch_human_name(values[0])
            page_name = "choosing_human_name"
            layout = layout_master(page_name, suggestion_dic)
            window.close()
            window = sg.Window('患者さんの名前を選択する画面', layout)

        elif event == "re_back_edit_yosei_page":
            page_name = "edit_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するページ', layout)

        elif re.match('human_name_\d', event):
            human_name = decision_human_name(event, suggestion_dic)
            page_name = "re_edit_yosei_page"
            layout = layout_master(page_name, human_name)
            window.close()
            window = sg.Window('予製を管理するページ', layout)

        elif event == "use_yosei_serch":
            print(values)
            use_yosei_serch(values)

        elif event == "calculation":
            data = values
            data = calculation(data)
            page_name = "re_add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

    # 検索ページ関連の処理

        elif event == "suggestion_medicines_name_searchPage":
            data = values
            if data["medicines_name"] == "":
                sg.popup("空白での検索はサポートされていません")
            else:
                data_dic = suggestion_medicines_name_searchPage(data)
                page_name = "choosing_medicines_name_searchPage"
                layout = layout_master(page_name, data_dic)
                window.close()
                window = sg.Window('薬品名を検索する画面', layout)

            # サジェスト画面で薬品名を選択した時の処理
        elif re.match('searchPage_medicinesName_decision_\d+', event):
            data = decision_medicines_name_searchPage(event, data_dic)
            page_name = "re_search_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        elif event == "re_back_search_page":
            page_name = "re_search_page"
            # data = suggestion_dic["data"]
            # data = data_dic["data"]
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        elif event == "suggestion_human_name_searchPage":
            data = values
            suggestion_dic = serch_human_name_searchPage(data)
            page_name = "choosing_human_name_searchPage"
            layout = layout_master(page_name, suggestion_dic)
            window.close()
            window = sg.Window('患者さんの名前を選択する画面', layout)

        elif re.match('searchPage_humanName_decision_\d+', event):
            data = decision_human_name_searchPage(event, suggestion_dic)
            page_name = "re_search_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        elif event == "search_yosei_medicines_searchPage":
            data = values
            view_data = view_yosei_medicines(data)
            sg.popup(view_data)

        elif event == "search_yosei_human_name_searchPage":
            data = values
            view_data = view_yosei_human_name(data)
            sg.popup(view_data)

        elif event == "search_yosei_date_searchPage":
            data = values
            view_data = view_yosei_date(data)
            sg.popup(view_data)

        elif event == "output":
            read_data()

    # 前ページ共通の処理

        # 最初のページに戻る為の処理
        elif event == "back_first_page":
            page_name = "first"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するツール', layout)

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simple_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
