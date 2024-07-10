from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    #system: instruções para o LLM
    {"role": "system", "content": "You are a helpful assistant."},
    #user: prompt enviado pelo usuário
    {"role": "user", "content": "Who won the world series in 2020?"},
    #assistant: a própria IA
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #user: prompt enviado pelo usuário
    {"role": "user", "content": "Where was it played?"}
  ]
)

#esse print mostra a resposta da IA para a última pergunta do usuário
print(response.choices[0].message.content)
