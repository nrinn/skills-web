from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index_page():
    # Return this as a strange
    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route('/application-template')
def application_submission():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salaryrequirement = request.args.get("salaryrequirement")
    jobtype = request.args.get("jobtype")

    return render_template("application-template.html", firstname=firstname, lastname=lastname,
                            salaryrequirement=salaryrequirement, jobtype=jobtype)

if __name__ == "__main__":
    app.run(debug=True)




# Make sure you write up the styles.css file to still be handled properly – 
# this will mean creating a static/ directory, moving it into there, 
# and updating the link tag in the HTML that points to it.