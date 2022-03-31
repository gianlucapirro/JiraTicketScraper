# open the data env file to parse the user_details
def	get_user_details(xrsf_token, anonymous_ID):
	with open("user_data/data.env", 'r') as data:
		data = str(data.read())
	data = data.split("DATA:")[1].strip().split("\n")
	user_details = {'state': {'csrfToken': xrsf_token, 'anonymousId': anonymous_ID}}
	for item in data:
		lst = item.split(":")
		user_details[lst[0]] = lst[1]
	return (user_details)