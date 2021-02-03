import smtplib, email, os
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

filename_part1="obi"
file_ext=".mp4"
now = datetime.now()
current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
filename=filename_part1+file_ext
filepath="/home/pi/HM/"


subject='HouseMonitor captured a new montion on:  ' +current_datetime
bodyText="""\
Hello from Housemonitor,

The HouseMonitor system has detected a new motion. Please view the recording on the app Housemonitor.
The recording is attached here for permanent storage.

kind regards,

Obyat and Mansi
"""
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
USERNAME=''
PASSWORD=''
RECIEVER_EMAIL=''





def send_email():
 message=MIMEMultipart()
 message["From"]=USERNAME
 message["To"]=RECIEVER_EMAIL
 message["Subject"]=subject

 message.attach(MIMEText(bodyText, 'plain'))
 attachment=open(filepath+filename, "rb")

 mimeBase=MIMEBase('application','octet-stream')
 mimeBase.set_payload((attachment).read())

 encoders.encode_base64(mimeBase)
 mimeBase.add_header('Content-Disposition', "attachment; filename= " +filename)

 message.attach(mimeBase)
 text=message.as_string()

 session=smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 session.ehlo()
 session.starttls()
 session.ehlo()

 session.login(USERNAME, PASSWORD)
 session.sendmail(USERNAME, RECIEVER_EMAIL, text)
 session.quit


def capture_video():
 camera.start_preview()
 camera.start_recording('/home/pi/HM/newvideo.h264')
 camera.wait_recording(8)
 camera.stop_recording()
 camera.stop_preview()


def remove_file():
 if os.path.exists("/home/pi/HM/newvideo.h264"):
  os.remove("/home/pi/HM/newvideo.h264")
 else:
  print("file does not exist")

 if os.path.exists(filepath+filename):
  os.remove(filepath+filename)
 else:
  print("file does not exist")



camera=PiCamera()

while True:
 if GPIO.input(11)==1:
  print("Detected a new motion, recording...")
  capture_video()
  res=os.system("MP4Box -add /home/pi/HM/newvideo.h264 /home/pi/HM/newvideo.mp4")
  os.system("mv /home/pi/HM/newvideo.mp4 "+filepath+filename)
  send_email()