# app.py
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/zapier-hook', methods=['POST'])
def zapier_hook():
    data = request.json
    # Extract relevant info
    title = data.get('title', 'No Title')
    description = data.get('description', 'No Description')

    # Send to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Chief of Staff assistant."},
            {"role": "user", "content": f"Add this event: {title} - {description}"}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000)
