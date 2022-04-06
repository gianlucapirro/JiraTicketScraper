# JiraTicketScraper

Hi, thanks for using the JiraTicketScraper.

This is designed to work on Amazon Workspaces and is only available for the front end of JiraTickets

This TicketScraper will grab all necessary information from the KanBan board and parse it into a structured file. 
No more copy pasting to write your review of the ticket. Simply fill in the ticket ID of the jira ticket and everything will 
be done for you.

It will try to open the file in gedit so make sure that you have it installed.

#### if not you can install it with: <br>
* sudo yum install gedit

## How to use: <br>
* Clone repository<br>
* Fill in email and passwd in the data.env file<br>
* Run main.py (python3 main.py)<br>
* Fill in the Ticket ID<br>

### IMPORTANT <br>
Please remember to fill in your email and password that you use to login to jira in the data.env without spaces<br>
for example:<br>
* username:email<br>
* password:pwd<br>
 
