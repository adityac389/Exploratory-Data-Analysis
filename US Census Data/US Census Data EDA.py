# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


#Importing the data and concatinating into one DataFrame
files = glob.glob("states*.csv")

states_list = []
for filename in files:
    data = pd.read_csv(filename)
    states_list.append(data)

us_census = pd.concat(states_list)


#Viweing the Dataframe
print(us_census.columns)
print(us_census.dtypes)
print(us_census)


## Cleaning the Dataframe

# Turning Income Column into a numercial type
for index in range(0,len(us_census["Income"])):
    string = str(us_census['Income'].iat[index])
    replace_dol = string.replace('$', '')
    replace_com = replace_dol.replace(',', '')
    us_census['Income'].iat[index] = replace_com

us_census["Income"] = pd.to_numeric(us_census['Income'])


# Splitting the GenderPop column

Men = []
Women = []
for index in range(0,len(us_census["GenderPop"])):
    string = str(us_census['GenderPop'].iat[index])
    replace = string.split('_')
    Men.append(replace[0])
    Women.append(replace[1])

us_census['Men'] = Men
us_census['Women'] = Women


# Converting the Populations into a numerical type

for index in range(0,len(us_census["Men"])):
    string = str(us_census['Men'].iat[index])
    replace = string.replace('M', '')
    us_census['Men'].iat[index] = replace
    
for index in range(0,len(us_census["Women"])):
    string = str(us_census['Women'].iat[index])
    replace = string.replace('F', '')
    us_census['Women'].iat[index] = replace
    
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])


# Converting Race Percentage into a numerical type

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    for index in range(0,len(us_census)):
        string = str(us_census[race].iat[index])
        replace = string.replace('%', '')
        if replace == "nan":
            replace = ""
        us_census[race].iat[index] = replace
    us_census[race] = pd.to_numeric(us_census[race])


# Calulating Women Population in states where Women Population = nan

us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])


# Calulating Hispanic Population Percentage in states where Hispanic Population Percentage = nan

us_census['Pacific'] = us_census['Pacific'].fillna(100 - us_census['Hispanic'] - us_census['White'] - us_census['Black'] - us_census['Native'] - us_census['Asian'])


#Checking any duplicates in the Dataframe

print(us_census.duplicated(subset = us_census.columns[1:]))


# Dropping Duplicates

census = us_census.drop_duplicates(subset = us_census.columns[1:])


## EDA

# Histograms of Races

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.hist(census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()

# Scatter Plot of Income VS. Population By Gender Per State


WI = plt.scatter(census['Women'], census['Income'])
MI = plt.scatter(census['Men'], census['Income'])
plt.title("Scatter Plot of Income vs. Population by Gender per State")
plt.xlabel("Population by Gender per State")
plt.ylabel("Income ($)")
plt.legend((WI, MI),('Womens','Mens'), scatterpoints=1, loc='lower right', ncol=3, fontsize=8)
plt.show()
plt.clf()