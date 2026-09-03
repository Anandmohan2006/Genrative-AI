from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key="YOUR_API_KEY"
)






from langchain.chat_models import init_chat_model

model = init_chat_model(
    "mistral-small-latest",
    model_provider="mistralai", temperature=1
)

prompt = input("you: ")
response = model.invoke(prompt)
print("bot:", response)





