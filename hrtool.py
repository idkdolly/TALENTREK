import requests
from flask import jsonify

@app.route('/send_to_hr_tool/<int:candidate_id>', methods=['POST'])
def send_to_hr_tool(candidate_id):
    # Fetch candidate details from the database
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({'error': 'Candidate not found!'}), 404

    # HR tool API endpoint and credentials
    hr_tool_api_url = "https://thirdpartyhrtool.com/api/applications"
    api_key = "your_api_key"  # Replace with your API key

    # Construct the payload
    payload = {
        'name': candidate.name,
        'email': candidate.email,
        'phone': candidate.phone,
        'skills': candidate.skills,
        'resume_url': candidate.resume_url
    }

    # Headers for the request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Make the API request
    try:
        response = requests.post(hr_tool_api_url, json=payload, headers=headers)
        if response.status_code == 201:  # Assuming 201 is success
            return jsonify({'message': 'Candidate sent to HR tool!', 'response': response.json()})
        else:
            return jsonify({'error': f'Failed to send candidate: {response.text}'}), response.status_code
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
