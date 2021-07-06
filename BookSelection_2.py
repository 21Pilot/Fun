"""
Created on Tue Jul  6 03:41:54 2021

@author: floraseo

The purpose of this code is to analyze the csv file that features the 100 book
that I read last year. 

"""
#%%
import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt

#%%
# Load csv file 
filename = '/Users/floraseo/Downloads/BookSelection_2.csv';
fields = [];
rows = [];

with open (filename, 'r' ) as csvfile:
    csvreader = csv.reader(csvfile);
    fields = next(csvreader);
    
    for row in csvreader:
        rows.append(row)
    # Show the book identities in the csv file
    print('Book identities are:'+','.join(field for field in fields[:5]))
    
df = pd.read_csv(filename)
# Change the index to start from 1 instead of 0
df.index = np.arange(1,len(df)+1);
# Show data in chart
df

#%%
# Sort and find the number of authors and nationalties 
def sort(name,fields):
    df = pd.read_csv(name)
    df.sort_values(fields, inplace =True)
    df.drop_duplicates(subset= fields, inplace=True)
    df_count = len(df)
    print(df_count)
    return df


author_count = len(sort(filename,"Author"));
nation_count = len(sort(filename, "Nationality"));
length_count = (sort(filename,"Length"));

print('The number of authors in the list is:', author_count) 
print('The number of different nationality in the list is:', nation_count)
print('The length of books are divided into:',list(length_count["Length"]))

# Sort to get the range of published years min and max
def sort_year(name, fields):
    df = pd.read_csv(name)
    df.sort_values(fields, inplace=True)
    df.drop_duplicates(subset=fields, inplace=True)
    df_min = df[fields].min()
    df_max = df[fields].max()
    return df_min,df_max

year_range = sort_year(filename, "Published Year");

print('The range of the published year of the books list is', year_range)
#%%
# Show the list of authors, nationalities and year without overlap
def show_list(name,fields):
    df = pd.read_csv(name)
    df.sort_values(fields, inplace =True)
    df.drop_duplicates(subset= fields, inplace=True)
    list(df)
    return df

author_list = show_list(filename, "Author")
nation_list = show_list(filename, "Nationality")
year_list = show_list(filename, "Published Year")

# Show only the specific column value
print(author_list["Author"],nation_list["Nationality"]
      ,year_list["Published Year"])

#%%
# Count Freuquency of each author,nationality and length 
def freq_count(x=fields, y = fields, z = fields):
    freq = df.set_index([x,y]).count(level=y)
    return freq 

author_freq = freq_count("Title","Author","Nationality")
nation_freq = freq_count("Title","Nationality","Author")
length_freq = freq_count("Title","Length","Author")

print(author_freq["Nationality"],nation_freq["Published Year"]
      ,length_freq["Author"])

#%%
# Plot - Author
# figsize = 10,15 to manage the graphs 
plt.figure(figsize = (10,15))
plt.barh(author_list["Author"],author_freq["Nationality"])
# Show the number of each bar at the end 
for index, value in enumerate(author_freq["Nationality"]):
    plt.text(value, index,str(value))
plt.xlabel('Frequency', fontsize=10)
plt.ylabel('Authors',fontsize =10)
plt.title('Book frequency for each author: Top 3: Haruki, Kundera/Werber,and Oe'
          ,fontsize=13)

# Plot - Nationality 
plt.figure()
plt.barh(nation_list["Nationality"],nation_freq["Author"])
# Show the number of each bar at the end 
for index, value in enumerate(nation_freq["Author"]):
    plt.text(value, index, str(value))
plt.xlabel('Frequency', fontsize=10)
plt.ylabel('Nationality',fontsize =10)
plt.suptitle('Book frequency for each nationality', fontsize=10)
plt.title('Top 3: Japanese, American, and French', fontsize=8)

# Plot - Length
plt.figure()
plt.barh(length_count["Length"],length_freq["Author"])
# Show the number of each bar at the end 
for index, value in enumerate(length_freq["Author"]):
    plt.text(value, index, str(value))
plt.xlabel('Frequency', fontsize=10)
plt.ylabel('Length',fontsize =10)
plt.suptitle('Book frequency for each length', fontsize=10)
plt.title('Long>350, 350<Medium<200, 200<Short', fontsize=8)
