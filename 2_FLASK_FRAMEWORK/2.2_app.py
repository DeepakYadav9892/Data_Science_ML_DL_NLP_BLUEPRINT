from flask import Flask
app=Flask(__name__)
@app.route("/")

def home():
    return "Hello ,Flask !"


@app.route("/index")
def index():
    return "Welcome to the Index page"

@app.route("/main")
def main():
    return "welcome to main page "




if __name__=="__main__":
    app.run(debug=True)