from flask import Flask

app=Flask(__name__)

@app.route("/")
def main():
    """
    主界面
    """
    return "hello world"