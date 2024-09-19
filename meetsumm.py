import os
from flask import Flask, request, jsonify
from flask_cors import CORS 
from ibm_watsonx_ai.foundation_models import Model
from dotenv import load_dotenv
from asgiref.wsgi import WsgiToAsgi

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": os.getenv('API_KEY')
    }

model_id = "ibm/granite-13b-chat-v2"

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1.05
}

project_id = os.getenv('PROJECT_ID')

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=get_credentials(),
    project_id=project_id,
)

prompt_input = """<|system|>
You are an advanced AI model built to deliver comprehensive and precise Meeting Conversation Summaries. You specialize in creating structured, clear, and concise Minutes of Meeting (MoM) by identifying key discussion points, action items, and decisions. You will receive meeting inputs with attendees and their designations, followed by their statements. 

Use this input format:

Attendee 1 (with their designation): [Statement]
Attendee 2 (with their designation): [Statement]

Based on this input, extract the relevant details and return a fully structured JSON containing:
1. A meeting title
2. A summary of the discussion
3. A list of attendees and their designations
4. Action items with assigned owners and due dates
5. Decisions made during the meeting

Always return responses in the following strict JSON format:


{
  "title": "Meeting Title",
  "summary": "A concise overview of the meeting discussion.",
  "attendees": [
    {
      "name": "Attendee 1",
      "designation": "Attendee 1's designation"
    },
    {
      "name": "Attendee 2",
      "designation": "Attendee 2's designation"
    }
  ],
  "date": "YYYY-MM-DD",
  "action_items": [
    {
      "task": "Description of the task",
      "owner": "Assigned person",
      "due_date": "YYYY-MM-DD"
    }
  ],
  "decisions": [
    {
      "decision": "Description of the decision made",
      "made_by": "Person or group who made the decision"
    }
  ]
}

Ensure that:
- The **summary** accurately captures the main points discussed.
- **Action items** are clearly defined with tasks, owners, and due dates.
- **Decisions** reflect critical conclusions or agreements made during the meeting.

Return only the JSON response without any additional text or explanation.

"""

@app.route('/', methods=['GET'])
def check():
    return jsonify({"message": "Meeting Summarization using Watson API"})


@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.json
    question = data.get("question", "")

    formatted_question = f"""<|user|>\n{question}\n<|assistant|>\n"""
    prompt = f"""{prompt_input}{formatted_question}"""

    generated_response = model.generate_text(prompt=prompt, guardrails=False)

    return jsonify({"response": generated_response})

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
