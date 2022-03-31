import json
import requests
import sys
import os
import queries as queries

# send request with cloud.session.token to receive a list of issues
def get_issues(cloud_session_token):
	cookies = {'cloud.session.token': cloud_session_token}
	params = {'rapidViewId': '7'}
	response = requests.get('https://thalex.atlassian.net/rest/greenhopper/1.0/xboard/work/allData.json', cookies=cookies, params=params)
	if response.status_code != 200:
		sys.exit("Invalid status code on response get_issues")
	response = json.loads(response.text)['issuesData']['issues']
	issues = {}
	for item in response:
		issues[item['key']] = item['summary']
	return (issues)


# send request with anonymousID, xsrf token, cloud_session_token and the issueID to receive the matching issue description
def get_description(anonymous_ID, xsrf_token, cloud_session_token, key):
	cookies = {'ajs_anonymous_id': anonymous_ID, 'atlassian.xsrf.token': xsrf_token, 'cloud.session.token': cloud_session_token}
	queries.description['query'] = queries.description['query'].format(KEY=key)
	response = requests.post('https://thalex.atlassian.net/rest/graphql/1/', cookies=cookies, json=queries.description)
	response = json.loads(response.text)
	for item in response['data']['issue']['fields']:
		if 'description' in item.values():
			return(item['content'])


# opens the file with key as name if it exists otherwhise it will create a file
def open_or_create_file(issues, key):
	if key not in issues:
		sys.exit("Key: \"" + key + "\" not found in Issues")
	fd = open(str(key), 'w+')
	return (fd)


# formats the file with the passed fd and format all information in the file
def format_file(fd, key, issues, description):
	fd.write("ISSUE ID: \n\t" + str(key) + "\n")
	fd.write("ISSUE: \n\t" + str(issues[key]) + "\n")
	fd.write("DESCRIPTION\n\t" + description)
	fd.close()
	os.system("./get_browser_versions.sh >> " + str(key))
	os.system("gedit " + str(key))
