from flask import(Flask ,
                render_template ,
                url_for ,
                redirect ,
                flash # this will show dummy msg
                )
app=Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key" #CSRF-Clint Side Reques Foregin for the form 

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


from forms import LoginForm , signupForm

# signup
@app.route("/signup",methods=["GET","POST"])  # Flask will know in signup page that your are performing GET and POST Method
def signup():
    signupObj=signupForm()
    if signupObj.validate_on_submit(): #if true
        flash(f"Successfully Registered {signupObj.username.data}!")  # this will show when flash msg when user submit form with validation
        return redirect(url_for("/home"))
    else:
        print(signupObj.errors)  # Print errors if validation fails
    return render_template("signup.html",title="Sign-up",form=signupObj) 
    

  
#sign in 
@app.route("/login",methods=["GET",'POST'])
def login():
    loginObj = LoginForm()  # making instance of login or singinObj
    return render_template("login.html",title="login",form=loginObj)



if __name__=="__main__":
    app.run(debug=True)