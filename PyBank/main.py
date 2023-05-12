# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:11:39 2023

@author: Chioma Uche
"""

# Main for pybank

import csv
import numpy as np
#Open the file by calling open and then csv.DictReader.

input_file = csv.DictReader(open("C:\\Users\\Asabe Chioma\\OneDrive\\Desktop\\GITHUB\\python-challange\\PyBank\\Resources\\budget_data.csv"))
#ou may iterate over the rows of the csv file by iterating ove input_file. (Similarly to other files, you need to re-open the file if you want to iterate a second time.)


Dates = []
Money = []
for row in input_file:
#    print(row)
#    
#    print(row['Date']) 
#    print(row['Profit/Losses'])
    
    Dates.append(row['Date'])
    Money.append(int(row['Profit/Losses']))
    
    
    

#print(Dates) 
#print(Money)

total_months = len(Dates)

print('Financial Analysis')

print('--------------------------------------------')

print('Total Months: ' + str(total_months))

print('Total: $'+str(np.sum(Money)))

change_in_money = np.diff(Money)
print('Average Change: $'+str(np.mean(change_in_money)))

biggest_change_idx = np.argmax(change_in_money)

smallest_change_idx = np.argmin(change_in_money)
biggest_change_dates = np.argmax(Dates)
smallest_change_dates = np.argmin(Dates)
#print('Greatest Increase in Profits: ' +str(Dates[biggest_change_dates])  +str(change_in_money[biggest_change_idx]) )

#print('Greatest Decrease in Profits: '+str(Dates[smallest_change_dates])+str(change_in_money[smallest_change_idx] ))

#print('Greatest Increase in Profits: $'  +str(change_in_money[biggest_change_idx]) )

#print('Greatest Decrease in Profits: $' +str(change_in_money[smallest_change_idx] ))

print('Greatest Increase in Profits: ' +str(Dates[biggest_change_dates+1])  + " ($" + str(change_in_money[biggest_change_idx]) +")")

print('Greatest Decrease in Profits: '+str(Dates[smallest_change_dates+1]) + " ($" + str(change_in_money[smallest_change_idx] )+")")
#+1 was added to the change in date due to indexing problem