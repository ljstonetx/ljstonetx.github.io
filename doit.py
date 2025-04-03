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
#https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01

import csv

conSiteShortTitle = "Mercedes Historic Photograps"
conSiteLongTitle = "Mercedes Texas 1900s to 1950s History and Images"
conEmailAddress = "mercedestx@gmail.com"
conNumCards=195
conNumHxRows=47
conNumHxTopics=4
conNumSubjects=22  #includes Citations in a kludge
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

def makeHtmlSubjectFilename(subject):  
    
    if (subject == "Citations"): 
        return conCitationsFile
    catNoSpace = subject.replace(" ", "")
    return "PChtml" + catNoSpace + ".html"

def writeStyle(FW):
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>' + conSiteShortTitle + '</title>')
    FW.write('<link rel="stylesheet" href="flexCss.css">')
    FW.write('</head><body><div>')

def writeShortHeading(FW, heading):

    FW.write('<p2>' + heading +'<br></p2></div>')    
     

def writeLongHeading(FW, heading):

    FW.write('<p2>' + heading + '<br><br><a href=' + conFileSubjects + ' class="button" target="_blank">Home</a>'+ '</p2></div>')
     
def writeTitle(FW, title):
    FW.write('<p1><div>')
    writeTitle2(FW, title)
    
def writeTitle2(FW, title):
    FW.write('<font color="#cc0000"> <strong>' + title + ' </strong></font>')

def makeColorFileName(key):
    return conColorFileDir + key + ".jpg" 

def makeHistoryFileName(key):
    return conColorFileDir + key     

def writeHomeHeader(FW):

    FW.write('<div id="flexHeader">')
    writeShortHeading(FW,conSiteLongTitle)
    FW.write('<br>')  
    
    FW.write('<div><p1>This website offer a glimpse into the early history of Mercedes, Texas. In the early 1900s, Mercedes and the Lower Rio Grande Valley underwent a transformative shift, moving from traditional ranching to commercial agriculture. This set the stage for significant growth and marked a dynamic period in the regional development. The era is well-documented, largely due to the popularity of postcards, which were popular during that time. The historical context provided on these pages is from various sources which can be explored further on the Citations page.</div><p1>')
    FW.write('</div><br>')    

def writeHeader(FW, subject, heading):
    FW.write('<div id="flexHeader">')
    writeLongHeading(FW, heading)
    FW.write('<div id="flexHeader">')
    FW.write('</div><br>')

def writeCitations(FW):
    FW.write('<div>View source citations:  <a href=' + conCitationsFile + 'class="button">' + 'View Citations </a></div>')

def writeDate(FW, date):
    FW.write('<font color="#414141">' + date + ' </font>')                       

def writeDescription(FW, description):
    FW.write('<br><br><p1>' +   description  + '</p1>')
    FW.write('<br><br>')

def writeImage(FW, imageFile): 
    FW.write('<div class="flex-wrap"><img src="'+ imageFile+ '">')


def writeSourceLink(FW, imageSource, imageId):
    if imageSource == conSMU:
        FW.write('<a href=' + conSMULink +  imageId          + '/ class="button">View High Resolution</a>&nbsp;&nbsp;')
    elif imageSource == conUTRGVSTUDIO: 
        FW.write('<a href=' + conUTRGVStudioLink + imageId   + '/ class="button">View UTRGV Studio</a>&nbsp;&nbsp;')
    elif imageSource == conUTRGVMISC:
        FW.write('<a href=' + conUTRGVMiscLink + imageId     + '/ class="button">View UTRGV Miscellaneous</a>&nbsp;&nbsp;')
    elif imageSource == conOTHER:
        FW.write('<a href=' + imageId                        + '/ class="button">View Source Article</a>')
    
def writeImageEnlarged(FW, imageFile):    
    FW.write('<a href=' + imageFile + ' class="button">'                          + 'View Enlarged</a>&nbsp;&nbsp;')


