import PySimpleGUI as sg

def layout_master(page, data):

# 最初のページ
    if page == "first":
        layout = [
            [sg.Text('予製を管理するソフトウェアです。\n\n・医薬品名を登録する場合は「薬品名を登録する」\n\n・予製を登録する場合は「予製を登録する」\n\n・来局状況の登録を行う場合は「予製を管理する」\n\n・予製から検索を行う場合は「検索をする」\n\nを押してください。')],
            [sg.Button('薬品名を登録する', key='add_medicines_name_page'),sg.Button('予製を登録する', key='add_yosei_page'),sg.Button('予製を管理する', key='edit_yosei_page'),sg.Button('検索をする', key='search_page')]
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
            [sg.Text('患者名', size=(10, 1)), sg.InputText(data["personal_name"], key ="personal_name"), sg.Button('人名検索', key='suggestion_human_name'), sg.Text('前回処方を呼び出す', size=(15, 1)), sg.Button('Do', key='do')],
            [sg.Text('来局予定日', size=(10, 1)), sg.InputText(data["date"], key = "date"), sg.Text('処方日数', size=(7, 0)), sg.InputText(data["days"], key='days'), sg.Button('処方日数から計算', key='calculation')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[0]), sg.Button('検索', key='search_0'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[1]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_1"], size=(3, 1), key ="calculation_1")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[2]), sg.Button('検索', key='search_2'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[3]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_3"], size=(3, 1), key ="calculation_3")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[4]), sg.Button('検索', key='search_4'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[5]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_5"], size=(3, 1), key ="calculation_5")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[6]), sg.Button('検索', key='search_6'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[7]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_7"], size=(3, 1), key ="calculation_7")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[8]), sg.Button('検索', key='search_8'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[9]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_9"], size=(3, 1), key ="calculation_9")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[10]), sg.Button('検索', key='search_10'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[11]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_11"], size=(3, 1), key ="calculation_11")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[12]), sg.Button('検索', key='search_12'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[13]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_13"], size=(3, 1), key ="calculation_13")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[14]), sg.Button('検索', key='search_14'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[15]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_15"], size=(3, 1), key ="calculation_15")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[16]), sg.Button('検索', key='search_16'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[17]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_17"], size=(3, 1), key ="calculation_17")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[18]), sg.Button('検索', key='search_18'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[19]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_19"], size=(3, 1), key ="calculation_19")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[20]), sg.Button('検索', key='search_20'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[21]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_21"], size=(3, 1), key ="calculation_21")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[22]), sg.Button('検索', key='search_22'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[23]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_23"], size=(3, 1), key ="calculation_23")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[24]), sg.Button('検索', key='search_24'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[25]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_25"], size=(3, 1), key ="calculation_25")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[26]), sg.Button('検索', key='search_26'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[27]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_27"], size=(3, 1), key ="calculation_27")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[28]), sg.Button('検索', key='search_28'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[29]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_29"], size=(3, 1), key ="calculation_29")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[30]), sg.Button('検索', key='search_30'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[31]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_31"], size=(3, 1), key ="calculation_31")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[32]), sg.Button('検索', key='search_32'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[33]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_33"], size=(3, 1), key ="calculation_33")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[34]), sg.Button('検索', key='search_34'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[35]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_35"], size=(3, 1), key ="calculation_35")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[36]), sg.Button('検索', key='search_36'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[37]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_37"], size=(3, 1), key ="calculation_37")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(data[38]), sg.Button('検索', key='search_38'), sg.Text('錠数', size=(5, 1)), sg.InputText(data[39]), sg.Text('一日量', size=(6, 1)), sg.InputText(data["calculation_39"], size=(3, 1), key ="calculation_39")],
            [sg.Button('予製を登録する', key='add_yosei'), sg.Button('戻る', key='back_first_page')]
        ]

    elif page == "add_yosei_page":
        layout = [
            [sg.Text('患者名', size=(10, 1)), sg.InputText('', key ="personal_name"), sg.Button('人名検索', key='suggestion_human_name'), sg.Text('前回処方を呼び出す', size=(15, 1)), sg.Button('Do', key='do')],
            [sg.Text('来局予定日', size=(10, 1)), sg.InputText('', key = "date"), sg.Text('処方日数', size=(7, 0)), sg.InputText('', key='days'), sg.Button('処方日数から計算', key='calculation')],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_0'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_1")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_2'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_3")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_4'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_5")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_6'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_7")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_8'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_9")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_10'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_11")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_12'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_13")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_14'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_15")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_16'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_17")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_18'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_19")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_20'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_21")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_22'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_23")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_24'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_25")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_26'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_27")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_28'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_29")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_30'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_31")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_32'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_33")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_34'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_35")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_36'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_37")],
            [sg.Text('薬剤名', size=(5, 1)), sg.InputText(''), sg.Button('検索', key='search_38'), sg.Text('錠数', size=(5, 1)), sg.InputText(''), sg.Text('一日量', size=(6, 1)), sg.InputText('', size=(3, 1), key ="calculation_39")],
            [sg.Button('予製を登録する', key='add_yosei') ,sg.Button('戻る', key='back_first_page')]
        ]

    elif page == "choosing_medicine":
        print(data)
        layout = []
        layout += [sg.Text('このページでは医薬品を選択します。')],
        for x in range(len(data["suggestion"])):
            print(data["suggestion"][x])
            key = "decision_" + str(x)
            layout += [sg.Text(str(data["suggestion"][x])), sg.Button('決定', key=key)],
        layout += [sg.Button('入力画面に戻る', key='re_back_yosei')],

    elif page == "suggestion_human_name":
        print(data)
        layout = []
        layout += [sg.Text('このページでは登録する患者名を選択します。')],
        for x in range(len(data["suggestion"])):
            print(data["suggestion"][x])
            key = "decision_human_" + str(x)
            layout += [sg.Text(str(data["suggestion"][x])), sg.Button('決定', key=key)],
        layout += [sg.Button('入力画面に戻る', key='re_back_yosei')],

    elif page == "edit_yosei_page":
        layout = [
            [sg.Text('このページでは予製の使用状況を管理します。\nこのページで患者さんの来局により使用済みとなった予製を登録することが出来ます')],
            [sg.Text('\n来局患者の名前で検索する')],
            [sg.InputText(''), sg.Button('人名検索', key='serch_human_name'),sg.Button('来局情報を更新して来局済みにします', key='use_yosei_serch')],
            [sg.Button('戻る', key='back_first_page')]
        ]

    elif page == "re_edit_yosei_page":
        layout = [
            [sg.Text('このページでは予製の使用状況を管理します。\nこのページで患者さんの来局により使用済みとなった予製を登録することが出来ます')],
            [sg.Text('\n来局患者の名前で検索する')],
            [sg.InputText(str(data)), sg.Button('人名検索', key='serch_human_name'),sg.Button('来局情報を更新して来局済みにします', key='use_yosei_serch')],
            [sg.Button('戻る', key='back_first_page')]
        ]

    elif page == "choosing_human_name":
        print(data)
        layout = []
        layout += [sg.Text('このページでは来局した患者さんの名前を選択します。')],
        for x in range(len(data)):
            print(data[x])
            key = "human_name_" + str(x)
            layout += [sg.Text(str(data[x])), sg.Button('決定', key=key)],
        layout += [sg.Button('入力画面に戻る', key='re_back_edit_yosei_page')],

