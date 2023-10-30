from sqlalchemy import inspect
from sqlalchemy import create_engine
from Appsetting import GetAppSetting
import pandas as pd
import os.path

appsetting = GetAppSetting()
engine = create_engine(appsetting.serverEnv.prod)
path = "Export Table.xlsx"
try:
    inspector = inspect(engine)
    table_List = inspector.get_table_names()
    print(table_List)
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    for index in range(len(table_List)):
        datalist = []
        # print(f"\n================ TABLE {table_List[index]} ================\n")
        columns_list = inspector.get_columns(table_List[index])
        for col in range(len(columns_list)):
            if columns_list[col].get("autoincrement") is not None:
                datalist.append([columns_list[col]["name"], columns_list[col]["type"], columns_list[col]["default"], columns_list[col]["comment"], columns_list[col]["nullable"], columns_list[col]["autoincrement"]])
                df1 = pd.DataFrame(datalist, columns=['name', 'type', 'default', 'comment', 'nullable', 'autoincrement'])
            else:
                datalist.append([columns_list[col]["name"], columns_list[col]["type"], columns_list[col]["default"], columns_list[col]["comment"], columns_list[col]["nullable"], None])
                df1 = pd.DataFrame(datalist, columns=['name', 'type', 'default', 'comment', 'nullable', 'autoincrement'])

        df1.to_excel(writer, sheet_name=table_List[index])

        # print(f"\n================END OF TABLE {table_List[index]} ================\n")

    writer.close()

except AssertionError as error:
    print(error)
