import requests
from googleapiclient.discovery import build
with open('api.txt','r') as inp:
	api = inp.read(39)

blogId = "6857454394447135529"
pageId = "8562663751107014220"

blog = build('blogger','v3',developerKey=api)
response = blog.blogs().get(blogId = blogId).execute()
print(response)





'''
blogId = "6857454394447135529"
pageId = "8562663751107014220"
parameters = {
	'publish':True ,
	'key' : api
}

header={
	#Authorization: Bearer [YOUR_ACCESS_TOKEN],
	'Accept': 'application/json',
	'Content-Type': 'application/json'
}
url = 'https://blogger.googleapis.com/v3/blogs/{}/pages/{}'.format(blogId,pageId)
k2 = requests.post(url = url,params=parameters,header = header)
print(k2)
'''