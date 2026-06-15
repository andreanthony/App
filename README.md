
Readme · MD
# 🧠 AI Quiz Generator
 
Generate multiple-choice quizzes on any topic instantly using the Claude API. Built with Python + Flask.
 
![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey) ![Claude](https://img.shields.io/badge/Powered%20by-Claude-purple)
 
## Features
 
- Enter any topic and get a custom quiz in seconds
- Choose number of questions (3, 5, 8, or 10)
- Three difficulty levels: Easy, Medium, Hard
- Interactive UI with instant answer feedback and explanations
- Score tracking
## Demo
 
![screenshot placeholder](https://via.placeholder.com/700x400?text=Add+a+screenshot+here)
 
## Getting Started
 
### 1. Clone the repo
 
```bash
git clone https://github.com/YOUR_USERNAME/ai-quiz-generator.git
cd ai-quiz-generator
```
 
### 2. Create a virtual environment
 
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Set your API key
 
Copy the example env file and add your [Anthropic API key](https://console.anthropic.com/):
 
```bash
cp .env.example .env
```
 
Then edit `.env`:
 
```
ANTHROPIC_API_KEY=your_api_key_here
```
 
### 5. Run the app
 
```bash
python app.py
```
 
Open [http://localhost:5000](http://localhost:5000) in your browser.
 
## Project Structure
 
```
ai-quiz-generator/
├── app.py              # Flask backend + Claude API call
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
 
## How It Works
 
1. User enters a topic, question count, and difficulty
2. Flask sends a structured prompt to the Claude API
3. Claude returns a JSON quiz object
4. The frontend renders questions and handles scoring client-side
## License
 
MIT
