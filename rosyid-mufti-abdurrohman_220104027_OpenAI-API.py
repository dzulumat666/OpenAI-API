import openai

# Pastikan Anda telah menginstal pustaka openai dengan menjalankan: pip install openai
openai.api_key = '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'

def chat_with_gpt(prompt):
    try:
        # Kirim permintaan ke API ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        # Ambil balasan dari respons
        reply = response['choices'][0]['message']['content']
        return reply

    except Exception as e:
        return f"Error: {str(e)}"

# Contoh penggunaan
user_input = input("Masukkan pertanyaan atau pernyataan Anda: ")
response = chat_with_gpt(user_input)
print("ChatGPT:", response)
