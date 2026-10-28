from flask import Flask , render_template, url_for, request, jsonify, flash, redirect

app = Flask(__name__ , static_folder = "static", static_url_path = "/static")
#default value of static_folder = "static"
# default val for static_url_path = "/static"


app.secret_key = "some secret message"

#URL => endpoint

@app.route("/json")
def js():
    data = {
        "message" : "Welcome to learn json"
    }

    return jsonify(data), 200 # status-code

@app.route("/")
def hello_world():

    name = request.args.get("name", default="anonymous")
    subject = request.args.get("subject")

    #static file ==> dynamicallh  generate the url

    print(url_for("static", filename="style.css"))
    return render_template("index.html", name = name, sub = subject)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        header = "<header>ABC heading</header>"

        # send it to database and verify
        return render_template("welcome.html" ,  name= name, password=password, header=header)

    else:
        return render_template("login.html")


# Inheritance template

@app.route("/contact")
def contact():
    flash("support is availabe between 9-5")
    return render_template("contact.html")



# redirect function
@app.route("/redirect")
def redirect_to_login():
    return redirect(url_for("login"))

#This ensures that if app.py is imported as a module
# in other file then app.py is not run automatically



if __name__ =="__main__":
    app.run(debug=True)


#template - html files
#static files - does not change during run  time (images/css/js)