from flask import Flask, request, jsonify, render_template
import openai

# Initialize the Flask app
app = Flask(__name__)

# Configure OpenAI API key (replace 'your_openai_api_key' with your actual key)
openai.api_key 

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Health query API endpoint
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('query', '')
    if not user_input:
        return jsonify({"error": "Query cannot be empty."}), 400

    try:
        # Call OpenAI GPT for response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI health assistant. Provide helpful, accurate, and concise health information, but always recommend consulting a doctor for critical concerns."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
