
import pandas as pd

df = pd.read_excel('data.xlsx')

df_result = df


df2 = df[df['first_name'] == 'Bella']


df_result.drop(df2.index, inplace=True)
print(df_result[df_result['first_name'] == 'Bella'])

