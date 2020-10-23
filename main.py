# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PySimpleGUI as sg

def layout_master(page,data):

    if page == "first":
        layout = [
            [sg.Text('予製を管理するソフトウェアです。\n\n・医薬品名を登録する場合は「薬品名を登録する」\n\n・予製を登録する場合は「予製を登録する」\n\n・予製から検索を行う場合は「検索をする」\n\nを押してください。')],
            [sg.Button('薬品名を登録する', key='add_medicines_name_page'),sg.Button('予製を登録する', key='add_yosei_page'),sg.Button('検索をする', key='search_page')]
        ]
    elif page == "add_medicines_name_page":
        layout = [
            [sg.Text('このページでは薬品名を登録することが出来ます。')],
            [sg.Text('医薬品名 剤型 規格 メーカー', size=(15, 1)), sg.InputText('○○○○錠△△mg「メーカー」')],
            [sg.Button('薬品名の入力を確認する', key='check_add_medicines_name'),sg.Button('戻る', key='back_first_page')]
        ]
    elif page == "re_check_the_name_of_the_medicines":
        layout = [
            [sg.Text('このページでは薬品名を登録することが出来ます。')],
            [sg.Text('医薬品名 剤型 規格 メーカー', size=(15, 1)), sg.InputText(data)],
            [sg.Button('薬品名の入力を確認する', key='check_add_medicines_name'), sg.Button('戻る', key='back_first_page')]
        ]
    elif page == "add_yosei_page":
        layout = [
            [sg.Text('このページでは予製を登録することが出来ます。')],
            [sg.Text('来局予定日', size=(10, 1)), sg.InputText('20XX年XX月XX日')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Button('予製を登録する', key='add_medicines_name'),sg.Button('戻る', key='back_first_page')]
        ]
    elif page == "check_the_name_of_the_medicines":
        show_message = "薬剤名　" + data + '　が登録されます。よろしいですか？\n'
        layout = [
            [sg.Text(show_message)],
            [sg.Button('薬品名を登録する', key='add_medicines_name'), sg.Button('再度入力しなおす', key='back_check_add_medicines_name_page'), sg.Button('戻る', key='back_first_page')]
        ]
    elif page == "search_page":
        layout = [
            [sg.Text('このページでは登録されているデータから検索が出来ます。\n')],
            [sg.Text('\n人の名前を検索する')],
            [sg.InputText(''),sg.Button('人の名前を検索', key='back_first_page')],
            [sg.Text('\n医薬品名を検索する')],
            [sg.InputText(''), sg.Button('医薬品名を検索する', key='back_first_page')],
            [sg.Text('\n来局予定日を検索する')],
            [sg.InputText(''), sg.Button('来局予定日を検索する', key='back_first_page')],
        ]

    return layout


def simple_gui():
    sg.theme('DarkTeal7')

    page_name = "first"
    data = ""

    layout = layout_master(page_name, data)
    window = sg.Window('予製を管理するツール', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:  # ウィンドウのXボタンを押したときの処理
            break

        if event == "add_medicines_name_page":
            page_name = "add_medicines_name_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名を登録するページ', layout)

        if event == "add_medicines_name":
            sg.popup("登録が完了しました。")

        if event == "add_yosei_page":
            page_name = "add_yosei_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を登録するページ', layout)

        if event == "check_add_medicines_name":
            data = values[0]
            page_name = "check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        if event == "back_check_add_medicines_name_page":
            page_name = "re_check_the_name_of_the_medicines"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('薬品名の入力を確認する画面', layout)

        if event == "back_first_page":
            page_name = "first"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('予製を管理するツール', layout)

        if event =="search_page":
            page_name = "search_page"
            layout = layout_master(page_name, data)
            window.close()
            window = sg.Window('検索ページ', layout)


    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simple_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
