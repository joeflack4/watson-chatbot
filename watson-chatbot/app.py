import json
from watson_developer_cloud import ConversationV1

workspace_id = '38fdaa1a-a45b-410c-972f-d4ed5fe68ba2'
conversation = ConversationV1(
	username='a77159a6-130a-4333-8240-c6e0a40d88f4',
	password='Lje5RAaGtpHw',
	version='2016-09-20'
)


inputs = [
	'Show me a list of ADCs.',
	'hello'
]

for input in inputs:
	response = conversation.message(workspace_id=workspace_id, message_input={
	'text': input})
	json_response = json.dumps(response, indent=2)
	# print(json_response)
	output = response['output']['text'][0]
	print('You said: ' + input)
	print('Chatbot says: ' + output)