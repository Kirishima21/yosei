import PySimpleGUI as sg

def layout_master(page, data):

# 最初のページ
    if page == "first":
        layout = [
            [sg.Text('予製を管理するソフトウェアです。\n\n・医薬品名を登録する場合は「薬品名を登録する」\n\n・予製を登録する場合は「予製を登録する」\n\n・予製から検索を行う場合は「検索をする」\n\nを押してください。')],
            [sg.Button('薬品名を登録する', key='add_medicines_name_page'),sg.Button('予製を登録する', key='add_yosei_page'),sg.Button('検索をする', key='search_page')]
        ]

# 医薬品登録関連のレイアウト

    # 医薬品登録ページのレイアウト
    if page == "add_medicines_name_page":
        layout = [
            [sg.Text('このページでは薬品名を登録することが出来ます。')],
            [sg.Text('医薬品名 剤型 規格 メーカー', size=(15, 1)), sg.InputText('○○○○錠△△mg「メーカー」')],
            [sg.Button('薬品名の入力を確認する', key='check_add_medicines_name'),sg.Button('戻る', key='back_first_page')]
        ]

    # 医薬品登録ページのレイアウト
    if page == "re_check_the_name_of_the_medicines":
        layout = [
            [sg.Text('このページでは薬品名を登録することが出来ます。')],
            [sg.Text('医薬品名 剤型 規格 メーカー', size=(15, 1)), sg.InputText(data)],
            [sg.Button('薬品名の入力を確認する', key='check_add_medicines_name'), sg.Button('戻る', key='back_first_page')]
        ]

    # 医薬品登録の確認ページのレイアウト
    if page == "check_the_name_of_the_medicines":
        show_message = "薬剤名　" + data + '　が登録されます。よろしいですか？\n'
        layout = [
            [sg.Text(show_message)],
            [sg.Button('薬品名を登録する', key='add_medicines_name'), sg.Button('再度入力しなおす', key='back_check_add_medicines_name_page'), sg.Button('戻る', key='back_first_page')]
        ]

# 予製登録関連のレイアウト

    # 予製登録ページのレイアウト
    elif page == "re_add_yosei_page":
        layout = [
            [sg.Text('このページでは予製を登録することが出来ます。')],
            [sg.Text('患者名', size=(10, 1)), sg.InputText(data["personal_name"], key ="personal_name")],
            [sg.Text('来局予定日', size=(10, 1)), sg.InputText(data["date"], key = "date")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[0]), sg.Button('検索', key='search_0'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[1])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[2]), sg.Button('検索', key='search_2'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[3])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[4]), sg.Button('検索', key='search_4'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[5])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[6]), sg.Button('検索', key='search_6'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[7])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[8]), sg.Button('検索', key='search_8'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[9])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[10]), sg.Button('検索', key='search_10'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[11])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[12]), sg.Button('検索', key='search_12'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[13])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[14]), sg.Button('検索', key='search_14'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[15])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[16]), sg.Button('検索', key='search_16'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[17])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[18]), sg.Button('検索', key='search_18'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[19])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[20]), sg.Button('検索', key='search_20'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[21])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[22]), sg.Button('検索', key='search_22'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[23])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[24]), sg.Button('検索', key='search_24'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[25])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[26]), sg.Button('検索', key='search_26'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[27])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[28]), sg.Button('検索', key='search_28'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[29])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[30]), sg.Button('検索', key='search_30'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[31])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[32]), sg.Button('検索', key='search_32'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[33])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[34]), sg.Button('検索', key='search_34'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[35])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[36]), sg.Button('検索', key='search_36'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[37])],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[38]), sg.Button('検索', key='search_38'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[39])],
            [sg.Button('予製を登録する', key='add_yosei'),sg.Button('戻る', key='back_first_page')]
        ]

    elif page == "add_yosei_page":
        layout = [
            [sg.Text('このページでは予製を登録することが出来ます。')],
            [sg.Text('患者名', size=(10, 1)), sg.InputText('テストさん', key ="personal_name")],
            [sg.Text('来局予定日', size=(10, 1)), sg.InputText('11月29日', key = "date")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText('フェブリク'), sg.Button('検索', key='search_0'), sg.Text('錠数', size=(5, 1)), sg.InputText('28')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText('ブロチゾラム'), sg.Button('検索', key='search_2'), sg.Text('錠数', size=(5, 1)), sg.InputText('28')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_4'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_6'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_8'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_10'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_12'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_14'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_16'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_18'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_20'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_22'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_24'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_26'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_28'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_30'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_32'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_34'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_36'), sg.Text('錠数', size=(5, 1)), sg.InputText('')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText('アトルバスタチン'), sg.Button('検索', key='search_38'), sg.Text('錠数', size=(5, 1)), sg.InputText('28')],
            [sg.Button('予製を登録する', key='add_yosei'),sg.Button('戻る', key='back_first_page')]
        ]

# 検索ページ関連のレイアウト

    # 検索ページのレイアウト
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