#change log
#12/20/2024 Fixed missing cards: A110 and 0102 had to be copied from "additonal" directory to imagesColorized
#12/20/2024 Had to edit the postcards csv file to remove "copy" form the key for "A110". Not sure how it get there
import csv

siteTitle = "Mercedes Historic Image Collective"

def makeHtmlSubjectFilename(category):  
    catNoSpace = category.replace(" ", "")
    return "PChtml" + catNoSpace + ".html"


def writeStyle(FW):
    FW.write('<style>')
    FW.write('font-family: {Arial, Helvetic, sans-serif;}')
    FW.write('.flex-wrap {display: flex; align-items: flex-start; gap: 15px;}')
    FW.write('.flex-wrap img {max-width: 30%; height: auto; }')
    FW.write('.flex-wrap p {flex: 1;background-color: Linen;}')
    
    
    FW.write('.flex-wrap-subjects {display: flex; align-items: flex-start; gap: 15px;}')
    FW.write('.flex-wrap-subjects img {max-width: 25%; height: auto; }')
    FW.write('.flex-wrap-subjects p {flex: 1;}')
    
    FW.write('.row {display: flex; flex-direction: row;flex-wrap: wrap;width: 100%;}')
    FW.write('.column {display: flex;flex-direction: column;ex-basis: 100%;flex: 1;!background-color: Ivory;!height: 100px;}')

    FW.write('p.a {font-family: Arial, Helvetic, sans-serif;}')
    FW.write('p.b {font-family: Arial, Helvetic, sans-serif;}')
    
    FW.write('a:link, a:visited {background-color: turquoise;color: white;padding: 5px 15px;text-align: center;text-decoration: none;display: inline-block;border-radius:8px}')
    FW.write('a:hover, a:active {background-color: teal;}')
 
    
    FW.write('</style>')

def writeHeader(FW, title, desc, doButton):
    imageColorFile = 'imagesColorized/AloeVera.jpg'    
    FW.write('<div style="text-align:center;">')
    #FW.write('<div class="flex-wrap-subjects">')
    FW.write('<large><b>'+ title + '</b></large><br>') 

 
    #FW.write('<img src="'+ imageColorFile+ '">')    
    FW.write(desc + '<br>')
    if (doButton > 0):
        FW.write('<a href="PCSubjects.html" target="_blank">Home</a>')    
    FW.write('<br></div>')
    
def writeAbout(FW):
    FH = open('aboutArchive.csv')
    reader = csv.DictReader(FH)    
    line = next(reader)
    subject = line["subject"]
    desc = line["description"]
    writeHeader(FW, subject, desc, 0)
    FH.close() 

def writeCitations(FW):
    htmlCitationsName = "PChtmlCitations.html"
    FW.write('<div>View source citations:  <a href=' + htmlCitationsName + '>' + 'View Citations </a></div>')
    

def writeColumn(FW, imageColorFile, subject, description, htmlName):
        FW.write('<div class="column">')
        FW.write('<div class="flex-wrap-subjects"><img src="'+ imageColorFile+ '">')
        FW.write('<p class="b"><b><font color="red">' + subject + ' </font>') 
        FW.write('</b><br>')
        FW.write('<small>')
        FW.write(description)
        FW.write('<br><a href=' + htmlName + '>' + 'View</a>')
        FW.write('</small>')
        FW.write('</div></div>')

