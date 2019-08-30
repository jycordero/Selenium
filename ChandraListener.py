
#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

#--------- FUNCTIONS
def FillIntroPage(browser, value):
    for name in value.keys():      # Iterates through the fields in the html file with the names in "value[NAMWE] = VALUE"
        elem = browser.find_element_by_name(name) # finds the field with the NAME 
        elem.send_keys(value[name])               # passes the VALUE to the field
    elem.send_keys(Keys.RETURN)    # Pass the RETURN value

#----------- MAIN
if __name__ == "__main__":#---------
    browser = webdriver.Firefox()  # Opens Firefox
    browser.get(webpage)           # Opens the webpage indicated above

    FillIntroPage(browser, IntroValues)


    #wait = WebDriverWait(browser,10)
    #try:
    #    wait.until_not(
    #                    
    #                    )


    #elem = browser.find_element_by_name("Target Name") # finds the field with the NAME 
    #print(elem.text)

    elem = browser.find_element_by_name("Exposure") # finds the field with the NAME 
    print(elem.text)

    print('browser')
    for b in dir(browser):
        print('-----',b)

    print('elem')
    for b in dir(browser.find_element_by_name("obsidRangeList")):
        print('-----',b)

    print(browser.name)
    #browser.close()

