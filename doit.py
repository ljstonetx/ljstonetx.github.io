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

#todo: card rio rico gambling - view article not working:
#infrastructure: U149, U149 need info, are these from UTRGV


import csv
from itertools import islice


SITE_SHORT_TITLE = "Mercedes Historic Photographs"
SITE_LONG_TITLE = "Mercedes Texas 1900s to 1950s History and Images"
EMAIL_ADDRESS = "mercedestx@gmail.com"

POSTCARD_FILE = 'PostcardSorted.csv'
SUBJECTS_FILE = 'postcardViewsSorted.csv'
HISTORY_FILE = 'History.csv'
HISTORY_TEXT_FILE = 'historyText.csv'
SUBJECTS_HTML = 'index.html'
ABOUT_HTML = 'about.html'
COLOR_IMAGE_DIR = 'imagesColorized/'
CITATIONS_FILE = 'Citations.pdf'
CITATIONS_TITLE = "Citations for Mercedes History Information"


conAbout= "<div><p1>"+ SITE_LONG_TITLE + " provides links to images provided by the DeGolyer Library at Southern Methodist University, Texas Digital Archive, the University of Texas Rio Grande Valley and Dr. Hector P. Garcia Memorial Library via The Portal to Texas History. For individual image citations, press the View Library button by the image. <br><br> Historic information was derived from over 100 sources, with the local newspaper serving as the primary reference. Additionally, numerous books, articles, and websites have contributed valuable insights. We have made every effort to properly acknowledge these sources on the Citations page. <a href=" + CITATIONS_FILE +" class='button'>View Citations </a><br><br>Please send questions and  feedback to mercedesimages@gmail.com.<div></p1>"


conMercedesTx =  "This website offers a glimpse into the early history of Mercedes, Texas. In the early 1900s, Mercedes and the Lower Rio Grande Valley underwent a transformative moving from traditional ranching to commercial agriculture. This set the stage for significant growthshift,moving from traditional ranching to commercial agriculture. This set and marked a dynamic period in the regional development. Explore the images which record era organized here by category." 


# --- Constants ---




SOURCE_LINKS = {
    "SMU": 'https://digitalcollections.smu.edu/digital/collection/tex/id/',
    "UTRGVSTUDIO": 'https://scholarworks.utrgv.edu/rgvstudio/',
    "UTRGVMISC": 'https://scholarworks.utrgv.edu/miscphotosedinburg/',
    "UTRGVMISCBROWN": 'https://scholarworks.utrgv.edu/miscphotosbrownsville/',
    "UTRGVHIDAL": 'https://scholarworks.utrgv.edu/hidalgohist_aa/',
    "TXHISARC": 'https://tsl.access.preservica.com/uncategorized/'
}
conOTHER       = "OTHER"
conNONE       = "NONE"

#colors
#COLOR_TITLE = "#cc0000"
#COLOR_DATE =  "#414141"

COLOR_TITLE = "#b22222"   # Firebrick – a deeper red, still bold but less harsh
COLOR_DATE = "#555555"    # Medium-dark gray – softer and more legible than #414141

# --- Utility Functions ---
def make_html_filename(subject):
    return CITATIONS_FILE if subject == "Citations" else f"PChtml{subject.replace(' ', '')}.html"

def make_image_path(key):
    return f"{COLOR_IMAGE_DIR}{key}.jpg"

def make_history_image_path(key):
    return f"{COLOR_IMAGE_DIR}{key}"
    
def write_image(fw, image_path):
    #fw.write(f'<div class="flex-wrap"><img src="{image_path}"></div>\n')
    fw.write('<div class="flex-wrap"><img src="'+ image_path+ '">')

def write_image_enlarged(fw, image_path):
    fw.write(f'<a href="{image_path}" class="button">View Enlarged</a>&nbsp;&nbsp;\n')

def write_style(fw):
    fw.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{SITE_SHORT_TITLE}</title>
