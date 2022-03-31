import json
from sre_constants import SUCCESS
import requests
import sys

# send request to 'https://id.atlassian.com/login' and read the response.cookies to parse the XSRF token
# if we receive invalid response we exit
def get_xsrf():
	response = requests.get('https://id.atlassian.com/login')
	if response.status_code != 200:
		sys.exit("Invalid status code on response get_xsrf")
	xsrf_token = response.cookies['atlassian.account.xsrf.token']
	return(xsrf_token)


# send request to 'https://www.atlassian.com/nl/software/jira' and read the response.headers to parse the anonymous_id
# if we receive invalid response we exit
def get_anon():
	response = requests.get('https://www.atlassian.com/nl/software/jira')
	if response.status_code != 200:
		sys.exit("Invalid status code on response get_anon")
	anonymous_ID = response.headers['Set-Cookie'].split('ajs_anonymous_id=')[1].split(';')[0]
	return (anonymous_ID)


# send request to 'https://auth.atlassian.com/co/authenticate?email={USERNAME}&errorCode' with user details as json_data
# and read the response.text we receive the redirect URL and we pasrse the redirect_token out of the URL
# if we receive invalid response we exit
def get_redirect_token(user_details):
	url = "https://auth.atlassian.com/co/authenticate?email=" + user_details['username'] + "&errorCode"
	response = requests.post(url, json=user_details)
	if response.status_code != 200:
		sys.exit("Invalid status code on response get_redirect_token")
	data = json.loads(response.text)
	redirect_token = data['redirectUri'].split('token=')[1]
	return (redirect_token)


# send an authorization request to 'https://id.atlassian.com/login/authorize' with XSRF token as cookie and redirect_token as parameter
# to receive the cloud.session.token
def get_cloud_token(xsrf_token, redirect_token):
	cookies = {'atlassian.account.xsrf.token': xsrf_token}
	params = {'token': redirect_token}
	response = requests.get('https://id.atlassian.com/login/authorize', params=params, cookies=cookies)
	if response.status_code != 200:
		sys.exit("Invalid status code on response get_cloud_token")
	cloud_session_token = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
	return (cloud_session_token)