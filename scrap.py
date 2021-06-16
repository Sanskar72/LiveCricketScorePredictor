import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt

dataframe1 = pd.read_excel('cric_ipl.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

"""
team_names = {
	"MI": "Mumbai Indians",
	"RCB": "Royal Challengers Bangalore",
	"DC": "Delhi Capitals",
	"KKR": "Kolkata Knight Riders",
	"CSK": "Chennai Super Kings",
	"RR": "Rajasthan Royals",
	"PBKS": "Punjab Kings",
	"SRH": "Sunrisers Hyderabad"
}

teams = dataframe1.loc[4,'Cricbuzz Mobile Apps']
x = teams.split(", ")
team_name = x[0]
y = team_name.split(" vs ")
team1 = y[0]
team2 = y[1]
print("T1: ",team1)
print("T2: ",team2)


crr_text = dataframe1.loc[11,'Cricbuzz Mobile Apps']
crr_array = crr_text.split(": ")
crr=float(crr_array[1])
print("CRR:",crr)
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
print("Team Batting First is " + team_names[t1])	

separate_score1 = score1[k1 +3:len(score1)].split(" ")
runs_wkts1 = separate_score1[0].split("/")

print("Runs, Wickets")
print(runs_wkts1)
runs=int(runs_wkts1[0])
wickets=int(runs_wkts1[1])

overs1 = separate_score1[1]
overs1 = overs1[1:len(overs1)-1]
overs1=float(overs1)

print("Overs:- " , overs1)

if score2.find("-")==-1:
	if team1 == team_names[t1]:
		print("Team Batting Second is " + team2)
	else:
		print("Team Batting Second is " + team1)
		print("Second Team Yet to Bat")
else:
	t2=""
	k2=0;
	for i in score2:
		if i!= ' ' and k2<4:
			t2=t2 + i
			k2=k2+1
		elif i==' ':
			break
	print("Team Batting Second is " + team_names[t2])

	separate_score2 = score2[k2 +3:len(score2)].split(" ")
	runs_wkts2 = separate_score2[0].split("/")

	print("Runs, Wickets")
	print(runs_wkts2)

	overs2 = separate_score2[1]
	overs2 = overs2[1:len(overs2)-1]




	"""
runs=51
prediction=140
crr_text = dataframe1.loc[11,'Cricbuzz Mobile Apps']
crr_array = crr_text.split(": ")
crr=float(crr_array[1])
print("CRR:",crr)
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

separate_score1 = score1[k1 +3:len(score1)].split(" ")
overs1 = separate_score1[1]
overs1 = overs1[1:len(overs1)-1]
overs1=float(overs1)
if score2.find("-")==-1:
	overs_left=20-math.ceil(overs1)
else:
	t2=""
	k2=0;
	for i in score2:
		if i!= ' ' and k2<4:
			t2=t2 + i
			k2=k2+1
		elif i==' ':
			break
	separate_score2 = score2[k2 +3:len(score2)].split(" ")
	overs2 = separate_score2[1]
	overs2 = overs2[1:len(overs2)-1]
	overs2=float(overs2)
	overs_left=20-math.ceil(overs2)
	print("Overs left",overs_left)



rand_runs = abs(np.random.normal(loc=5.25, scale=4, size=(overs_left)))
rand_runs=np.array(rand_runs)
total1=sum(rand_runs)
total=total1+runs
diff=prediction-total
to_add=diff/overs_left
rand_runs=rand_runs+to_add
runs_over = [round(num) for num in rand_runs]
overrs = [*range(19-overs_left+1, 20, 1)]


tott=0
cum_runs=list()
for i in runs_over:
	cum_runs.append(tott+i)
	tott=tott+i

ncum_runs=np.array(cum_runs)
ncum_runs=ncum_runs+runs
print("CR:",cum_runs)
print("tot1:",sum(runs_over))


def plot_bar(overrs, runs_over):
	plt.style.use("fivethirtyeight")
	plt.bar(overrs, runs_over, label='Prediction')
	plt.xlabel('Over')
	plt.ylabel('Runs in that over')
	plt.legend()
	plt.savefig("plot1.png")
	plt.close()

def plot_line(overrs, runs_over):
	plt.style.use("fivethirtyeight")
	plt.plot(overrs, runs_over, linestyle='--', label='Prediction')
	plt.xlabel('Over')
	plt.ylabel('Total Runs')
	plt.legend()
	plt.savefig("plot2.png")
	plt.close()


plot_bar(overrs, runs_over)
plot_line(overrs, ncum_runs)


#class='result-p'


	
	