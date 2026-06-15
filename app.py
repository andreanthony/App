import os
import json
from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic

app = Flask(__name__)
client = Anthropic()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_quiz():
    data = request.get_json()
    topic = data.get("topic", "").strip()
    num_questions = int(data.get("num_questions", 5))
    difficulty = data.get("difficulty", "medium")

    if not topic:
        return jsonify({"error": "Please provide a topic."}), 400

    prompt = f"""Generate a quiz about "{topic}" with {num_questions} multiple-choice questions at {difficulty} difficulty.

Return ONLY a valid JSON object with this exact structure:
{{
  "title": "Quiz title here",
  "questions": [
    {{
      "question": "Question text here?",
      "options": ["A) Option one", "B) Option two", "C) Option three", "D) Option four"],
      "answer": "A) Option one",
      "explanation": "Brief explanation of why this is correct."
    }}
  ]
}}

Rules:
- Each question must have exactly 4 options labeled A), B), C), D)
- The answer must match one of the options exactly
- Make questions clear and unambiguous
- Do not include any text outside the JSON object"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    quiz = json.loads(raw)
    return jsonify(quiz)


if __name__ == "__main__":
    app.run(debug=True)
