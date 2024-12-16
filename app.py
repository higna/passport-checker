from flask import Flask, render_template, request
import datetime as dt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        validity = request.form["validity"]

        # Convert inputs to datetime objects
        today = dt.datetime.now()
        validity_date = dt.datetime.strptime(validity, '%Y-%m')

        # Calculate the difference in months
        time_difference = (validity_date.year - today.year) * 12 + (validity_date.month - today.month)

        # Determine the validity message
        if time_difference > 3:
            message = f"{name}, your passport is valid for more than 3 months."
        elif time_difference == 3:
            message = f"{name}, your passport has exactly 3 months left to expire."
        elif 1 < time_difference < 3:
            message = f"{name}, your passport has {time_difference} months of validity left. Go renew."
        elif time_difference == 1:
            message = f"{name}, your passport has 1 month validity left. Go renew."
        else:
            message = f"{name}, your passport is expired or expiring this month. Please renew immediately."

        return render_template("index.html", message=message)

    return render_template("index.html")