<link rel="stylesheet" href="flexCss.css">
</head>
<body><div>
''')



def write_history_title(FW, title):
    FW.write('<p1><div>')
    FW.write('<font color="+COLOR_TITLE"+"> <strong>' + title + ' </strong></font>')
    
def write_title(FW, title):
    FW.write('<font color="+COLOR_TITLE"+"> <strong>' + title + ' </strong></font>')

def write_header(FW, subject, heading):
    FW.write('<div id="flexHeader">')
    FW.write('<p2>' + heading + '<br><br><a href=' + SUBJECTS_HTML + ' class="button" target="_blank">Home</a>'+ '</p2></div>')
    FW.write('<div id="flexHeader">')
    FW.write('</div><br>')

def write_citations(FW):
    FW.write('<a href=' + CITATIONS_FILE + 'class="button">' + 'View Citations </a>')

def write_date(fw, date):
    fw.write('<font color='+COLOR_DATE+'>'+date+'</font>\n')

def write_description(fw, description):
    fw.write(f'<br><br><p1>{description}</p1><br><br>\n')
    
def write_source_link(fw, source, source_id):
    if source == "NONE": return
    if source in SOURCE_LINKS:
        fw.write(f'<a href="{SOURCE_LINKS[source]}{source_id}" class="button">View Library</a>&nbsp;&nbsp;\n')
    else:
        fw.write(f'<a href="{source_id}" class="button">View Source Article</a>\n')


def write_heading(fw, heading, is_home=False):
    fw.write('<div id="flexHeader">\n')
    if is_home:
        fw.write(f'<p2>{heading}<br><br><a href="{ABOUT_HTML}" class="button" target="_blank">About</a></p2>\n')
    else:
        fw.write(f'<p2>{heading}<br><br><a href="{SUBJECTS_HTML}" class="button" target="_blank">Go Home</a></p2>\n')
    fw.write('</div><br>\n')

def write_home_intro(fw, heading):
    write_heading(fw, SITE_LONG_TITLE, is_home=True)
    
    fw.write('<div id="flexHeader">\n')
    intro = (
        "<p3>" + heading + "</p3></div><br>"
    )
    fw.write(intro)

def write_subject_intro(fw, heading):
     
    fw.write('<div id="flexHeader">\n')
    intro = (
        "<p3>" + heading + "</p3></div><br>"
    )
    fw.write(intro)

def write_about():
    with open(ABOUT_HTML, "w", encoding="utf-8") as fw:
        write_style(fw)
        #write_home_intro(fw,conAbout )
        write_heading(fw, SITE_LONG_TITLE)
     
        fw.write('<div id="flexHeader">\n')
        intro = (
        "<p3>" + conAbout + "</p3></div><br>"
        )     
        fw.write(intro)
        
        image_path = make_image_path("E006")       
        write_image(fw, image_path)

def write_subjects():
    with open(SUBJECTS_HTML, "w", encoding="utf-8") as fw:
        write_style(fw)
        write_home_intro(fw, conMercedesTx)

        with open(SUBJECTS_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)     
            for line in islice(reader,1, None):
               subject, _, key, description, heading = line[:5]
               
               image_path = make_image_path(key)
               write_image(fw, image_path)
               fw.write('<p1>')
               write_title(fw, heading) 
               
               write_description(fw, description)
               htmlName= make_html_filename(subject);
               fw.write('<a href=' + htmlName         + ' class="button">' + 'View '+ subject + '</a>')
               fw.write('</div><br>')
               
               if subject in {"Fuste", "Colegio", "Rio Rico"}:
                    write_history_subject(subject,heading, description)
               elif (subject != "Citations"):
                # Citations.pdf file was made by importing citations.csv into a google doc, format order as
                # number, wrapping the citation column, and exporting to pdf. Then copying file to source code directory               
                   
                write_postcard_subject(subject, heading, description)

        #write_citations(fw)
        write_heading(fw, SITE_LONG_TITLE, heading)
        fw.write('</body></html>')



def write_postcard_subject(subject, heading, description):
    filename = make_html_filename(subject)
    with open(filename, "w", encoding="utf-8") as fw:
        write_style(fw)
        write_heading(fw, heading)
        write_subject_intro(fw, description)
        with open(POSTCARD_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            for row in islice(reader,1,None):   #start at row 1, None = go to end
                if row[5] != subject or row[3] == "0": continue

                key, source, source_id, _, heading_text, _, date, description = row[:8]
                image_path = make_image_path(key)
                write_image(fw, image_path)
                fw.write('<p1>') #added
                write_date(fw, key)
                write_title(fw, heading_text)
                write_date(fw, date)
                write_description(fw, description)
                write_image_enlarged(fw, image_path)
                write_source_link(fw, source, source_id)               
                fw.write('<br><br>') #added
                fw.write('</div>')   #added
                

        write_heading(fw, heading)
        fw.write('</body></html>')
            
def write_history_subject(subject, heading, description):
    subjectIdx = 1
    filename = make_html_filename(subject)
    with open(filename, "w", encoding="utf-8") as fw:
        write_style(fw)
        write_heading(fw, heading)
        write_subject_intro(fw, description)
        with open(HISTORY_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in islice(reader,1,None):
                if row[subjectIdx] != subject: continue
                title, _, image, citation_text, date, summary, link = row[:7]
                image_path = make_history_image_path(image)
                write_image(fw, image_path)
                write_history_title(fw,title)
                write_date(fw, date)
                write_description(fw, summary)
                write_image_enlarged(fw, image_path)
                write_source_link(fw, "OTHER", link)
                fw.write('</div></div><br><br>')

        write_heading(fw, heading)
        fw.write('</body></html>')

write_about()
write_subjects()

#check this out https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flexbox-tricks
