from __future__ import print_function
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#this is where you can type up your response -> https://wordtohtml.net/
#Type your response in the visual editor and whatever appears in the HTML editor
#copy/paste it in between the """  """
#here is an example:
example = """
<p>This is the text that will appear in my email</p>
"""
#this is where you will need to add your message, including your signature
loadmess = """
To whom it may concern,<br/>
This is important and I need you to see it<br/>
best,<br/>
Hector
           """
loadmess = loadmess
fromaddr = "Enter your SPU email here"
#region, my pasword
password = "Enter your SPU password here"
#endregion

path = '.'                                  #current directory
files = os.listdir(path)                    #gets all files in current directory

server = smtplib.SMTP('smtp.outlook.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)            #login

for path in files:                          #for each file, format of name should be localpart_filedate_loadsheet
    if ".xlsx" in path:                         #only sending excel files
        localp = path.split('_')[0]             #email, local part
        filedate = path.split('_')[1]           #date data was retrieved
        filecontents = path.split('.')[0]       #contents of file
        toaddr = localp + "@spu.edu"
        print("attempting to send email to " + str(toaddr))
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = filecontents + " " + filedate

        html = """\
        <html>
            <head></head>
            <body>
                    <p>""" + loadmess + """</p>
            </body>
        </html>
        """

        msg.attach(MIMEText(html, 'html'))

        path.encode('utf-8') #encode file
        #attach file start
        part = MIMEBase('application', "octet-stream") 
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(path)))
        msg.attach(part)
        #attach file end

        text = msg.as_string()
        
        server.sendmail(fromaddr, toaddr, text)
        print("sent email to " + str(toaddr))

        #server = smtplib.SMTP('mail') #idk what this is for but it makes the app break
        server.set_debuglevel(True)  #show communication with the server, idk what this is for
try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()