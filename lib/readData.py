import PySimpleGUI as sg
import pandas as pd
import re
import time
import datetime

def read_data():

    df = pd.read_excel('data.xlsx', sheet_name=None, index_col=0)
    df1 = df["Sheet1"]
    df2 = df["Sheet2"]

    sdf = df1[df1["来局状態"].str.contains("未")]
    dic = sdf.to_dict(orient='index')
    sdf_count = 0

    out_put_dic = {}

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

        print(recall)

        dic_count = 0

        while dic_count < 39:

            if recall[0] == "":
                dic_count += 2
                continue
            elif recall[int(dic_count)] in out_put_dic:
                bool_check = recall[dic_count + 1].isdecimal()
                if bool_check:
                    out_put_dic[recall[int(dic_count)]] = int(out_put_dic[recall[int(dic_count)]]) + int(recall[dic_count + 1])
                dic_count += 2
                continue
            else:
                bool_check = recall[dic_count + 1].isdecimal()
                if bool_check:
                    out_put_dic[recall[int(dic_count)]] = int(recall[dic_count + 1])
                dic_count += 2
                continue

        sdf_count += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(out_put_dic)

    text = ""
    for k, v in out_put_dic.items():
        text += str(k) + ":" + str(v) + "\n"

    now = datetime.datetime.now()
    path_w = "output" + now.strftime("%Y%m%d") + ".txt"

    with open(path_w, mode='w') as f:
        f.write(text)