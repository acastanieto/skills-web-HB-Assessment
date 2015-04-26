from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    return render_template("application-form.html")


@app.route('/application', methods=["POST"])
def application_confirmation():
    first = request.form.get("first")
    last = request.form.get("last")
    salary = request.form.get("salary")
    job = request.form.get("job")

    return render_template("application.html", first_name=first, last_name=last, salary=salary, job=job)





if __name__ == "__main__":
    app.run(debug=True)
