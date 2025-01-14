import xlrd # for opening an excel file to get the list of email-ids to send the mail.

import smtplib # this library is for using the protocol to send the mail. 

from email.message import EmailMessage # this library is used for formatting the mail. 

import imghdr # for checking the type of the image attached. 



# To read the html formatted file you want to share in mail. 
bodytemp = r'Path to your file'

with open(bodytemp,"r",encoding='utf-8') as f:  # 'content.txt' is the name of file which has the content.
        a = f.read()
        f.close()

# To access the image to be attached. 
with open ('Path to your image','rb') as f:
        img_file = f.read()
        img_type = imghdr.what(f.name)
        img_name = f.name


# To access the pdf to be attached
with open ('path to your pdf','rb') as f:
        pdf_file = f.read()
        pdf_name = f.name


# To access the excel sheet which contains the mails of the receiver. 
wb = xlrd.open_workbook("file-name") # 'mail-ids' is the name of excel file which contain mail-ids, take care of the file extension
sheet = wb.sheet_by_index(0)


# remove these comment when you will change your code
# here I will make some changes and make my own comments to tell you the changes I made.
#AADI I will add AADi after # to tell you that I have made this comment.


#AADI keeping only parameter with variable "i" in the loop
msg=EmailMessage()
msg['Subject']='Test OTP'  # Write the subject of you email here. 
msg['From']='From-email_id'

#AADI server start here
server= smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("From-email_id","password")

#AADI for loop start here
for i in range(sheet.nrows): #for sending the mails to each of the mail-id in the file. 
        
        msg['To']=sheet.cell_value(i,0)
#AADI        print(sheet.cell_value(i,0))  Why is there a print in the finished code? Just comment it out.
        msg.add_alternative(a, subtype='html')  # This is used to format the email content using html format. 
        server.send_message(msg) #AADI sending the message
# msg.add_attachment(img_file,maintype='image',subtype=img_type,filename=img_name) # for attaching images uncomment this.
# msg.add_attachment(pdf_file,maintype='application',subtype='octet-stream',filename=pdf_name) # for attaching pdfs uncomment this.

#AADI server quit here as no quit required in the for loop.
server.quit()