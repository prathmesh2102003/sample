from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/videos/<filename>")
def serve_video(filename):
    return send_file(f"videos/{filename}", mimetype="video/mp4")

if __name__ == "__main__":
    app.run(debug=True)
