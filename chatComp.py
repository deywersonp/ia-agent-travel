from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    #system: instruções para o LLM
    {"role": "system", "content": "You are a helpful assistant."},
    #user: prompt enviado pelo usuário
    {"role": "user", "content": "Vou viajar em Agosto de 2024 para Londres e quero um roteiro de viagens"}
  ]
)

#esse print mostra a resposta da IA para a última pergunta do usuário
print(response.choices[0].message.content)
