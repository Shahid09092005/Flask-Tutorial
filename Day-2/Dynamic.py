from flask import Flask

Dynamic=Flask(__name__) 

@app.route("/")  # main or we can say user goes to firstly this page 
def main():
    return "<h1>Welcome to 1-st class--</h1>"


# using dynamic url that change url for every person name
@Dynamic.route("/greet/<name>")  #greet page
def greet(name):
    return f"<h2> hey! {name.title()}, Welcome to come here </h2>"


if __name__=="__main__":   
    Dynamic.run(debug=True)
