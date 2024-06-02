import openai
import os

# 환경 변수에서 OpenAI API 키 읽어오기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = api_key

# Define the input text
input_text = """
John Doe
123 Main St, Springfield, IL 62701
Phone: (555) 123-4567
Email: john.doe@example.com
"""

# Create a request to extract name, contact details, and address
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a data extraction assistant."},
        {"role": "user", "content": f"Extract the name, contact details, and address from the following profile text:\n{input_text}"}
    ],
    max_tokens=1000,
    temperature=0.5
)


# Print the extracted information
extracted_info = response['choices'][0]['message']['content'].strip()
print(extracted_info)
