#Domain setup
#1. do nslookup for ljstone.github.com
#there will be several addresses at the bottom, get one of them. For example
#mercedextx.com 185.1999.110.153
#www.mercedestx.com 185.1999.110.153
#2.Domain mercedestx.com is registered with Wix
#In Wix, go to Billing & Subscription, Pages, Domains, 
#mercedestx, click on ellipse, select , Select DNS Records. 
#3.Add A (Host) records for the address obtained in the nslookpu 
#We tried to use CNAME ljstone.gethub.io, but it
#would not let use put the www.mercedestx.com only mercedestx.com
#so as a workaround used the A records. But will need to update these if github
#changes the ip addresses
#4.go to ljstone.github.io. Go to Pages, Settings, domains. 
#add custom domain mercedestx.com
#
#change log
#12/20/2024 Fixed missing cards: A110 and 0102 had to be copied from "additonal" directory to imagesColorized
#12/20/2024 Had to edit the postcards csv file to remove "copy" form the key for "A110". Not sure hSow it get there
#
#TODO Update github repository

import csv

conSiteShortTitle = "Mercedes Historic Photograps"
conSiteLongTitle = "Mercedes Texas 1900s to 1950s History and Images"
conEmailAddress = "mercedestx@gmail.com"
conNumCards=195
conNumSubjects=21
conPostCardFile='PostcardSorted.csv'
conSubjectsFile='postcardViewsSorted.csv'
conHistoryFile='History.csv'
conFileSubjects='index.html'
conHistoryTextFile='historyText.csv'
conColorFileDir = 'imagesColorized/'
conCitationsTitle = "Citations for Mercedes History Information" 
conCitationsFile = "Citations.pdf" 
conSMULink         = 'https://digitalcollections.smu.edu/digital/collection/tex/id/'
conUTRGVStudioLink = 'https://scholarworks.utrgv.edu/rgvstudio/' 
conUTRGVMiscLink   = 'https://scholarworks.utrgv.edu/miscphotosedinburg/' 
conSMU = "SMU"
conUTRGVSTUDIO = "UTRGVSTUDIO"
conUTRGVMISC   = "UTRGVMISC"
conOTHER       = "OTHER"



def makeHtmlSubjectFilename(category):  
    catNoSpace = category.replace(" ", "")
    return "PChtml" + catNoSpace + ".html"

def writeSourceLink(FW, imageSource, imageId):
    if imageSource == conSMU:
        FW.write('<a href=' + conSMULink + imageId        + '/>View High Resolution</a>')
    elif imageSource == conUTRGVSTUDIO: 
        FW.write('<a href=' + conUTRGVStudioLink + imageId   + '/>View UTRGV Studio</a>')
    elif imageSource == conUTRGVMISC:
        FW.write('<a href=' + conUTRGVMiscLink + imageId  + '/>View UTRGV Miscellaneous</a>')
    elif imageSource == conOTHER:
        FW.write('<a href=' + imageId  + '/>View Source Article</a>')

def writeStyle(FW):
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>' + conSiteShortTitle + '</title>')
    FW.write('<link rel="stylesheet" href="flexCss.css">')

def writeShortTitle(FW, heading):

    FW.write('<p2>' + heading +'</p2></div>')    
     

def writeLongTitle(FW, heading):

    FW.write('<p2>' + heading + '<br><a href=' + conFileSubjects + ' class="button" target="_blank">Home</a>'+ '</p2></div>')
     
def writeTitle(FW, title):
    FW.write('<p1><div><font color="#cc0000"> <strong>' + title + ' </strong></font>') 
    
def writeTitle2(FW, title):
    FW.write('<font color="#cc0000"> <strong>' + title + ' </strong></font>')

def makeColorFileName(key):
    return conColorFileDir + key + ".jpg" 

def makeHistoryFileName(key):
    return conColorFileDir + key     

def writeHomeHeader(FW):

    FW.write('<div id="flexHeader">')
    writeShortTitle(FW,conSiteLongTitle)
    FW.write('<div id="flexHeader">')  
    
    FW.write('<div><p1>These photographs offer a glimpse into the early history of Mercedes, Texas. In the early 1900s, both Mercedes and the Lower Rio Grande Valley experienced a profound transformation, transitioning from traditional ranching to thriving commercial agriculture. This shift laid the foundation for remarkable growth, marking a dynamic and challenging period in the regions development. The era is extensively documented, thanks in part to the widespread popularity of postcards. Most of the images featured here were sourced from these collectible postcards, which were a common medium at the time. The historical context provided has been gathered from a variety of sources, which can be explored further on the Citations page of this website.</div><p1>')
    FW.write('</div>')    

def writeHeader(FW, subject, heading):
    FW.write('<div id="flexHeader">')
    writeLongTitle(FW, heading)
    FW.write('<div id="flexHeader">')
    FW.write('</div><br>')

def writeCitations(FW):
    FW.write('<div>View source citations:  <a href=' + conCitationsFile + '>' + 'View Citations </a></div>')
    

def writeDate(FW, date):
    FW.write('<font color="grey">' + date + ' </font>')                       

def writeDescription(FW, description):
    FW.write('<br><br><p1>' +   description  + '</p1>')

def writeImage(FW, imageFile):    
    FW.write('<div class="flex-wrap"><img src="'+ imageFile+ '">')
   
def writeImageEnlarged(FW, imageFile):    
    FW.write('<br><br><a href=' + imageFile + '>' + 'View Enlarged</a> &nbsp;&nbsp;')
   
def writeSubjects():
 
