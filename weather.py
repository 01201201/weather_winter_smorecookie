import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def calculate_snow_and_temperature():
    user_input_date_str = entry.get()
   
    try:
        user_input_date = datetime.strptime(user_input_date_str, "%m-%d")
    except ValueError:
        messagebox.showerror("에러", "올바른 날짜 형식을 입력하세요 (예: 12-25)")
        return

    future_rows = df[df.apply(lambda row: datetime.strptime(row['날짜'].strip(), "%m-%d") == user_input_date, axis=1)]

    if not future_rows.empty:
        snow_probability = future_rows['눈 O/X'].mean()
        result_label.config(text=f"{user_input_date_str}에 눈이 올 확률: {snow_probability:.2%}")

        average_temperature = future_rows['평균기온'].mean()
        temperature_label.config(text=f"{user_input_date_str}의 평균 기온: {average_temperature:.2f} °C")
    else:
        result_label.config(text=f"{user_input_date_str}에 대한 데이터가 없습니다.")
        temperature_label.config(text="")

excel_file_path = '겨울.xlsx'

sheet_names = ['2018', '2019', '2020', '2021', '2022']

dfs = [pd.read_excel(excel_file_path, sheet_name=sheet) for sheet in sheet_names]

df = pd.concat(dfs, ignore_index=True)

window = tk.Tk()
window.title("날씨 예측 프로그램:서울의 눈")

window.geometry("630x280")

label = tk.Label(window, text="겨울(입동-입춘)에 해당하는 5개년(2018-2022) 날씨 데이터를 분석하여 제작한 날씨 예측 프로그램입니다.")
label.pack(pady=20)

label = tk.Label(window, text="기간에 해당하는 날짜를 입력해 주세요. (11-07 ~ 02-03)")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="확인하기", command=calculate_snow_and_temperature)
button.pack(pady=10)
 
result_label = tk.Label(window, text="")
result_label.pack(pady=5)
 
temperature_label = tk.Label(window, text="")
temperature_label.pack(pady=5)
 
window.mainloop()
