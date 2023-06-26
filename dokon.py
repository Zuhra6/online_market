# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
df = pd.read_excel('data.xlsx')

# print(df['Experence'].value_counts())
df_result = df
# df_result.drop(labels='bithday', axis=1, inplace=True)


df2 = df[df['first_name'] == 'Bella']
# print(df2)

df_result.drop(df2.index, inplace=True)
print(df_result[df_result['first_name'] == 'Bella'])
# df_result.to_excel('data_result.xlsx', index=False)

