from flask import Flask 
from flask import redirect , url_for , render_template
 
app=Flask(__name__) 

@app.route("/")  # main or we can say user goes to firstly this page
def index():
    return " welcome "

# use of inheritance
@app.route("/contact") #contact
def contact():
    return render_template("contact.html",title="contact")  #contact.html should be inside templates folder
 
#sum
@app.route("/sum/<int:n1>/<int:n2>") #sum
def sum(n1,n2):
    return render_template("sum.html",title="sum",n1=n1,n2=n2)  

@app.route("/home")  #Home
def home():
    return render_template("home.html",title="home")  #home.html should be inside templates folder
    # title is act as placeholder

@app.route("/about") #About
def about():
    return render_template("about.html",title="about")  #about.html should be inside templates folder
 
if __name__=="__main__":
    app.run(debug=True)
