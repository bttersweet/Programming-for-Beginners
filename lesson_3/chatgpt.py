import openai

# String
my_api_key = "sk-xxxxx"
model_name = "gpt-3.5-turbo"

# Integer
n = 2

# Float
temperature = 1.2

# Dictionary
message_1 = {"role": "system", "content": "You are a helpful assistant."}
message_2 = {"role": "user", "content": "Who are you?"}
message_3 = {"role": "assistant", "content": "My name is Leona."}
message_4 = {"role": "user", "content": "What is your name?"}

# List, Array
messages = [message_1, message_2, message_3, message_4]

openai.api_key = my_api_key

reponse = openai.ChatCompletion.create(
	model=model_name,
	messages=messages,
	n=n,
	temperature=temperature
)

print(reponse)