def writeSubjects():

    subjectIdx =0
    keyIdx = 2
    descriptionIdx =3
    headingIdx=4
    FW= open(conFileSubjects, "w+")    
    writeStyle(FW)   

    writeHomeHeader(FW) 

    from itertools import islice
    with open(conSubjectsFile) as csvfile:
        reader1 = csv.reader(csvfile)       
        for line in islice(reader1, conNumSubjects): 
           
           subject = line[subjectIdx]
           key = line[keyIdx] 
           description = line[descriptionIdx]
           heading = line[headingIdx]
           imageFile = makeColorFileName(line[keyIdx])
           if subject != "subject": #skip first line

               writeImage(FW, imageFile)
               FW.write('<p1>')
               writeTitle2(FW, heading) 
               writeDescription(FW, description)
               htmlName= makeHtmlSubjectFilename(subject);
               FW.write('<a href=' + htmlName         + ' class="button">' + 'View '+ subject + '</a>')
               FW.write('</div><br>')
               
               if (subject == "Fuste" or subject == "Colegio" or subject == "Rio Rico"): 
                writeHxSubjectFile(subject, heading)
               elif (subject != "Citations"):
                    # Citations.pdf file was made by importing citations.csv into a google doc, format order as
                    # number, wrapping the citation column, and exporting to pdf. Then copying file to source code directory               
                   writeSubjectFile(subject, heading) 
               print(subject)        
           
        writeHeader(FW, conSiteLongTitle, conSiteLongTitle)
        FW.write('</body></html>')
        
def writeSubjectFile(subject, heading): 
 
    filename = makeHtmlSubjectFilename(subject);
    #then editing it in Open Office Calc to sort on the score column
    
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
    writeHeader(FW, subject, heading ) 

    from itertools import islice
    with open(conPostCardFile) as csvfile:
        reader = csv.reader(csvfile)       
        for row in islice(reader, conNumCards): 
            if row[subjectIdx] != subject: continue
            if row[scoreIdx] == "0": continue
            imageFile = makeColorFileName(row[keyIdx])
            writeImage(FW,imageFile)
            FW.write('<p1>')                     
            writeDate(FW, row[keyIdx])                    
            writeTitle2(FW, row[headingIdx])
            writeDate(FW, row[dateIdx])
           
            writeDescription(FW, row[descriptionIdx])
 
            writeSourceLink(FW, row[sourceIdx], row[idIdx]) 
            writeImageEnlarged(FW,imageFile)
            FW.write('<br><br>') 
            FW.write('</div>')
                
        writeHeader(FW,subject, heading) 
        FW.write('</body></html>')
        
def writeHxSubjectFile(subject, heading):
 #"Title","topic","imagePic","citationText","citationDate","summary","citationLink"
    filename = makeHtmlSubjectFilename(subject);  
    titleIdx = 0
    
    subjectIdx = 1
    imagePicIdx=2    
    citationTextIdx =imagePicIdx+1
    dateIdx = citationTextIdx+1
    summaryIdx = dateIdx+1
    citationLinkIdx = summaryIdx+1
    FW= open(filename, "w+")    
    writeStyle(FW)   
    writeHeader(FW,subject, heading ) 

    from itertools import islice
    with open(conHistoryFile) as csvfile:
        reader = csv.reader(csvfile)       
        for row in islice(reader,conNumHxRows): 
            if row[subjectIdx] != subject: continue
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
        for row in islice(reader,conNumHxTopics): 
            if row[subjectIdx] != subject: continue         
            writeImage(FW,makeColorFileName(row[imagePicIdx]))
            writeTitle(FW, row[titleIdx])
            writeDescription(FW, row[summaryIdx])
            FW.write('</div></div>')
            writeHxSubjectFile(FW, subject)
        writeHeader(FW,subject) 
        FW.write('</body></html>')

writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
