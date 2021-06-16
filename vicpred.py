# -*- coding: utf-8 -*-
"""VicPred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XqVoJezgruvcTwciA95SZED7eQw38xlS
"""

import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
df = pd.read_csv('matches.csv')

#ONLY TAKING THE TEAMS THAT ARE REGULAR
consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Daredevils', 'Sunrisers Hyderabad']
df = df[(df['team1'].isin(consistent_teams)) & (df['team2'].isin(consistent_teams))]

#FILLING NULL VALUES
conditions = [df["venue"] == "Rajiv Gandhi International Stadium, Uppal",df["venue"] == "Maharashtra Cricket Association Stadium",
              df["venue"] == "Saurashtra Cricket Association Stadium", df["venue"] == "Holkar Cricket Stadium",
              df["venue"] == "M Chinnaswamy Stadium",df["venue"] == "Wankhede Stadium",
              df["venue"] == "Eden Gardens",df["venue"] == "Feroz Shah Kotla",
              df["venue"] == "Punjab Cricket Association IS Bindra Stadium, Mohali",df["venue"] == "Green Park",
              df["venue"] == "Punjab Cricket Association Stadium, Mohali",df["venue"] == "Dr DY Patil Sports Academy",
              df["venue"] == "Sawai Mansingh Stadium", df["venue"] == "MA Chidambaram Stadium, Chepauk", 
              df["venue"] == "Newlands", df["venue"] == "St George's Park" , 
              df["venue"] == "Kingsmead", df["venue"] == "SuperSport Park",
              df["venue"] == "Buffalo Park", df["venue"] == "New Wanderers Stadium",
              df["venue"] == "De Beers Diamond Oval", df["venue"] == "OUTsurance Oval", 
              df["venue"] == "Brabourne Stadium",df["venue"] == "Sardar Patel Stadium", 
              df["venue"] == "Barabati Stadium", df["venue"] == "Vidarbha Cricket Association Stadium, Jamtha",
              df["venue"] == "Himachal Pradesh Cricket Association Stadium",df["venue"] == "Nehru Stadium",
              df["venue"] == "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",df["venue"] == "Subrata Roy Sahara Stadium",
              df["venue"] == "Shaheed Veer Narayan Singh International Stadium",df["venue"] == "JSCA International Stadium Complex",
              df["venue"] == "Sheikh Zayed Stadium",df["venue"] == "Sharjah Cricket Stadium",
              df["venue"] == "Dubai International Cricket Stadium",df["venue"] == "M. A. Chidambaram Stadium",
              df["venue"] == "Feroz Shah Kotla Ground",df["venue"] == "M. Chinnaswamy Stadium",
              df["venue"] == "Rajiv Gandhi Intl. Cricket Stadium" ,df["venue"] == "IS Bindra Stadium",df["venue"] == "ACA-VDCA Stadium"]
values = ['Hyderabad', 'Mumbai', 'Rajkot',"Indore","Bengaluru","Mumbai","Kolkata","Delhi","Mohali","Kanpur","Mohali","Pune","Jaipur","Chennai","Cape Town","Port Elizabeth","Durban",
          "Centurion",'Eastern Cape','Johannesburg','Northern Cape','Bloemfontein','Mumbai','Ahmedabad','Cuttack','Jamtha','Dharamshala','Chennai','Visakhapatnam','Pune','Raipur','Ranchi',
          'Abu Dhabi','Sharjah','Dubai','Chennai','Delhi','Bengaluru','Hyderabad','Mohali','Visakhapatnam']
df['city'] = np.where(df['city'].isnull(),
                              np.select(conditions, values),
                              df['city'])

#Removing records having null values in "winner" column
df=df[df["winner"].notna()]

#REMOVING USELESS COLS
columns_to_remove = ['id', 'date', 'result', 'dl_applied', 'win_by_runs', 'win_by_wickets', 'player_of_match', 'umpire1', 'umpire2', 'umpire3']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

#NUMERICALLY CATEGORIZING THE FEATURES
encoder= LabelEncoder()
df["team1"]=encoder.fit_transform(df["team1"])
df["team2"]=encoder.fit_transform(df["team2"])
df["winner"]=encoder.fit_transform(df["winner"].astype(str))
df["toss_winner"]=encoder.fit_transform(df["toss_winner"])
df["venue"]=encoder.fit_transform(df["venue"])
df["city"]=encoder.fit_transform(df["city"])
df["toss_decision"]=encoder.fit_transform(df["toss_decision"])

#outcome variable team1_win as a probability of team1 winning the match
df.loc[df["winner"]==df["team1"],"team1_win"]=1
df.loc[df["winner"]!=df["team1"],"team1_win"]=0

#outcome variable team1_toss_win as a value of team1 winning the toss
df.loc[df["toss_winner"]==df["team1"],"team1_toss_win"]=1
df.loc[df["toss_winner"]!=df["team1"],"team1_toss_win"]=0

#FEATURES AND LABEL DISTINCTION
X = df.iloc[:,[2,3,4,5,7,9]].values
y = df.iloc[:, 6].values

#TRAIN-TEST-SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=420)

#SCALING THE INPUT 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#FITTING THE MODEL
reg = RandomForestClassifier(n_estimators=100)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
#print('Accuracy of Classifier on test set: {:.4f}'.format(reg.score(X_test, y_test)))

#PICKLING THE MODEL
filename = 'vp.pkl'
pickle.dump(reg, open(filename, 'wb'))

"""
#PREDICTION

prediction=reg.predict([[0,7,0,1,10,1]])
prediction
"""


