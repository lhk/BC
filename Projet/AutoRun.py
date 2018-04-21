import sys, os

li = ['Calories', 'TotalFat', 'TransFat', 'SatFat', 'Sodium', 'Carbohydrates', 'Cholesterol', 'Fibre', 'Sugars', 'Protein', 'VitaminA', 'VitaminC', 'Calcium', 'Iron']

n = len(li)

for i in range(0, n): 
    for j in range(i+1, n): 
        os.system('python Visualize.py '+ li[i] + ' '+ li[j])

