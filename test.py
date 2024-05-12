import openai

openai.api_key = 'sk-proj-SIhTnSKO9NOetMBgGySxT3BlbkFJ3KKoGkEoODeFtO6AEp97'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the World Series in 2020?"}
  ]
)
print(response['choices'][0]['message']['content'])