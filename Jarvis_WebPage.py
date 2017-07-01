'''
Author : Hari om Singh
Date : 06-June -2017
Description: This will help jarvis for webpage navigation i.e google searh
'''


import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)

'''

def websearch(searctTxt):

    Txt=searctTxt.replace(' ','+')
    driver.get('https://www.google.co.in/search?q=' +Txt);
    # need to find out the direct webpage hit or google element name to search for the same .
    # "searctTxt" needs to be ussed to find the desired pattern from the google


def youtubeSearch(searchTxt):
    # this will searh the required the video in youtube
    Txt = searchTxt.replace(' ', '+')
    print('youtube',Txt)
    url='https://www.youtube.com/results?search_query='+Txt
    print(url)
    driver.get(url)
    # driver.find_element_by_id("bt-dwl-bt").click()
    driver.find_element_by_css_selector('#results ol li ol li:first-child a').click()
    #driver.find_element_by_css_selector('#results ol li ol li:nth-child(2) a').click()

def youtubeplay(searchTxt):
    # This module will be responsible for yje video play of specific content
    driver=webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver')
    driver.get('http://www.youtube.com/search=?'+ searchTxt);

'''
def myFacebook():
    # This help in navigation for facebook
    # Note: It should be using the cookies of the browser to get the creditails

#def myGmail():
    # This will open the gmail for the user
    # Note: It should be using the cookies of the browser to get the creditails

def torrentDownload(filename):
    pass
    # This will enable to download the series or movies from torrent .
    # Default video quality size need to be fixed or Jarvis should ask the user for video quality

def getSoftware(softwareName):
    pass
    # It will ge  the desired software from internet
    # Note : Needs to decide the software hub for the same

def getPythonModule():
    pass
    # It will pip and install the module name which is being asked
'''
if __name__=='__main__' :
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    websearch('India')
    youtubeSearch('waka waka')
else:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
