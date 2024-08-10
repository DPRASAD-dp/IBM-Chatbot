import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

user_input = input("Please enter your query\n")

body = {
	 "input": "Provide a concise, focused answer to the following question about carbon footprint. Do not generate any follow-up questions or additional topics." + user_input,
	"parameters": {
		"decoding_method": "greedy",
		"max_new_tokens": 200,
		"stop_sequences": ["\"What\"","\"How\"","\"Why\"","\"Would\"","\"Can\"","\"Is\""],
		"repetition_penalty": 1.5
	},
	"model_id": "meta-llama/llama-3-405b-instruct",
	"project_id": "1a28e7b5-592d-4083-9d64-75491cdde1c2",
	"moderations": {
		"hap": {
			"input": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			},
			"output": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			}
		}
	}
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer Enter your generated token here.Dont remove the 'Bearer' at the beginning"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

# Extract and format the response
data = response.json()
