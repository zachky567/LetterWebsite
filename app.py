
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recipient = ""
    subject = ""
    message = ""

    if request.method == "POST":
        recipient = request.form["recipient"]
        subject = request.form["subject"]
        message = request.form["message"]

    return render_template(
        "index.html",
        recipient=recipient,
        subject=subject,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)

