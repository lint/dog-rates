import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#Initializing Selenium
driver = webdriver.Firefox()

#List of Dates in YYYY-MM-DD format
dates = []

#Will Store the Tweets
data = []

#Generating Dates
for year in range(2015,2019):
    for month in range(1,13):
        for day in range(1,32):
            
            date = "{}-{}-{}".format(year,month,day)
            dates.append(date)

#Adding/Removing Dates
dates.append("2019-01-01")
dates = dates[310:]


#Main Method
for date in range(len(dates)-1):

    #Twitter's Advanced Search for user @dog_rates and inbetween two dates
    url = "https://twitter.com/search?l=&q=from%3Adog_rates%20since%3A{}%20until%3A{}&src=typd".format(dates[date],dates[date+1])

    #Loads the webpage
    driver.get(url)
    time.sleep(.5)


    #Variable to indicate if scrolling reached the bottom of the page
    last_height = driver.execute_script("return document.body.scrollHeight")

    #Scrolling to the bottom of the page
    for a in range(30):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        #if the current scroll height is the same as the last one, scrolling has stopped. 
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        
        last_height = new_height
        
    
    #Creating BeautifulSoup object
    soup = BeautifulSoup(driver.page_source,"html.parser")

    #Getting Each Tweet's Text
    for tweet in soup.find_all("p",class_="tweet-text"):

        #Stopps picture url from being included in tweet text 
        try:
            tweet.a.clear()
        except:
            pass

        #Adding it to master list
        data.append(tweet.text)

    #Logging Information
    print date,len(data)

#Quits Selenium
driver.quit()

#Saving Data
with open("data.txt",'w') as f:
    for a in data:
        f.write(a+"\n")
