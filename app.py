from flask import Flask


@app.route("/")
def hello():
    return "Hello. This is version 1.0.0"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
