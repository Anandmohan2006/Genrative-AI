# from dotenv import load_dotenv

# load_dotenv()


# from langchain.chat_models import init_chat_model

# model = init_chat_model(
#     "mistral-small-latest",
#     model_provider="mistralai", temperature=1, max_output_tokens=55
# )



# # print(model.invoke("what is love?"))
# answer = model.invoke("why people fall in love? ")

# print(answer)


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key="YOUR_API_KEY"
)