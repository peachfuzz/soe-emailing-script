from __future__ import print_function
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.base import MIMEBase
from email import encoders

path = '.'                                  #current directory
 
files = os.listdir(path)                    #gets all files in current directory

[x.encode('utf-8') for x in files]          #encoding the files


loadmess = "This is an important message. Please take a look at the file. If there are any errors, please reply back."
fromaddr = "your email"
#region, my pasword
password = "your email password goes here"
#endregion

#headless browser
#python - beautiful soup
#automate the boring stuff with python - free book

server = smtplib.SMTP('smtp.outlook.com', 587) #10 used to be 587, idk what the 587 is for
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)

for path in files:                          #for each file, format of name should be localpart_filedate_loadsheet
    localp = path.split('_')[0]             #local-part
    filedate = path.split('_')[1]           #file date
    toaddr = localp + "@spu.edu"
    print("attempting to send email to " + str(toaddr))
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Load sheet " + filedate

    html = """\
    <html>
        <head></head>
        <body>
            <p>
                Hello
                """ + loadmess + """ 
            </p>
        </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    print("attaching file")
    #attach file start
    part = MIMEBase('application', "octet-stream") 
    with open(path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(path)))
    msg.attach(part)
    #attach file end
    print("attached file")

    print("sending email to " + str(toaddr))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("sent email to " + str(toaddr))

    #server = smtplib.SMTP('mail') #idk what this is for
    server.set_debuglevel(True)  #show communication with the server, idk what this is for

try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()
    print("quit server?")
    