#https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01
    count=0
    keyIdx = 2
    subjectIdx =0
    descriptionIdx =3
    headingIdx=4
    FW= open(conFileSubjects, "w+")    
    writeStyle(FW)   
    FW.write('</head><body><div>')
    writeHomeHeader(FW) 

    from itertools import islice
    with open(conSubjectsFile) as csvfile:
        reader1 = csv.reader(csvfile)       
        for line in islice(reader1, conNumSubjects): 
           
           subject = line[subjectIdx]
           key = line[keyIdx] 
           description = line[descriptionIdx]
           heading = line[headingIdx]
           imageFile = makeColorFileName(key)
           if subject == "subject": continue
           
           count = count + 1
           writeImage(FW, imageFile)
           FW.write('<p1>')
           writeTitle2(FW, heading) 
           writeDescription(FW, description)
           htmlName= makeHtmlSubjectFilename(subject);
           # the citations.pdf file was made by importing citations.csv into a google doc,
           # formatting the number to number, wrapping the citation, and exporting to pdf
           # and copying that file to the source code directory
           if (subject == "Citations"): 
               FW.write('<br><br><a href=' + conCitationsFile + '>' + 'View '+ subject + '</a>') 
           else:  
               FW.write('<br><br><a href=' + htmlName + '>' + 'View '+ subject + '</a>') 
           FW.write('</div>')
           
           if (subject == "Fuste" or subject == "Colegio" or subject == "Rio Rico"): 
            writeHxSubjectFile(subject, heading)
           else: 
               writeSubjectFile(subject, heading) 
           print(subject)        
            
        writeHomeHeader(FW) 
        FW.write('</body></html>')
        
def writeSubjectFile(subject, heading):
 
    filename = makeHtmlSubjectFilename(subject);
    #This file was created by exporting the postcards table from wix, then editing to remove single quotes, 
    #then editing it in Open Office Calc to sort on the score column
    
    count=0
    keyIdx = 0
    sourceIdx = 1
    idIdx=2    
    scoreIdx =3
    headingIdx =4
    subjectIdx =5
    dateIdx =6
    descriptionIdx =7
    FW= open(filename, "w+")    
    writeStyle(FW)   
    FW.write('</head><body><div>')
    writeHeader(FW, subject, heading ) 

    from itertools import islice
    with open(conPostCardFile) as csvfile:
        reader = csv.reader(csvfile)       
        for row in islice(reader, conNumCards): 
            if row[subjectIdx] != subject: continue
            if row[scoreIdx] == "0": continue
            count += 1 
            imageFile = makeColorFileName(row[keyIdx])
            writeImage(FW,imageFile)
            FW.write('<p1>')                     
            writeDate(FW, row[keyIdx])                    
            writeTitle2(FW, row[headingIdx])
            writeDate(FW, row[dateIdx])   
            writeDescription(FW, row[descriptionIdx])
            writeImageEnlarged(FW,imageFile)
            writeSourceLink(FW, row[sourceIdx], row[idIdx])
            FW.write('</div>')
                
        writeHeader(FW,subject, heading) 
        FW.write('</body></html>')
        
def writeHxSubjectFile(subject, heading):
 #"Title","topic","imagePic","citationText","citationDate","summary","citationLink"
    filename = makeHtmlSubjectFilename(subject);  
    count=0
    titleIdx = 0
    
    subjectIdx = 1
    imagePicIdx=2    
    citationTextIdx =imagePicIdx+1
    dateIdx = citationTextIdx+1
    summaryIdx = dateIdx+1
    citationLinkIdx = summaryIdx+1
    FW= open(filename, "w+")    
    writeStyle(FW)   
    FW.write('</head><body><div>')
    writeHeader(FW,subject, heading ) 

    from itertools import islice
    with open(conHistoryFile) as csvfile:
        reader = csv.reader(csvfile)       
        for row in islice(reader,47 ): 
            if row[subjectIdx] != subject: continue
            count += 1 
            title = row[titleIdx]
            date = row[dateIdx]
            imageFile = makeHistoryFileName(row[imagePicIdx])   
            citationText = row[citationTextIdx]
            citationDate = row[dateIdx]
            summary = row[summaryIdx]
            citationLink = row[citationLinkIdx]
            writeImage(FW,imageFile)  
            writeTitle(FW, title)
            writeDate(FW, date)            
            writeDescription(FW, summary)
            writeImageEnlarged(FW,imageFile)
            writeSourceLink(FW, conOTHER, citationLink)
            FW.write('</div></div><br><br>')
        writeHeader(FW,subject, heading ) 
        FW.write('</body></html>')  
            
def writeHxSubjectTextFile(subject):
 #"Title","topic","imagePic","citationText","citationDate","summary","citationLink"
    filename = makeHtmlSubjectFilename(subject);
    #This file was created by exporting the postcards table from wix, then editing to remove single quotes, 
    #then editing it in Open Office Calc to sort on the score column
    #"heading","topic","description","image","imageHeader","score"
    count=0
    titleIdx = 0   
    subjectIdx = 1
    summaryIdx = 2
    imagePicIdx= 3
    scoreIdx= 4
 
    FW= open(filename, "w+")    
    writeStyle(FW)   
    FW.write('</head><body><div>')
    writeHeader(FW, subject) 

    from itertools import islice
    with open(conHistoryTextFile) as csvfile:
        reader = csv.reader(csvfile)       
        for row in islice(reader,4 ): 
            if row[subjectIdx] != subject: continue
            
            count = count + 1           
            title = row[titleIdx]
            imageFile = makeColorFileName(row[imagePicIdx])   
            summary = row[summaryIdx]
            writeImage(FW,imageFile)
            writeTitle(FW, title)
            writeDescription(FW, summary)
            FW.write('</div></div>')
            writeHxSubjectFile(FW, subject)
                
        writeHeader(FW,subject) 
        FW.write('</body></html>')

writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
