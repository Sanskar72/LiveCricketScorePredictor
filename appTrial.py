# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import math

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))
filename = 'vp.pkl'
classi = pickle.load(open(filename, 'rb'))
dataframe1 = pd.read_excel('cric_ipl.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('indexTrial.html')

@app.route('/predict', methods=['POST'])
def predict():

    team_names = {
    "MI": "Mumbai Indians",
    "RCB": "Royal Challengers Bangalore",
    "DC": "Delhi Capitals",
    "KKR": "Kolkata Knight Riders",
    "CSK": "Chennai Super Kings",
    "RR": "Rajasthan Royals",
    "PBKS": "Kings XI Punjab",
    "SRH": "Sunrisers Hyderabad"
    }
    """
    teams = dataframe1.loc[4,'Cricbuzz Mobile Apps']
    x = teams.split(", ")
    team_name = x[0]
    y = team_name.split(" vs ")
    team1 = y[0]
    team2 = y[1]
    """
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]


        temp_arrayZ=temp_array

        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
            
            
        score1 = dataframe1.loc[8,'Cricbuzz Mobile Apps']
        score2 = dataframe1.loc[9,'Cricbuzz Mobile Apps']
        t1=""
        k1=0;
        for i in score1:
            if i!= ' ' and k1<4:
                t1=t1 + i
                k1=k1+1
            elif i==' ':
                break
        #print("Team Batting First is " + team_names[t1])  

        separate_score1 = score1[k1 +3:len(score1)].split(" ")
        runs_wkts1 = separate_score1[0].split("/")
        runs1=int(runs_wkts1[0])
        wickets1=int(runs_wkts1[1])
        

        overs1 = separate_score1[1]
        overs1 = float(overs1[1:len(overs1)-1])
        overs1=float(overs1)
        

        if score2.find("-")==-1:
            temp_arrayZ = temp_arrayZ + [overs1, runs1, wickets1, runs_in_prev_5, wickets_in_prev_5]
            data1 = np.array([temp_arrayZ])
            my_prediction = int(regressor.predict(data1)[0])
        else:
            t2=""
            k2=0;
            for i in score2:
                if i!= ' ' and k2<4:
                    t2=t2 + i
                    k2=k2+1
                elif i==' ':
                    break
            #print("Team Batting Second is " + team_names[t2])

            separate_score2 = score2[k2 +3:len(score2)].split(" ")
            runs_wkts2 = separate_score2[0].split("/")
            runs2=int(runs_wkts2[0])
            wickets2=int(runs_wkts2[1])

            overs2 = separate_score2[1]
            overs2 = overs2[1:len(overs2)-1]
            overs2=float(overs2)
            temp_array = temp_array + [overs2, runs2, wickets2, runs_in_prev_5, wickets_in_prev_5]
            data = np.array([temp_array])
            my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit = my_prediction-15, upper_limit = my_prediction)


@app.route('/victory', methods=['POST'])
def victory():
    temp_array1 = list()
    team='None'
    
    
    if request.method == 'POST':
        
        batting_team1 = request.form['batting-team']
        if batting_team1 == 'Chennai Super Kings':
            temp_array1 = temp_array1 + [0]
        elif batting_team1 == 'Delhi Daredevils':
            temp_array1 = temp_array1 + [1]
        elif batting_team1 == 'Kings XI Punjab':
            temp_array1 = temp_array1 + [2]
        elif batting_team1 == 'Kolkata Knight Riders':
            temp_array1 = temp_array1 + [3]
        elif batting_team1 == 'Mumbai Indians':
            temp_array1 = temp_array1 + [4]
        elif batting_team1 == 'Rajasthan Royals':
            temp_array1 = temp_array1 + [5]
        elif batting_team1 == 'Royal Challengers Bangalore':
            temp_array1 = temp_array1 + [6]
        elif batting_team1 == 'Sunrisers Hyderabad':
            temp_array1 = temp_array1 + [7]
            
            
        bowling_team1 = request.form['bowling-team']
        if bowling_team1 == 'Chennai Super Kings':
            temp_array1 = temp_array1 + [0]
        elif bowling_team1 == 'Delhi Daredevils':
            temp_array1 = temp_array1 + [1]
        elif bowling_team1 == 'Kings XI Punjab':
            temp_array1 = temp_array1 + [2]
        elif bowling_team1 == 'Kolkata Knight Riders':
            temp_array1 = temp_array1 + [3]
        elif bowling_team1 == 'Mumbai Indians':
            temp_array1 = temp_array1 + [4]
        elif bowling_team1 == 'Rajasthan Royals':
            temp_array1 = temp_array1 + [5]
        elif bowling_team1 == 'Royal Challengers Bangalore':
            temp_array1 = temp_array1 + [6]
        elif bowling_team1 == 'Sunrisers Hyderabad':
            temp_array1 = temp_array1 + [7]

        toss_winner = request.form['toss-winner']
        if toss_winner == 'Chennai Super Kings':
            temp_array1 = temp_array1 + [0]
        elif toss_winner == 'Delhi Daredevils':
            temp_array1 = temp_array1 + [1]
        elif toss_winner == 'Kings XI Punjab':
            temp_array1 = temp_array1 + [2]
        elif toss_winner == 'Kolkata Knight Riders':
            temp_array1 = temp_array1 + [3]
        elif toss_winner == 'Mumbai Indians':
            temp_array1 = temp_array1 + [4]
        elif toss_winner == 'Rajasthan Royals':
            temp_array1 = temp_array1 + [5]
        elif toss_winner == 'Royal Challengers Bangalore':
            temp_array1 = temp_array1 + [6]
        elif toss_winner == 'Sunrisers Hyderabad':
            temp_array1 = temp_array1 + [7]
            
            
        toss_deci = float(request.form['toss-deci'])
        venue = int(request.form['venue'])
        team1_toss = int(request.form['team1_toss'])
        
        temp_array1 = temp_array1 + [toss_deci,venue,team1_toss]
        
        data = np.array([temp_array1])
        prediction1 = int(classi.predict(data)[0])

        a=abs(temp_array1[0]-prediction1)
        b=abs(temp_array1[1]-prediction1)

        if a<=b:
            prediction1=temp_array1[0]
        else:
            prediction1=temp_array1[1]

        percent=((max(a,b)-min(a,b))/max(a,b))*100
        percent=percent-10
        percent=round(percent,2)

        if prediction1 == 0:
            team='Chennai Super Kings'
        elif prediction1 == 1:
            team = 'Delhi Daredevils'
        elif prediction1 == 2:
            team = 'Kings XI Punjab'
        elif prediction1 == 3:
            team = 'Kolkata Knight Riders'
        elif prediction1 == 4:
            team = 'Mumbai Indians'
        elif prediction1 == 5:
            team = 'Rajasthan Royals'
        elif prediction1 == 6:
            team = 'Royal Challengers Bangalore'
        elif prediction1 == 7:
            team = 'Sunrisers Hyderabad'

              
        return render_template('resultVP.html', prediction1 = team, percent = percent)



if __name__ == '__main__':
	app.run(debug=True)