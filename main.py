from flask import Flask, render_template, request, abort
from utilites.TxtFileHelper import AddLineBreaks
from utilites.GithubScraper import get_github_projects
from utilites.AccountCracker import run
from flask.json import jsonify
import hmac
import hashlib
import git


app = Flask(__name__)


def is_valid_signature(x_hub_signature, data, private_key):
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)


@app.route("/home")
def home():
    project_list = get_github_projects()
    return render_template("home.html", value=project_list)


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        x_hub_signature = request.headers.get('X-Hub-Signature')
        if not is_valid_signature(x_hub_signature, request.data, "Mantini88"):
            print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
            abort(418)
        g = git.Git('overflow/')
        g.pull('origin','master')
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


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

