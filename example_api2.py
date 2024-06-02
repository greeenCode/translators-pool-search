import openai
import os

# 환경 변수에서 OpenAI API 키 읽어오기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = api_key

# Define the input text
# Read input text from a file
with open("abba\extracted\곽민희.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

# Read promt text from a file
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()


# Create a request to extract name, contact details, and address
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a data extraction assistant."},
        {"role": "user", "content": f"{prompt}:\n{input_text}"}
    ],
    max_tokens=1500,
    temperature=0.5
)


# Print the extracted information
extracted_info = response['choices'][0]['message']['content'].strip()
print(extracted_info)
