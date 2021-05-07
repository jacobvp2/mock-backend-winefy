from flask import Flask, render_template, request, redirect, url_for,jsonify
from arbitraryFunction import definePersonality
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to our backend for the Twitter Algorithm! Nothing to see here. Try sending a POST \
    request to /predict to recieve a personality type based on Twitter data analysis!"

@app.route('/predict', methods=['GET', 'POST'])
def testfn():
    # Post request
    if request.method == 'POST':
        HTTP_data = request.get_json()
        username = HTTP_data["handle"]
        MBtype = definePersonality(username)
        return jsonify(MBtype), 200  # serialize and use JSON headers

if __name__ == "__main__":
    app.run()
