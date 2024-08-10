# IBM-Chatbot

This project provides a tool for querying IBM Watson's AI model about carbon footprint topics using the IBM Cloud Text Generation API.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a Python environment set up (Python 3.6 or later recommended)
* You have an IBM Cloud account and API key
* You have access to the IBM Watson Text Generation API

## Installation

1. Clone this repository to your local machine.

2. Install the required Python packages:  `pip install ibm_watson` and `pip install requests`

## Configuration

1. Open the script file.

2. Replace `'Enter your API key here.'` with your actual IBM Cloud API key.

3. Replace `'Enter your generated token here.'` in the `Authorization` header with your generated Bearer token. Make sure to keep the word 'Bearer' at the beginning.

## Usage

1. Run the script:
   `python your_script_name.py`


2. When prompted, enter your query about carbon footprint.

3. The script will send your query to the IBM Watson AI model and display the response.

## How It Works

1. The script first generates an IAM token using your IBM Cloud API key.
2. It then prompts the user for a query about carbon footprint.
3. The query is sent to the IBM Watson Text Generation API along with specific parameters to control the response.
4. The API's response is then processed and displayed to the user.

## Features

- Uses the meta-llama/llama-3-405b-instruct model for text generation
- Implements moderation to ensure appropriate content
- Limits the response to a maximum of 200 tokens
- Uses stop sequences to prevent the generation of follow-up questions
- Implements a repetition penalty to improve response quality

## Important Notes

- The generated IAM token expires after 1 hour. For continuous use, you should implement a mechanism to refresh the token periodically.
- Ensure your API key and generated tokens are kept secure and not shared publicly.
- The project is set up to query specifically about carbon footprint topics. Modify the input prompt in the code if you want to use it for different topics.

## Troubleshooting

If you encounter a "Non-200 response" error, check the following:
1. Ensure your API key is correct and has the necessary permissions.
2. Verify that your Bearer token is valid and correctly formatted in the Authorization header.
3. Check your IBM Cloud account status and ensure you have access to the required services.

## Contributing

Contributions to this project are welcome. Please ensure you update tests as appropriate.


## Contact

If you have any questions or feedback, please contact kdurgaprasadkavali@gmail.com

