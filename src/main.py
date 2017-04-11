import urllib3
import requests
import sys
import re
import os
import time
from bs4 import BeautifulSoup

# Spoof a user agent to stop Austlii throwing 410 errors
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

# Set up the http object that will be used to get resources from the web
http = urllib3.PoolManager(10, headers=user_agent)

# Open the list of URLS from the text file
SourceFile = open('ListOfAustliiURLs.txt', 'r')
ListOfURLsAndMNCs = []

#Create a 'scraped' folder if one doesn't exist
if not os.path.exists(os.path.join(os.path.expanduser('~'),'scraped')):
    os.makedirs(os.path.join(os.path.expanduser('~'),'scraped'))
ScrapedDir = os.path.join(os.path.expanduser('~'),'scraped')

#This is where the txt files must be for checking. If this directory doesn't exist, create it.
TxtDir = 'd:\\txt\\'

for EachLine in SourceFile:
    #For each line in the file, build a list in which each item is a list containing the URL and the MNC for the relevant court
    ListFromLine = EachLine.split('/')
    ListOfURLsAndMNCs.append([EachLine.replace('\n',''),ListFromLine[-2]])

# Begin looping through the main list
for EachItem in ListOfURLsAndMNCs:
    #print('EachItem = '+str(EachItem))
    #Get the HTTP Response Object by 'getting' the url for the court page
    CourtPage = http.request('GET', EachItem[0])
    CourtPageSoup = BeautifulSoup(CourtPage.data, 'html.parser')
    #Go find all the links in the court page
    for YearLink in CourtPageSoup.find_all('a'):
        #See if the link is a four digit number
        if (len(YearLink.text)==4) and (YearLink.text.isdigit()==True):
            Year = YearLink.text
            #Go to the year page
            #print('Court = '+str(EachItem)+', Year = '+str(Year))
            YearPage = http.request('GET', EachItem[0]+YearLink.get('href'))
            YearPageSoup = BeautifulSoup(YearPage.data, 'html.parser')
            #Go find all the cases on that year page
            for CaseEntry in YearPageSoup.find_all('li'):
                #Make a BeautifulSoup out of the case entry so that we can extract href and title
                #print('li on case page = ' + str(CaseEntry))
                CaseEntrySoup = BeautifulSoup(str(CaseEntry),'html.parser')
                for CaseLink in CaseEntrySoup.find_all('a'):
                    #print('Caselink = ' + CaseLink.get('href'))
                    #print('found a link = ' + str(CaseLink))
                    #Get the CaseNumber by stripping the CaseLink of the needless 'up directory' text, and html suffix
                    CaseNumber = CaseLink.get('href')
                    if CaseNumber.startswith('../'):
                        CaseNumber = CaseNumber.replace(CaseNumber[:8],'')
                    CaseNumber = CaseNumber.replace('.html','')
                    #Test whether file exists
                    NewRTFFileName = '[' + Year + '] ' + EachItem[1] + ' ' + CaseNumber + '.rtf'
                    NewTXTFileName = '[' + Year + '] ' + EachItem[1] + ' ' + CaseNumber + '.rtf.txt'
                    GoToCasePage = 0

                    if os.path.isfile(os.path.join(TxtDir, NewTXTFileName)) == False:
                        #print(NewTXTFileName + ' does not exist, going to case.')
                        GoToCasePage = 1

                    if GoToCasePage == 1:
                        #Go to the case page
                        print('Going to case page for ' + NewTXTFileName)
                        CasePage = http.request('GET',EachItem[0]+YearLink.get('href')+'/'+CaseNumber+'.html')
                        CasePageSoup = BeautifulSoup(CasePage.data, 'html.parser')
                        #Find the download link
                        for LinkInCasePage in CasePageSoup.find_all('a'):
                            #print('Link in case page = ' + str(LinkInCasePage))
                            if LinkInCasePage.text=='Download':
                                #Go to the page linked to by the word 'Download'
                                #print('CaseDownloadPage = '+EachItem[0] + YearLink.get('href') + '/' + LinkInCasePage.get('href'))
                                if LinkInCasePage.get('href')[-3:] == 'rtf':
                                    #download this rtf
                                    print('Downloading ' + EachItem[0]+YearLink.get('href')+'/'+CaseNumber+'.rtf' + ' from case page')
                                    time.sleep(.1)
                                    PageToDownload = requests.get(EachItem[0]+YearLink.get('href')+'/'+CaseNumber+'.rtf', headers=user_agent)
                                    with open(os.path.join(ScrapedDir, NewRTFFileName), 'wb') as NewFile:
                                        NewFile.write(PageToDownload.content)
                                else:
                                    CaseDownloadPage = http.request('GET', EachItem[0] + YearLink.get('href') + '/' + LinkInCasePage.get('href'))
                                    CaseDownloadPageSoup = BeautifulSoup(CaseDownloadPage.data, 'html.parser')
                                    #Find the list items
                                    for LiOnCaseDownloadPage in CaseDownloadPageSoup.find_all('li'):
                                        LiOnCaseDownloadPageSoup = BeautifulSoup(str(LiOnCaseDownloadPage), 'html.parser')
                                        #Find the hyperlink in the list item
                                        for LinkInLiOnDownload in LiOnCaseDownloadPageSoup.find_all('a'):
                                            #print('LinkInLiOnDownload = ' + str(LinkInLiOnDownload.text))
                                            if LinkInLiOnDownload.text=='Rich Text Format (RTF)':
                                                #print('RTF download link found.')
                                                #Download the RTF file
                                                time.sleep(.1)
                                                #print('Download = '+LinkInLiOnDownload.get('href'))
                                                PageToDownload = requests.get(LinkInLiOnDownload.get('href'), headers=user_agent)
                                                #Downloader = http.request('GET', LinkInLiOnDownload.get('href'), preload_content=False)
                                                with open(os.path.join(ScrapedDir,NewRTFFileName),'wb') as NewFile:
                                                    NewFile.write(PageToDownload.content)
                                                    #print('Download started.')
                                                    #while True:
                                                        #data = Downloader.read(1)
                                                        #if not data:
                                                            #break
                                                        #NewFile.write(data)
                                                #Downloader.release_conn()
                                                #print('Download finished.')


# http://www.emreakkas.com/localization-tools/convert-rtf-to-txt



