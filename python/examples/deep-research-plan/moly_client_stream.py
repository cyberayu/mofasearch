from openai import OpenAI

if __name__ == "__main__":
    client = OpenAI(base_url="http://127.0.0.1:8000/v3", api_key="sk-jsha-1234567890")

    user_input = '未来ai形态下 ai数据库可能的发展的形式和趋势是什么呢？'
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ], stream=True
    )
    for chunk in response:
        print(chunk)
        print("****************")