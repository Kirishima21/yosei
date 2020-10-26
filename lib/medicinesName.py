import PySimpleGUI as sg
import pandas as pd

def add_medicines_name(data):
    df = pd.read_excel('data.xlsx', sheet_name=None)
    bool = not any(df["Sheet2"]["name"].str.contains(str(data)))
    if bool:
        df_add = pd.DataFrame([data], columns=['name'])
        df1 = df["Sheet1"]
        df2 = df["Sheet2"].append(df_add)
        with pd.ExcelWriter('data.xlsx') as writer:
            df1.to_excel(writer, sheet_name='Sheet1', index=False)
            df2.to_excel(writer, sheet_name='Sheet2', index=False, header="name")
        sg.popup("登録が完了しました。")
    else:
        sg.popup("登録済みの医薬品名です")