def writeSubjects():
    
    #https://dev.to/drews256/ridiculously-easy-row-and-column-layouts-with-flexbox-1k01
    
    numSubjects = 18
    count = 0
    FH = open('postcardViewsSorted.csv')
    reader = csv.DictReader(FH)
    
    filename = "PCSubjects.html"
    FW= open(filename, "w+")
    
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>Mercedes Photographs</title>')
    writeStyle(FW)
    FW.write('</head><body>')
    writeAbout(FW)
    while (count < numSubjects):
        
        #start a new row
        FW.write('<div class="flex-wrap">')
        FW.write('<div class="row">')
        
        
        #start column 1
        line = next(reader)
        subject = line["subject"]
        key = line["key"]        
        imageFile = "imagesColorized/" + key + ".jpg"  
        description = line["description"]    
        imageColorFile = "imagesColorized/" + key + ".jpg"           
        htmlName= makeHtmlSubjectFilename(subject);
        writeColumn(FW, imageColorFile, subject, description, htmlName)
        writeSubjectFile(subject)

        if count < 16:
            #start column 2
            line = next(reader)        
            subject = line["subject"]
            key = line["key"]        
            imageFile = "imagesColorized/" + key + ".jpg"  
            description = line["description"]    
            imageColorFile = "imagesColorized/" + key + ".jpg"           
            htmlName= makeHtmlSubjectFilename(subject);
            writeColumn(FW, imageColorFile, subject, description, htmlName)

            #end row
            count=count+1
            FW.write('<div>')
            FW.write('<div>')
            FW.write('<div>')
            writeSubjectFile(subject) 
           
           
        # the next is writing the citations
        if count == 16:  
            #start column 2
            line = next(reader)        
            subject = line["subject"]
            key = line["key"]        
            imageFile = "imagesColorized/" + key + ".jpg"  
            description = "Citations for Mercedes History Information"    
            imageColorFile = "imagesColorized/" + key + ".jpg"           
            htmlName= "PChtmlCitations.html"
            writeColumn(FW, imageColorFile, subject, description, htmlName)
            count=count+1
            
            #end row
            FW.write('<div>')
            FW.write('<div>')
            FW.write('<div>')
            
        count=count+1
        print(count)

    FW.write('</body></html>')  
    count=count+1
    FH.close() 
    FW.close()

def writeSubjectFile(subject):
 
    filename = htmlName= makeHtmlSubjectFilename(subject);
    #This file was created by exporting the postcards table from wix, then editing to remove single quotes, 
    #then editing it in Open Office Calc to sort on the score column
    

    count=0
    error=0
    smu="5517"
    keyIdx = 0
    smuIdx = 1
    scoreIdx =2
    headingIdx =3
    subjectIdx =4
    dateIdx =5
    descriptionIdx =6
    title = 'Mercedes Historic Photos' 
    
    FW= open(filename, "w+") 
    FW.write('<!DOCTYPE html>')
    FW.write('<html lang="en">')
    FW.write('<head>')
    FW.write('<meta charset="UTF-8">')
    FW.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    FW.write('<title>Mercedes Historic Photos ' + title + '</title>')
    
    writeStyle(FW)
    
    FW.write('</head><body><div>')
    writeHeader(FW, title, subject, 1) 
    FW.write('<small>')
    
  
    FW.write('<div class="flex-wrap">')
    FW.write('<p class="b">')         
    FW.write("Camp Llano Grande was located near Mercedes and about five miles from the Rio Grande on a flat 200-acre site. It was served by a rail line and had a flag depot, but other than the main house, which became the camp hospital, and an old ranch house that became camp headquarters, there was little else in place when troops first arrived. Their arrival precipitated a flurry of activity")
    FW.write('<p class="a">')   
    FW.write("Camp Llano Grande was located near Mercedes and about five miles from the Rio Grande on a flat 200-acre site. It was served by a rail line and had a flag depot, but other than the main house, which became the camp hospital, and an old ranch house that became camp headquarters, there was little else in place when troops first arrived. Their arrival precipitated a flurry of activity")

    #FW.write('<p class="b">') 
    #FW.write('<div class="flex-wrap"><img src="imagesColorized/A001.jpg">')
    #FW.write('<p class="flex-wrap"><img src="imagesColorized/A001.jpg">')
    #FW.write('<img src="imagesColorized/A001.jpg"; max-width=100%; height=auto>')
    #FW.write('<img src="imagesColorized/A001.jpg">')
    #FW.write('</div>')   
    FW.write('<p class="b">')   
    FW.write("Company areas were laid out, ditches dug for drainage, and brush cleared; latrines dug; incinerators erected; water pipes laid and buried. Structures were erected for kitchens and mess halls. Small wooden houses were built for officers, and platforms were built to keep the soldiers' tents off the ground")
    #FW.write('<div class="flex-wrap"><img src="imagesColorized/A001.jpg">')
    #FW.write('<img src="imagesColorized/A001.jpg">')
    FW.write('</div>')
    

    from itertools import islice
    with open('PostcardCorrectedQuotesSorted.csv') as csvfile:
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
            
        writeHeader(FW, 'Mercedes History Collective', subject, 1) 
        FW.write('</body></html>')

    print(subject)
    print(count)

writeSubjectFile("Irrigation")

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
