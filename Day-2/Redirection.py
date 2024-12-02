from flask import Flask 
from flask import redirect , url_for

Redirection=Flask(__name__) 

@Redirection.route("/")  # main or we can say user goes to firstly this page 
def main():
    return "<h1>Welcome to 1-st class--</h1>"


# using dynamic url that change url for every person name
@Redirection.route("/greet/<name>")  #greet page
def greet(name):
    return f"<h2> hey! {name.title()}, Welcome to come here </h2>"

@Redirection.route("/test/<name>/<int:marks>")
def test(name,marks):
    if marks>30:
        return redirect(url_for('Studentpass',name=name,marks=marks))
    else:
        return redirect(url_for('Studentfail',name=name,marks=marks))
        
@Redirection.route("/Studentpass/<name>/<int:marks>")  # passed student
def Studentpass(name,marks):
    return f"<h2>Congratulation {name.title()} , you passed the exam and your scored {marks} in your test </h2>"

@Redirection.route("/Studentfail/<name>/<int:marks>") #failed Student
def Studentfail(name,marks):
    return f"<h2>Sorry {name.title()} , you failed the exam bcz your scored {marks} in your test </h2>"

if __name__=="__main__":   
    Redirection.run(debug=True)


# Note: Common Response Codes
# 301: Moved permanently
# 302,303,307,308:Redirected temporarily
