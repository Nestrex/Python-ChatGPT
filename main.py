
import openai

# GPT-3 API anahtarınızı buraya girin
api_key = 'YOUR_API_KEY'

# OpenAI API'sine bağlanın
openai.api_key = api_key

# Chatbot için bir soru veya girdi alın
girdi = input("Soru veya girdi: ")

# GPT-3 API'sini kullanarak chatbotunuzdan bir yanıt alın
yanit = openai.Completion.create(
  prompt=girdi,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.7
)

# Yanıtı ekrana yazdırın
print(yanit.choices[0].text)
