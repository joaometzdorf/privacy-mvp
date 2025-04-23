from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    site_name = request.form.get("site_name")
    contact_email = request.form.get("contact_email")
    data_collected = request.form.getlist("data_collected")
    purposes = request.form.getlist("purpose")
    third_parties = request.form.getlist("third_parties")
    other_services = request.form.get("other_third_parties")
    if other_services:
        third_parties.append(other_services)
    has_eu_users = request.form.get("has_eu_users")
    retention_period = request.form.get("retention_period")
    data_sharing = request.form.get("data_sharing")
    audience = request.form.get("audience")

    return render_template(
        "result.html",
        site_name=site_name,
        contact_email=contact_email,
        data_collected=data_collected,
        purposes=purposes,
        third_parties=third_parties,
        has_eu_users=has_eu_users,
        retention_period=retention_period,
        data_sharing=data_sharing,
        audience=audience,
        effective_date=datetime.today().strftime("%B %d, %Y"),
    )


if __name__ == "__main__":
    app.run(debug=True)
