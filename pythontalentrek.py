from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load configuration
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Import models
from models.models import Candidate, Job

# Routes
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Automated Application Screening System!'})

# Add a new candidate
@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    data = request.json
    try:
        candidate = Candidate(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            skills=data['skills'],
            resume_url=data['resume_url']
        )
        db.session.add(candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Update candidate resume
@app.route('/update_resume/<int:candidate_id>', methods=['PUT'])
def update_resume(candidate_id):
    data = request.json
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({'error': 'Candidate not found!'}), 404
    try:
        candidate.resume_url = data['resume_url']
        db.session.commit()
        return jsonify({'message': 'Resume updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Connect to third-party HR tool API
@app.route('/send_to_hr_tool/<int:candidate_id>', methods=['POST'])
def send_to_hr_tool(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({'error': 'Candidate not found!'}), 404

    # Replace with actual HR tool API endpoint and credentials
    hr_tool_api_url = "https://thirdpartyhrtool.com/api/applications"
    api_key = "your_api_key"

    payload = {
        'name': candidate.name,
        'email': candidate.email,
        'phone': candidate.phone,
        'skills': candidate.skills,
        'resume_url'