# 検索ページ関連のレイアウト

    # 検索ページのレイアウト
    elif page == "search_page":
        layout = [
            [sg.Text('このページでは登録されているデータから検索が出来ます。\n')],
            [sg.Text('\n人の名前を検索する')],
            [sg.InputText('', key='human_name'), sg.Button('検索', key='suggestion_human_name_searchPage'), sg.Button('人の名前を検索', key='search_yosei_human_name_searchPage')],
            [sg.Text('\n医薬品名を検索する')],
            [sg.InputText('', key='medicines_name'), sg.Button('検索', key='suggestion_medicines_name_searchPage'), sg.Button('医薬品名を検索する', key='search_yosei_medicines_searchPage')],
            [sg.Text('\n来局予定日を検索する')],
            [sg.InputText('', key='search_date'), sg.Button('来局予定日を検索する', key='search_yosei_date_searchPage')],
            [sg.Button('戻る', key='back_first_page')],
        ]

    elif page == "re_search_page":
        layout = [
            [sg.Text('このページでは登録されているデータから検索が出来ます。\n')],
            [sg.Text('\n人の名前を検索する')],
            [sg.InputText(data["human_name"], key='human_name'), sg.Button('検索', key='suggestion_human_name_searchPage'), sg.Button('人の名前を検索する', key='search_yosei_human_name_searchPage')],
            [sg.Text('\n医薬品名を検索する')],
            [sg.InputText(data["medicines_name"], key='medicines_name'), sg.Button('検索', key='suggestion_medicines_name_searchPage'), sg.Button('医薬品名を検索する', key='search_yosei_medicines_searchPage')],
            [sg.Text('\n来局予定日を検索する')],
            [sg.InputText(data["search_date"], key='search_date'), sg.Button('来局予定日を検索する', key='search_yosei_date_searchPage')],
            [sg.Button('戻る', key='back_first_page')],
        ]

    elif page == "choosing_medicines_name_searchPage":
        print(data)
        layout = []
        layout += [sg.Text('このページでは医薬品を選択します。')],
        for x in range(len(data["suggestion"])):
            print(data["suggestion"][x])
            key = "searchPage_medicinesName_decision_" + str(x)
            layout += [sg.Text(str(data["suggestion"][x])), sg.Button('決定', key=key)],
        layout += [sg.Button('入力画面に戻る', key='re_back_search_page')],

    elif page == "choosing_human_name_searchPage":
        print(data)
        layout = []
        layout += [sg.Text('このページでは検索する患者名を選択します。')],
        for x in range(len(data["suggestion"])):
            print(data["suggestion"][x])
            key = "searchPage_humanName_decision_" + str(x)
            layout += [sg.Text(str(data["suggestion"][x])), sg.Button('決定', key=key)],
        layout += [sg.Button('入力画面に戻る', key='re_back_search_page')],


    return layout