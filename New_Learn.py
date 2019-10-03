from pandas import read_csv, DataFrame

ROOT : str = "C:\\Users\\Samarth\\Desktop\\"
loc1 : str = ROOT + "GLOBEMeasurementData-12037.csv"
loc2 : str = ROOT + "GLOBEMeasurementData-12034.csv"
loc3 : str = ROOT + "GLOBEMeasurementData-12041.csv"
# loc4 : str = ROOT +
loc_final : str = ROOT + "Data_Combined_1.csv"

df1 : DataFrame = read_csv(filepath_or_buffer = loc1, encoding = "utf-8")
df2 : DataFrame = read_csv(filepath_or_buffer = loc2, encoding = "utf-8")
df3 : DataFrame = read_csv(filepath_or_buffer = loc3, encoding = "utf-8")
# df4 : DataFrame = read_csv(filepath_or_bufferv = "", encoding = "utf-8")

# df_comnbined : DataFrame = DataFrame(index = range())  # TODO
# all_ids : list = list(set(df1[""].unique().to_list() + df1[""].unique().to_list() + df1[""].unique().to_list() +
#                           df1[""].unique().to_list()))
#
# for id in all_ids :

df_comnbined : DataFrame = df1.join(df2, on = ["organization_id"], how = "outer")\
                                .join(df3, on = ["organization_id"], how = "outer")\
                                # .join(df4, on = ["organization_id"], how = "outer", lsuffix = "left_3_", rsuffix = "right_3_")

print(len(df_comnbined.columns))
df_comnbined.dropna(axis = 1, how = "all", inplace = True)
print(len(df_comnbined.columns))

print(len(df_comnbined))
# df_comnbined.dropna(thresh = 5, inplace = True)
# print(len(df_comnbined))

df_comnbined.to_csv(path_or_buf = loc_final, index = False, encoding = "utf-8")

# There are no rows with > 5 nas
import pandas as pd

df = pd.read_csv("C:\\Users\\Samarth\\Desktop\\Data_Combined.csv")
print(df)

