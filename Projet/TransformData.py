from Import import *

df['SugarProCal'] = df['Sugars']/(1 + df['Calories'])
del df['Sodium']
del df['SatFat']

print(df.columns.values)
