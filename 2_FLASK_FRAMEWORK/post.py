from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")

def home():
    return "<html><H1>Welcome to the flask course  </H1>  </html>"


@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/main")
def main():
    return "welcome to main page "

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    if request.method=='POST':
        email=request.form['email']
        return f' provided email {email}!'
    
    if request.method=='POST':
        age=request.form['age']
        return f'the provided age is  {age}!'
    return render_template('form.html')




if __name__=="__main__":
    app.run(debug=True)