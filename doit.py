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
conSiteLongTitle = "Mercedes Texas Historic Photographs 1900s to 1950s"
conEmailAddress = "mercedestx@gmail.com"
conNumCards=195
conNumSubjects=21
conPostCardFile='PostcardSorted.csv'
conSubjectsFile='postcardViewsSorted.csv'
conHistoryFile='History.csv'
conHistoryTextFile='historyText.csv'
conColorFileDir = 'imagesColorized/'
conCitationsTitle = "Citations for Mercedes History Information" 
conCitationsFile = "PChtmlCitations.html" 
conSMULink         = 'https://digitalcollections.smu.edu/digital/collection/tex/id/'
conUTRGVStudioLink = 'https://scholarworks.utrgv.edu/rgvstudio/' 
conUTRGVMiscLink   = 'https://scholarworks.utrgv.edu/miscphotosedinburg/' 
conSMU = "SMU"
conUTRGVSTUDIO = "UTRGVSTUDIO"
conUTRGVMISC   = "UTRGVMISC"
conOTHER       = "OTHER"

def makePostcard(key, source, id, score, heading, subject, date, description):
    postcard = Postcard(key, source, id, score, heading, subject, date, description)
    return postcard


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

def writeLongTitle(FW,subject, heading):
    #FW.write('<h1>' + conSiteLongTitle + '</h1></div>')
    FW.write('<h1>' + heading + '</h1></div>')   
    
    
    #FW.write('<h1>' + heading          + '</div></h1>')
    #FW.write('<center><h2><strong><font color="#cc0000"> ' + heading + '</font></strong> </h2> </center></div>')
    #FW.write('<h1><center>' + heading + '</center></div></h1>')
     
def makeColorFileName(key):
    return conColorFileDir + key + ".jpg" 

def makeHistoryFileName(key):
    return conColorFileDir + key     

def writeHomeHeader(FW):

    FW.write('<div id="flexHeader">')
    writeLongTitle(FW,"", "")
    FW.write('<div id="flexHeader">')  
    
    FW.write('<div><p1>These photographs capture the early history of Mercedes, Texas. In the early 1900s, the city and the Lower Rio Grande Valley underwent a dramatic transformation, shifting from traditional ranching to commercial agriculture. This transition set the stage for unprecedented growth, marking an exciting yet challenging era in the regions development. During this time, irrigation and canal systems were established in Mercedes</div><p1>')
    FW.write('</div><div id="flexHeader">')
    FW.write('<div2><p1>Contact us if you have photographs or images to share on this website ' + conEmailAddress+ '.</p1></div2></div>')
    FW.write('</div><div id="flexHeader">')
    FW.write('<div><p1> The town built its own power plant. Mercedes was first in the Valley to have electric lights. Mercedes also served as the site of military camps during both the Border War and World War I. Do you have historical photographs from this period that you would like to share? We would be thrilled to add them to this website. Please reach out to us at ' + conEmailAddress+ '. Thank you for your interest in sharing the history of Mercedes</p1></div>')
    FW.write('</div>')
    FW.write('</div>')     

def writeHeader(FW, subject, heading):
    FW.write('<div id="flexHeader">')
    writeLongTitle(FW, subject, heading)
    FW.write('<div id="flexHeader">')
    FW.write('<div2><p1><a href="PCSubjects.html" target="_blank">Home</a><p1></div2>')
    FW.write('</div>')

def writeCitations(FW):
    FW.write('<div>View source citations:  <a href=' + conCitationsFile + '>' + 'View Citations </a></div>')
    

def writeDescription(FW, description):
    FW.write('<br><p1>' +   description  + '</p1>')

def writeImage(FW, imageFile):    
    FW.write('<div class="flex-wrap"><img src="'+ imageFile+ '">')
    
def writeSubjects():
 
#https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01
    count=0
    keyIdx = 2
    subjectIdx =0
    filename = "PCSubjects.html"
    descriptionIdx =3
    headingIdx=4
    FW= open(filename, "w+")    
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
           #FW.write('<div class="flex-wrap"><img src="'+ imageFile+ '">')
           writeImage(FW, imageFile)
           FW.write('<p1>')                    
           FW.write('<font color="#cc0000"> <strong>' + heading + ' </strong></font>')
           writeDescription(FW, description)
           htmlName= makeHtmlSubjectFilename(subject);
           FW.write('<br><br><a href=' + htmlName + '>' + 'View '+ subject + '</a>') 
           FW.write('</div>')
           if (count > 3): writeSubjectFile(subject, heading)
           if (count <= 3): writeHxSubjectFile(subject, heading) 
           print(subject) 
           print(count)           
            
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
            count = count + 1
            imageFile = makeColorFileName(row[keyIdx])
            writeImage(FW,imageFile)
            FW.write('<p1>')                     
            FW.write('<font color="grey"> ' + row[keyIdx] + '</font> ')                     
            FW.write('<font color="#cc0000"> <strong>' + row[headingIdx] + ' </strong></font>')  
            FW.write('<font color="grey">' + row[dateIdx] + ' </font>')             
            writeDescription(FW, row[descriptionIdx])
            FW.write('<br><br><a href=' + imageFile + '>' + 'View Enlarged</a> &nbsp;&nbsp;')
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
            
            count = count + 1
            
            title = row[titleIdx]
            date = row[dateIdx]
            imageFile = makeHistoryFileName(row[imagePicIdx])   
            citationText = row[citationTextIdx]
            citationDate = row[dateIdx]
            summary = row[summaryIdx]
            #print('summary ' + summary)
            citationLink = row[citationLinkIdx]
            writeImage(FW,imageFile)
            FW.write('<p1>')                     
            #FW.write('<font color="grey"> ' + date + '</font> ')                     
            FW.write('<div><font color="#cc0000"> <strong>' + title + ' </strong></font>')  
            FW.write('<font color="grey">' + date + ' </font>')             
            writeDescription(FW, summary)
            FW.write('<br><br><a href=' + imageFile + '>' + 'View Enlarged</a> &nbsp;&nbsp;')
            
            writeSourceLink(FW, conOTHER, citationLink)
            #FW.write('<br><br><a href=' + citationText + '>' + 'View Article</a> &nbsp;&nbsp;')
            #writeSourceLink(FW, sourceLink, id)
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
            FW.write('<p1>')                                        
            FW.write('<div><font color="#cc0000"> <strong>' + title + ' </strong></font>')
            writeDescription(FW, summary)
            FW.write('</div></div>')
            writeHxSubjectFile(FW, subject)
                
        writeHeader(FW,subject) 
        FW.write('</body></html>')

#writeHxSubjectTextFile("Colegio")
#writeHxSubjectTextFile("Fuste")
#writeHxSubjectTextFile("Rio Rico")
writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
