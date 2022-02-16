#!/usr/bin/python3

import requests
import sys
import yagmail
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

def sendMail(url, contentToFind):
	yag = yagmail.SMTP(os.environ['GMAIL_USER'], os.environ['GMAIL_PASS'])
	o = urlparse(url)
	subject = f'Hey ! The website : {o.hostname} changed !'
	content = f'\
<h1>Website : {o.hostname}</h1>\
<h3>Page requested : {url}</h3>\
<h4>Content Requested :</h4>\
<p>{contentToFind}</p>\
'
	yag.send(subject=subject, contents=content)
	print('Mail Sended')


def main():
	contentToFind = ''
	urlToSearch = ''
	with open('to-find.wd') as tf:
		urlToSearch = tf.readline().strip()
		contentToFind = tf.read()

	print('__________ Will search on : __________')
	print(urlToSearch)
	print('__________ Will try to find : __________')
	print(contentToFind)

	request = requests.get(urlToSearch)
	if request.status_code != 200:
		print(f'Request failed with status : {request.status_code}')
		sys.exit(1)

	result = request.text

	res = result.find(contentToFind)
	if res == -1:
		print(f'Content changed ! {res}')
		sendMail(urlToSearch, contentToFind)
	else:
		print(f'Found same content : {res}')

if __name__=='__main__':
	load_dotenv()
	sys.exit(main())