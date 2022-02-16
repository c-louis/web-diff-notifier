# Web Diff Notifier
This project is simple python project to setup as a Cron Task to receive a mail when a website content has changed

# Requirement
* A server working 24/24
* A gmail address to send the mails
* The data you want to inspect

# How to use
1. Clone the project
	* git clone https://github.com/c-louis/web-diff-notifier.git
2. Install script requirement
	* pip3 install yagmail requests python-dotenv
3. Prepare `to-find.wd`
	* The first line should be the URL of the page you want to lookup
	* All the rest of the file should be the data you want to know if present on the page
		* Can be as HTML, in this case it should be an exact copy of the page current html code (Even newline and invisible characters
		* Can be a simple string
			If there is content before or after your string the string will not consider it, example :
			If your string is : "I am the poli"
			The webpages :
				* "PoI am the poli"  -> will match as identical
				* "I am the polia" -> will match as identical
				* "I am the pola" -> will not match as identical
	* BE CAREFULL ABOUT LAST NEWLINE ADDED BY SOME FILES EDITOR
4. Make the CRON Task on your server
	* Tutorial : https://phoenixnap.com/kb/set-up-cron-job-linux
	* CRON format help : https://crontab.guru/
