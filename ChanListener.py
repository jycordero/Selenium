
# coding: utf-8

# In[5]:


#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# In[6]:


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


# In[7]:


#--------- FUNCTIONS
def FillIntroPage(browser, value):
    for name in value.keys():      # Iterates through the fields in the html file with the names in "value[NAMWE] = VALUE"
        elem = browser.find_element_by_name(name) # finds the field with the NAME 
        elem.send_keys(value[name])               # passes the VALUE to the field
    elem.send_keys(Keys.RETURN)    # Pass the RETURN value
    
def GetTable(browser,VAR = "exp",ID='21372'):
    name = VAR+ID
    XPATH = "//*[@id=\""+name+"\"]"
    return browser.find_element_by_xpath(XPATH).text


# In[ ]:


#----------- MAIN
if __name__ == "__main__":#---------
    browser = webdriver.Firefox()  # Opens Firefox
    browser.get(webpage)           # Opens the webpage indicated above

    FillIntroPage(browser, IntroValues)

    time.sleep(2)
    
    tableValue = GetTable(browser)
    
    print(tableValue)
    

