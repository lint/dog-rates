#!/usr/bin/python3
import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import json

#Note: Tabbing is inconsistent in some places (mostly double width for the entire script)
#This is due to mixing work done on Pythonista (iOS mobile app) and work done on my pc

#Loading Data
data  = []
with open("data.txt") as f:
        tweets = f.read().splitlines()

#Iterating through every tweet
for string in tweets:

    #Initializing List for the percents
    rates = []

    #Splits the tweet text on the "/" character which is used to denotate rates
    split =  string.split("/")

    #Each part that was separated by the slash
    for part in range(len(split)-1):

        #The strings that are left and right of the slash
        leftStr = ""
        rightStr = ""

        #Branching from the slash until it hits a space
        for a in range(len(split[part])-1,-1,-1):
            if split[part][a] != " ":
                leftStr = split[part][a] + leftStr
            else:
                break

        for a in range(len(split[part+1])):
            if split[part+1][a] != " ":
                rightStr+=split[part+1][a]
            else:
                break

        #Only adds it to rates if both sides are digits
        if leftStr.isdigit() and rightStr.isdigit():
            rates.append("/".join([leftStr,rightStr]))

    #Adds the rates to the master data list
    data.append(rates)


#Creates frames folder if it does not exist
if not os.path.exists("frames/"):
    os.makedirs("frames/")




#############################################

#Master holds the counts for each rating
master = {}

#Counting for different file names
frame = 1

#Going through every tweets by denotated bin size
binSize = 10

for a in range(0,len(data),binSize):
	
	#Initializing vars
	subset = []
	final = []
	
	#if a comment had multiple rates
	for extra in data[a:a+binSize]:
		for part in extra:
			subset.append(part)
			
	
	#weeding out anything that isnt a whole number out of 10 
	for b in range(len(subset)):
		if  subset[b].split("/")[1] == "10":
			if subset[b].split("/")[0].isdigit() and len(subset[b].split("/")[0]) <= 2: 
				final.append(subset[b])
	
	
	#getting rates' frequencies 
	counter  = dict(Counter(final))
	
	#adding rates' frequencies to the master dict
	for rating in  sorted(counter,key = lambda x: float(x.split("/")[0])):
		if rating not in master:
			master[rating] = counter[rating]
		else:
			master[rating] += counter[rating]
			
	#Then we graph===================
	
	#Ordering rates from smallest to largest
	objects = sorted(master,key = lambda x: float(x.split("/")[0]))
	
	#y values (counts) for each rate
	performance = [master[x] for x in objects]
	
	#giving each bar its position on the graph
	position = range(len(objects))
	
	
	#Creating the figure and plotting
	plt.figure(figsize=(12, 5))  
	plt.bar(position, performance, align='center', alpha=.75, color=(0,.6,.5))
	
	#Adding Information to graph
	plt.title('The Distribution of WeRateDogs\'s Ratings',size=20)
	plt.xticks(position, objects)
	plt.ylabel('Count',size=15)
	plt.xlabel("Ratings",size=15)
	plt.ylim(0,int(max(performance)*1.2))
	plt.xlim([-1,len(objects)])

	#Removing Top and Right Edges and Ticks
	ax=plt.gca() 
	
	spines = list(ax.spines.values())
	spines[3].set_visible(False)
	spines[1].set_visible(False)
	
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	

	

	
	#Saving the figure
	#plt.show()
	filename = "0"*(3-len(str(frame)))+str(frame)
	plt.savefig("frames/frame{}.png".format(filename),dpi=200)
	
	#Clearing Figure
	plt.close("all")
	
	#Logging
	print ("done frame:", frame)
	
	#Incrementing Counter
	frame +=1
	
	
	
	
	
	



