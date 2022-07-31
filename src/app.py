import pandas as pd 
#import dotenv
#from dotenv import load_dotenv
#import os

#load_dotenv()

#url_data_set = os.environ.get('url_data_set')
#no pude instalar dotenv !
# 
 
url_data_set = 'https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv'
df = pd.read_csv(url_data_set)

#Data Preprocessing

df['reviews_per_month'].fillna(0,inplace = True)
df['name'].fillna("$",inplace=True)
df['host_name'].fillna("#",inplace=True)
df.drop(['last_review'],axis=1,inplace=True)

df.to_csv("../data/procesdded/AB_NYC_clean.csv")

#No me esta dejando grabar por este error.
#  File "/home/gitpod/.pyenv/versions/3.8.13/lib/python3.8/site-packages/pandas/io/common.py", line 568, in check_parent_directory
#    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
#OSError: Cannot save file into a non-existent directory: '../data/procesdded'