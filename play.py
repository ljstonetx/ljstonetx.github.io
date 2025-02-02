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
#
#FANTASTIC flex tutorial: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
#

import csv

conSiteShortTitle = "Mercedes Historic Photograps"
conSiteLongTitle = "Mercedes Texas Historic Photographs 1900s to 1950s"
conEmailAddress = "mercedestx@gmail.com"
conNumCards=195
conNumSubjects=17
conPostCardFile='PostcardSorted.csv'
conSubjectsFile='postcardViewsSorted.csv'
conColorFileName = 'imagesColorized/'
conCitationsTitle = "Citations for Mercedes History Information" 
conCitationsFile = "PChtmlCitations.html" 
conSMULink         = 'https://digitalcollections.smu.edu/digital/collection/tex/id/'
conUTRGVStudioLink = 'https://scholarworks.utrgv.edu/rgvstudio/' 
conUTRGVMiscLink   = 'https://scholarworks.utrgv.edu/miscphotosedinburg/' 
conSMU = "SMU"
conUTRGVSTUDIO = "UTRGVSTUDIO"
conUTRGVMISC   = "UTRGVMISC"

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
    
def writeStyle(FW):
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>' + conSiteShortTitle + '</title>')
    FW.write('<link rel="stylesheet" href="flexCss.css">')

def writeLongTitle(FW):
    FW.write('<h1><center>' + conSiteLongTitle + '</center></div></h1>')

def makeColorFileName(key):
    return conColorFileName + key + ".jpg"  

def writeHomeHeader(FW):

    FW.write('<div id="flexHeader">')
    writeLongTitle(FW)
    FW.write('<div id="flexHeader">')  
    
    FW.write('<div>These photographs capture the early history of Mercedes, Texas. In the early 1900s, the city and the Lower Rio Grande Valley underwent a dramatic transformation, shifting from traditional ranching to commercial agriculture. This transition set the stage for unprecedented growth, marking an exciting yet challenging era in the regions development. During this time, irrigation and canal systems were established in Mercedes</div>')
    FW.write('<div2> Contact us if you have photographs or images to share on this website ' + conEmailAddress+ '.</div2>')
    FW.write('<div> The town built its own power plant. Mercedes was first in the Valley to have electric lights. Mercedes also served as the site of military camps during both the Border War and World War I. Do you have historical photographs from this period that you would like to share? We would be thrilled to add them to this website. Please reach out to us at ' + conEmailAddress+ '. Thank you for your interest in sharing the history of Mercedes</div>')
    FW.write('</div>')  

def writeHeader(FW, subject):
    FW.write('<div id="flexHeader">')
    writeLongTitle(FW)
    FW.write('<div id="flexHeader">')
    FW.write('<div>Subject: '+ subject + '</div>')
    FW.write('<div2><a href="PCSubjects.html" target="_blank">Home</a></div2>')
    FW.write('<div>' + conEmailAddress + '</div>')
    FW.write('</div>')

def writeCitations(FW):
    FW.write('<div>View source citations:  <a href=' + conCitationsFile + '>' + 'View Citations </a></div>')
    

def writeDescription(FW, description):
    FW.write('<font size="2.5em">' + description + "</font>")

def writeColumn(FW, reader, isCitations):
        line = next(reader)
        subject = line["subject"]
        key = line["key"] 
        imageColorFile = makeColorFileName(key)
        if isCitations == 1:
            description = conCitationsTitle             
            htmlName= "PChtmlCitations.html"
        else:
            description = line["description"]             
            htmlName= makeHtmlSubjectFilename(subject);
            
        FW.write('<div class="column">')
        FW.write('<div class="flex-wrap-subjects"><img src="'+ imageColorFile+ '">')
        FW.write('<p class="b"><b><font color="#cc0000">' + subject + ' </font></b>')
        writeDescription(FW, description)
        #FW.write('<p class="a">' + description) !puts in a new paragraph
        FW.write('<br>')
        FW.write('<a href=' + htmlName + '>' + 'View Photos</a>')        
        FW.write('</div></div>')
        return subject

def writeSubjects():
    
    #https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01
    count = 0
    FH = open(conSubjectsFile)
    reader = csv.DictReader(FH)
    filename = "play.html"
    FW= open(filename, "w+")
    writeStyle(FW)
    FW.write('</head><body>')
    writeHomeHeader(FW)
    while (count < conNumSubjects):
        #start a new row
        FW.write('<div class="flex-wrap">')
        FW.write('<div class="row">')
        subject = writeColumn(FW, reader, 0)
        writeSubjectFile(subject)
        if count < conNumSubjects-1:
            #start column 2
            subject = writeColumn(FW, reader,0)
            count+=1
            FW.write('<div><div><div>')
            writeSubjectFile(subject) 
        # the next is writing the citations
        if count == conNumSubjects-1:  
            writeColumn(FW, reader, 1)
            count=count+1
            FW.write('<div><div><div>')
            
        count+=1
    FW.write('</body></html>')  
    count+=1
    FH.close() 
    FW.close()

def writeSubjectFile(subject):
 
    filename = makeHtmlSubjectFilename(subject);
    #This file was created by exporting the postcards table from wix, then editing to remove single quotes, 
    #then editing it in Open Office Calc to sort on the score column
    
    count=0
    keyIdx = 0
    smuIdx = 1
    idIdx=2    
    scoreIdx =3
    headingIdx =4
    subjectIdx =5
    dateIdx =6
    descriptionIdx =7
    FW= open(filename, "w+")    
    writeStyle(FW)   
    #FW.write('</head><body><div>')
    FW.write('</head><body>')
    writeHeader(FW, subject) 

    from itertools import islice
    with open(conPostCardFile) as csvfile:
        reader1 = csv.reader(csvfile)       
        for row in islice(reader1, conNumCards): 
           
            if row[subjectIdx] != subject: continue
            if row[scoreIdx] == "0": continue
            count = count + 1
            key = row[keyIdx]
            date = row[dateIdx]
            imageColorFile = makeColorFileName(key)   
            description = row[descriptionIdx]
            heading = row[headingIdx]
            source = row[smuIdx]
            id = row[idIdx]
            
            #write out the row
            conType = "fullxxx"
            if conType == "full":  #need to fix css so that image does not center
                FW.write('<div class="flex-wrap">')
                FW.write('<p class="b">')         
                FW.write('<font color="grey"> ' + key + '</font> ')                     
                FW.write('<font color="#cc0000"> <strong>' + heading + ' </strong></font>')  
                FW.write('<font color="grey">' + date + ' </font></p>')  
                FW.write('<img src="'+ imageColorFile+ '">')
                FW.write('<p class="a">' +   description  + '</p>')
                FW.write('<a href=' + imageColorFile + '>' + 'View Enlarged</a>')
                writeSourceLink(FW, source, id)
                FW.write('</div>')
            else:
                FW.write('<div class="flex-wrap-media">')
                FW.write('<p class="b">')         
                FW.write('<font color="grey"> ' + key + '</font> ')                     
                FW.write('<font color="#cc0000"> <strong>' + heading + ' </strong></font>')  
                FW.write('<font color="grey">' + date + ' </font></p>')  
                FW.write('<img src="'+ imageColorFile+ '">')
                FW.write('<p class="a">' +   description  + '</p>')
                FW.write('<a href=' + imageColorFile + '>' + 'View Enlarged</a>')
                writeSourceLink(FW, source, id)
                FW.write('</div>')
        
                
            
            
            
            
            
            
        writeHeader(FW,subject) 
        FW.write('</body></html>')

writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
