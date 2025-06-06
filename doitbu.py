#change log
#12/20/2024 Fixed missing cards: A110 and 0102 had to be copied from "additonal" directory to imagesColorized
#12/20/2024 Had to edit the postcards csv file to remove "copy" form the key for "A110". Not sure how it get there
import csv

siteTitle = "Mercedes Historic Photograps"

def makeHtmlSubjectFilename(category):  
    catNoSpace = category.replace(" ", "")
    return "PChtml" + catNoSpace + ".html"

def writeStyle(FW):
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>' + siteTitle + '</title>')
    FW.write('<link rel="stylesheet" href="flexCss.css">')

def writeNewHeader(FW):
    #FW.write('<h1><center>Mercedes Historic Photographs from the 1900s to 1950s</center></h1>')

    FW.write('<div id="flexHeader">')
    FW.write('<h1><center>Mercedes Texas Historic Photographs 1900s to 1950s</center></div></h1>')
    FW.write('<div id="flexHeader">')
    #FW.write('<div style="background-color:white; font-weight: bold;">Mercedes Historic Photographs from the 1900s to 1950s<br></div>')
    FW.write('<div>These photographs capture the early history of Mercedes, Texas. In the early 1900s, the city and the Lower Rio Grande Valley underwent a dramatic transformation, shifting from traditional ranching to commercial agriculture. This transition set the stage for unprecedented growth, marking an exciting yet challenging era in the regions development. During this time, irrigation and canal systems were established in Mercedes</div>')
    FW.write('<div2> Contact us if you have photographs or images to share on this website lisajensenstone@gmail.com.</div2>')
    FW.write('<div> The town built its own power plant. Mercedes was first in the Valley to have electric lights. Mercedes also served as the site of military camps during both the Border War and World War I. Do you have historical photographs from this period that you would like to share? We would be thrilled to add them to this website. Please reach out to us at mercedestx.gmail. Thank you for your interest in sharing the history of Mercedes</div>')
    FW.write('</div>')


def writeHeader(FW, title, desc, doButton):
    imageColorFile = 'imagesColorized/AloeVera.jpg'    
    FW.write('<div style="text-align:center;">')
    #FW.write('<div class="flex-wrap-subjects">')
    FW.write('<div><medium><b>'+ title + '</b></medium></div>') 
    #FW.write('<img src="'+ imageColorFile+ '">')    
    FW.write(desc + '<br>')
    if (doButton > 0):
        FW.write('<a href="PCSubjects.html" target="_blank">Home</a>')    
    FW.write('<br></div>')
    

def writeCitations(FW):
    htmlCitationsName = "PChtmlCitations.html"
    FW.write('<div>View source citations:  <a href=' + htmlCitationsName + '>' + 'View Citations </a></div>')
    

def writeColumn(FW, reader, isCitations):
        line = next(reader)
        subject = line["subject"]
        print(subject)
        key = line["key"]        
        imageFile = "imagesColorized/" + key + ".jpg"  
        print(subject)
        print(key)
        print(imageFile)
        
        if isCitations == 1:
            description = "Citations for Mercedes History Information"    
            imageColorFile = "imagesColorized/" + key + ".jpg"           
            htmlName= "PChtmlCitations.html"
        else:
            description = line["description"]    
            imageColorFile = "imagesColorized/" + key + ".jpg"           
            htmlName= makeHtmlSubjectFilename(subject);
            
        FW.write('<div class="column">')
        FW.write('<div class="flex-wrap-subjects"><img src="'+ imageColorFile+ '">')
        FW.write('<p class="b"><b><font color="red">' + subject + ' </font></b><br>')
        FW.write(description)
        FW.write('<br>')
        FW.write('<a href=' + htmlName + '>' + 'View Photos</a>')        

        #FW.write('<small>')

        #FW.write('<br><a href=' + htmlName + '>' + 'View</a>')
        #FW.write('</small>')
        FW.write('</div></div>')
        return subject

def writeSubjects():
    
    #https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01
    
    numSubjects = 18
    count = 0
    FH = open('postcardViewsSorted.csv')
    reader = csv.DictReader(FH)
    filename = "PCSubjects.html"
    FW= open(filename, "w+")
    writeStyle(FW)
    FW.write('</head><body>')
    writeNewHeader(FW)
    while (count < numSubjects):
        #start a new row
        FW.write('<div class="flex-wrap">')
        FW.write('<div class="row">')
        subject = writeColumn(FW, reader, 0)
        writeSubjectFile(subject)
        if count < 16:
            #start column 2
            subject = writeColumn(FW, reader,0)
            count+=1
            FW.write('<div><div><div>')
            writeSubjectFile(subject) 
        # the next is writing the citations
        if count == 16:  
            writeColumn(FW, reader, 1)
            count=count+1
            FW.write('<div><div><div>')
            
        count+=1
    FW.write('</body></html>')  
    count+=1
    FH.close() 
    FW.close()

def writeSubjectFile(subject):
 
    filename = htmlName= makeHtmlSubjectFilename(subject);
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
    writeHeader(FW, subject, siteTitle,1) 

    from itertools import islice
    with open('PostcardSorted.csv') as csvfile:
        reader1 = csv.reader(csvfile)       
        for row in islice(reader1, 172): 
           
            if row[subjectIdx] != subject: continue
            if row[scoreIdx] == "0": continue
            count = count + 1
            key = row[keyIdx]
            date = row[dateIdx]
            imageColorFile = "imagesColorized/" + key + ".jpg"
            imageBWFile    = "imagesBW/"        + key + ".jpg"    
            desc = row[descriptionIdx]
            heading = row[headingIdx]
            smu = row[smuIdx]
            
            #write out the row
            FW.write('<div class="flex-wrap"><img src="'+ imageColorFile+ '">')
            FW.write('<p class="b">')         
            FW.write('Card: <font color="blue"> ' + key + '</font> Date: ')            
            FW.write('<font color="blue">' + date + ' </font>') 
            FW.write('<font color="red"> <strong>' + heading + ' </strong></font><br>')   
            FW.write('<br>')
            FW.write(desc)
            FW.write('<br><br><a href=' + imageColorFile + '>' + 'View Enlarged</a> &nbsp; &nbsp;')
            if smu != "none":
                FW.write('<a href=' + 'https://digitalcollections.smu.edu/digital/collection/tex/id/' + smu   + '/>View High Resolution</a>')       
            FW.write('</div>')
            #end write out the row
            
        writeHeader(FW, siteTitle, subject, 1) 
        FW.write('</body></html>')

    print(subject)

writeSubjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
