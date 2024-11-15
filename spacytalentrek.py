import spacy
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined list of keywords for job screening
JOB_KEYWORDS = ["Python", "Flask", "SQL", "machine learning", "NLP", "deep learning", "API", "data analysis"]

def extract_keywords(text):
    """
    Extract matching job-related keywords from a given text.
    """
    doc = nlp(text)
    matched_keywords = set()

    for token in doc:
        # Match tokens with keywords (case insensitive)
        if token.text.lower() in map(str.lower, JOB_KEYWORDS):
            matched_keywords.add(token.text)

    return list(matched_keywords)

@app.route('/screen_portfolio', methods=['POST'])
def screen_portfolio():
    """
    Screen candidate portfolio for relevant keywords.
    """
    data = request.json
    portfolio_text = data.get("portfolio", "")

    if not portfolio_text:
        return jsonify({"error": "Portfolio text is required"}), 400

    # Extract keywords
    keywords_found = extract_keywords(portfolio_text)

    return jsonify({
        "keywords_matched": keywords_found,
        "total_keywords": len(keywords_found),
        "message": "Portfolio screened successfully!"
    })

if __name__ == '__main__':
    app.run(debug=True)