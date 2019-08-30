
# coding: utf-8

# In[12]:


#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Import smtplib for the actual sending function
# Import the email modules we'll need
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email

import time


# In[13]:


#------------ VARIABLES
webpage = 'https://cda.harvard.edu/chaser/mainEntry.do' 
fields = [
            "target",
            "obsidRangeList",
            "Exposure",
            ]
IntroValues = {}
IntroValues["target"] = "GW170817"
IntroValues["obsidRangeList"]  =  "21372"
#nextEvt = '22737'
#IntroValues["obsidRangeList"]  =  nextEvt


delay = 3


# In[14]:


#--------- FUNCTIONS
def FillIntroPage(browser, value):
    for name in value.keys():      # Iterates through the fields in the html file with the names in "value[NAMWE] = VALUE"
        elem = browser.find_element_by_name(name) # finds the field with the NAME 
        elem.send_keys(value[name])               # passes the VALUE to the field
    elem.send_keys(Keys.RETURN)    # Pass the RETURN value
    
def GetXPath(browser,VAR = "exp",ID='21372'):
    return "//*[@id=\""+VAR+ID+"\"]"

def GetTable(browser,XPATH):
    return browser.find_element_by_xpath(XPATH).text

def ChanListener(webpage,IntroValues,delay):
    browser = webdriver.Firefox()  # Opens Firefox
    browser.get(webpage)           # Opens the webpage indicated above

    FillIntroPage(browser, IntroValues) # Fills in the values according to the dictionary 

    time.sleep(1) #Waits for the page to load
      
    wait  = WebDriverWait(browser,delay)# Create Wait onbject linked to the browser, checking evey "delay" seconds
    XPATH = GetXPath(browser,VAR='exp',ID='21372')
    try:
        myElem = wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
        Status['notReady']  = False
        Status['Target'] = IntroValues['target']
        Status['ID']     = IntroValues['obsidRangeList']
        
        browser.close()
        return Status
    except TimeoutException:
        Status['notReady']  = True
        Status['Target'] = None
        Status['ID']     = None
        
        browser.close()
        return Status
    
    
    
def SendEmail(Status,
              mailFrom = 'joseph.cordero1@gmail.com',
              mailTo   = 'joseph.cordero1@gmail.com',
             ):
        
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(mailFrom, "PASSWORD")
    
    msg = MIMEMultipart()
    msg['From'] = mailFrom
    msg['To'] = mailTo
    if Status['notReady']:
        msg['Subject'] = 'Chandar NOT ready'
        msg.attach(MIMEText('Chandra data is NOT ready!\n'+
                       'Somehow code stopped working\n'+
                       '\n'+
                       'You can check status of data here webpage https://cda.harvard.edu/chaser/mainEntry.do \n' 
                           )
                  )
    else:
        msg['Subject'] = 'Chandar READY!'
        msg.attach(MIMEText('Chandra data is ready!\n'+
                       '---Target:: '+Status['Target']+'\n'+
                       '---ID    :: '+Status['ID']+'\n'+
                       '\n'+
                       'Visit webpage https://cda.harvard.edu/chaser/mainEntry.do \n' 
                           )
                  )

    server.set_debuglevel(True) # show communication with the server
    try:
        server.sendmail(mailFrom, [mailTo], msg.as_string())

    finally:
        server.quit()


# In[15]:


#----------- MAIN
if __name__ == "__main__":#---------
    Status = {'notReady':True}
    while Status['notReady']:
        Status = ChanListener(webpage, IntroValues, delay)
        print("Still waiting for Chandra ¯\_(ツ)_/¯ ")
        
    SendEmail(Status)
        


# In[16]:


Status

