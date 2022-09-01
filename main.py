from sre_constants import SUCCESS
from tokens import *
from create_file import *
from user_data.user_data import *

def main():
	#get necessary tokens
	xsrf_token = get_xsrf()
	anonymous_ID = get_anon()
	user_details = get_user_details(xsrf_token, anonymous_ID)
	redirect_token = get_redirect_token(user_details)
	cloud_session_token = get_cloud_token(xsrf_token, redirect_token)

	#send request to receive list of issues
	issues = get_issues(cloud_session_token)

	#ask user input for issueID and open or create a file
	key = input("Please enter the Issue Key (\"starts with FR-\"):\n").upper()
	if "FR-" not in key:
		key = "FR-" + key
	fd = open_or_create_file(issues, key)

	#parse all received information in the file and format it in the correct way
	format_file(fd, key, issues)
	exit(SUCCESS)

if __name__ == "__main__":
	main()
