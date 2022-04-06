# JiraTicketScraper

Hi, thanks for using the JiraTicketScraper.

This is designed to work on Amazon Workspaces and is only available for the front end of JiraTickets

JiraTicketScraper will ask you to enter a ticket ID, for example FR-722. It will then create a 
small report with all necessary information of that ticket inside of it. It will open the file
in gedit so make sure that you have that installed.

if not you can install it with: sudo yum install gedit

How to use:
-clone repository
-fill in email and passwd in the data.env file
-run main.py (python3 main.py)
-fill in the Ticket ID

!IMPORTANT!

Please remember to fill in your email and password that you use to login to jira in the data.env without spaces

for example:
username:email
password:pwd
