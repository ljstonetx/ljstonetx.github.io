#change log
#12/20/2024 Fixed missing cards: A110 and 0102 had to be copied from "additonal" directory to imagesColorized
#12/20/2024 Had to edit the postcards csv file to remove "copy" form the key for "A110". Not sure hSow it get there
#TODO Citations for Texas Historic Archive Cards, also improve descriptions
#TODO Update github repository
import csv

conSiteShortTitle = "Mercedes Historic Photograps"
conSiteLongTitle = "Mercedes Texas Historic Photographs 1900s to 1950s"
conEmailAddress = "mercedestxhx@gmail.com"
conNumCards=175
conNumSubjects=17
conPostCardFile='PostcardCorrectedQuotesSorted.csv'
conSubjectsFile='postcardViewsSorted.csv'
conColorFileName = 'imagesColorized/'

def makeHtmlSubjectFilename(category):  
    catNoSpace = category.replace(" ", "")
    return "PChtml" + catNoSpace + ".html"

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
    htmlCitationsName = "PChtmlCitations.html"
    FW.write('<div>View source citations:  <a href=' + htmlCitationsName + '>' + 'View Citations </a></div>')
    

def writeDescription(FW, description):
    FW.write('<font size="2.5em">' + description + "</font>")

def writeColumn(FW, reader, isCitations):
        line = next(reader)
        subject = line["subject"]
        key = line["key"] 
        imageColorFile = makeColorFileName(key)
        if isCitations == 1:
            description = "Citations for Mercedes History Information"               
            htmlName= "PChtmlCitations.html"
        else:
            description = line["description"]             
            htmlName= makeHtmlSubjectFilename(subject);
            
        FW.write('<div class="column">')
        FW.write('<div class="flex-wrap-subjects"><img src="'+ imageColorFile+ '">')
        FW.write('<p class="b"><b><font color="#cc0000">' + subject + ' </font></b><br>')
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
    filename = "PCSubjects.html"
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
    scoreIdx =2
    headingIdx =3
    subjectIdx =4
    dateIdx =5
    descriptionIdx =6
    FW= open(filename, "w+")    
    writeStyle(FW)   
    FW.write('</head><body><div>')
    writeHeader(FW, subject) 

    from itertools import islice
    with open(conPostCardFile) as csvfile:
    #with open('PostcardCorrectedQuotesSorted.csv') as csvfile:
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
            smu = row[smuIdx]
            
            #write out the row
            FW.write('<div class="flex-wrap"><img src="'+ imageColorFile+ '">')
            FW.write('<p class="b">')         
            FW.write('<font color="grey"> ' + key + '</font> ')                     
            FW.write('<font color="#cc0000"> <strong>' + heading + ' </strong></font>')  
            FW.write('<font color="grey">' + date + ' </font><br><br>')             
            writeDescription(FW, description)
            FW.write('<br><br><a href=' + imageColorFile + '>' + 'View Enlarged</a> &nbsp; &nbsp;')
            if smu != "none":
                FW.write('<a href=' + 'https://digitalcollections.smu.edu/digital/collection/tex/id/' + smu   + '/>View High Resolution</a>')       
            FW.write('</div>')
            
        writeHeader(FW,subject) 
        FW.write('</body></html>')

writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
