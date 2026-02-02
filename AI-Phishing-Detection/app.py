from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

HTML = '''
<!DOCTYPE html>
<html>
<head>
<title>Phishing Detection</title>
</head>
<body>
<h2>AI-Based Phishing Detection System</h2>
<form method="POST">
<input type="text" name="url" placeholder="Enter URL or message" required>
<button type="submit">Check</button>
</form>
{% if result %}
<h3>{{ result }}</h3>
{% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        pred = model.predict([url])[0]
        result = "Phishing Detected" if pred == 1 else "Safe URL"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
