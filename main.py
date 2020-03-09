from flask import Flask, render_template, request
from utilites.TxtFileHelper import AddLineBreaks
from utilites.GithubScraper import get_github_projects
from utilites.AccountCracker import run
import threading
import time
from flask.json import jsonify

app = Flask(__name__)


@app.route("/home")
def home():
    project_list = get_github_projects()
    return render_template("home.html", value=project_list)


@app.route("/github")
def github():
    project_list = get_github_projects()
    return render_template("github.html", value=project_list)


@app.route("/account")
def cracker():
    return render_template("account.html")


@app.route("/reddit")
def reddit():
    return render_template("reddit.html", )


@app.route('/reddit', methods=['POST'])
def reddit_post():
    return render_template("reddit.html", value=messages)


@app.route("/khan-academy")
def khan():
    return render_template("khan.html")


@app.route("/coupon")
def coupons():
    return render_template("coupons.html")


@app.route("/generated-accounts")
def generated():
    return render_template("/txt/generated.txt")


@app.route("/default-accounts")
def default():
    AddLineBreaks()
    return render_template("/txt/default.txt")


@app.route('/account', methods=['POST'])
def form_post():
    emails1 = request.form['email1']
    emails2 = request.form['email2']
    emails3 = request.form['email3']
    usernames = [emails1, emails2, emails3]
    accounts = [{'index': '0', 'username': '', 'password': ''},]
    accounts = run(usernames, False, False)
    return render_template("cracker.html", value=accounts)


if __name__ == "__main__":
    app.run(debug=True)

