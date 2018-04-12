from Import import *

df['SugarProCal'] = df['Sugars']/(1 + df['Calories'])
df['SodSug'] = df['Sodium'] + df['Sugars']

print(df[0:3])
