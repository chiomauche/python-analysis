# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:11:39 2023

@author: Chioma Uche
"""

# Main for pypoll

import csv
import numpy as np
#Open the file by calling open and then csv.DictReader.

input_file = csv.DictReader(open("C:\\Users\\Asabe Chioma\\OneDrive\\Desktop\\Starter_Code\\PyBank\\Resources\\budget_data.csv"))
#ou may iterate over the rows of the csv file by iterating ove input_file. (Similarly to other files, you need to re-open the file if you want to iterate a second time.)


ID = []
County = []
Candidates = []
for row in input_file:
#    print(row)
#    
#    print(row['Date']) 
#    print(row['Profit/Losses'])
    
    ID.append(int(row['Ballot ID']))
    County.append(row['County'])
    Candidates.append(row['Candidate'])
    
print('Election Results')

print('--------------------------------------------')

print('Total Votes:',len(ID))

print('--------------------------------------------')

#print(np.unique(Candidates))
each_candidate = np.unique(Candidates)


#for i in range(len(ID)):
#    if Candidates[i] == 'Charles Casper Stockham':
#        Charles += 1
#    elif Candidates[i] == 'Diana DeGette':
#        Diana += 1
#    elif Candidates[i] == 'Raymon Anthony Doane':
#        Raymon += 1
#        
FinalCount = np.zeros(len(each_candidate))
for i in range(len(ID)):
     for c in range(len(each_candidate)):
         if Candidates[i] == each_candidate[c]:
            FinalCount[c] += 1    
         
#        if Candidates[i] == 'Charles Casper Stockham':
#            Charles += 1
#        elif Candidates[i] == 'Diana DeGette':
#            Diana += 1
#        elif Candidates[i] == 'Raymon Anthony Doane':
#            Raymon += 1

#print(FinalCount[1],each_candidate[1])

            
for c in range(len(each_candidate)):
    #print(c)
    print('')
    print(each_candidate[c] + ': ' + str(FinalCount[c]/len(ID)*100) + '% (' + str(FinalCount[c]) + ')')

print('--------------------------------------------')
#FinalCount= [Charles, Diana, Raymon]

winner_index = np.argmax(FinalCount)
#print(winner_index)

print('Winner:',each_candidate[winner_index])

print('--------------------------------------------')
#    
#    
#
#print(Dates) 
#print(Money)
#
#total_months = len(Dates)
#print('Total Months: ' + str(total_months))
#
#print('Total: $',np.sum(Money))
#
#change_in_money = np.diff(Money)
#print('Average Change: $', np.mean(change_in_money))
#
#biggest_change_idx = np.argmax(change_in_money)
#
#smallest_change_idx = np.argmin(change_in_money)
#
#
#print('Greatest Increase in Profits: ',change_in_money[biggest_change_idx] )
#print('Greatest Decrease in Profits: ',change_in_money[smallest_change_idx] )