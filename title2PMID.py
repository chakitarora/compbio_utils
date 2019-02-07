
#title2PMID.py #https://github.com/chakitarora

#This code converts a csv containing article titles to a csv containing PMID of the articles.
#Enter input/output filename and path to get results.
#example input file: title2PMID_input.csv

#usage: 
#On terminal go to folder containing .py file then run:
# >python3 title2PMID.py input_filename.csv output_filename.csv



#requirements (installation order):
#1. python3
#2. chromedriver
#3. selenium for python

#For a mac os which already has anaconda (python3) and homebrew (like mine), just run these on your terminal window:
# >brew tap homebrew/cask
# >brew cask install chromedriver
# >conda install -c conda-forge selenium

#---------------------------------------------------------------------------------------------------------------#
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv
import sys
#HC: to run headless chrome browser
from selenium.webdriver.chrome.options import Options #HC1
options = Options()                                   #HC2
options.set_headless(headless=True)                   #HC3
driver = webdriver.Chrome(options=options)            #HC4

#to display browser window comment HC1-4 and uncomment:
#driver = webdriver.Chrome()


driver.get("https://www.ncbi.nlm.nih.gov/pubmed") #pubmed webpage

#----------------------------------------------INPUT-------------------------------------------------------#

#input csv file containing titles in a single column csv
input=list((pd.read_csv(sys.argv[1],sep='\n',header=None)).iloc[:,0])


input_start=1                     #or enter a manual start
input_end=len(input)             #or enter a manual end value

#---------------------------------------------OUTPUT------------------------------------------------------#

#specify output filename and path here
file = open(sys.argv[2],'w')


#---------------------------------------------------------------------------------------------------------#
with file:
    writer = csv.writer(file);

    for i in range(input_start-1,input_end):
        driver.find_element_by_xpath('//*[@id="term"]').send_keys(input[i])
        driver.find_element_by_xpath('//*[@id="search"]').click()

        #time.sleep(1)

        try:
            driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[2]/div/div/div[1]/div/h3/a').click()    
        except :
            pass
        
        try:
            x = driver.find_elements_by_xpath('//*[@id="maincontent"]/div/div[5]/div[1]/div[2]/div[2]/div/dl/dd')
        except:
            pass
        
        try:
            x = driver.find_elements_by_xpath('//*[@id="maincontent"]/div/div[5]/div/div[5]/div[1]/dl/dd[1]')
        except:
            pass
            
        for p in x:
            val=p.text
        file.write(val+"\n")
        print(val)
        driver.execute_script("window.open('https://www.ncbi.nlm.nih.gov/pubmed');")
        driver.switch_to.window(driver.window_handles[-1])
driver.quit()     
