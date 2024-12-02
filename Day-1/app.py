from flask import Flask

app=Flask(__name__) 

@app.route("/")  # main or we can say user goes to firstly this page 
def main():
    return "<h1>Welcome to 1-st class--</h1>"


@app.route("/home")  #home page
def home():
    return "<h2> welcome to home page</h2>"

@app.route("/contact/<name>")   # Parameter in route 
def contact(name):  # taking paramerts
    return f"<h3> hello {name.title()} , you can now contact to owner of the website </h3>"

@app.route("/sum/<int:num1>/<int:num2>") # taking int parameters
def sum(num1,num2):
    return f"<h1>Sum of {num1} and {num2} is {num1+num2}</h1>"


if __name__=="__main__":  # this page run when use run this page if the user import this page somewhere or any other file then
    # it will not run bcz in that file this file __name__ is app so it will not run there 
    app.run(debug=True)
