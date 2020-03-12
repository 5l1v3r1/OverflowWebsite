from flask import Flask, render_template, request, abort, redirect
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


@app.route("/")
def default():
    return redirect("/home")


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
    accounts = [{'index': '1', 'username': '', 'password': ''},{'index': '2', 'username': '', 'password': ''},{'index': '3', 'username': '', 'password': ''},{'index': '4', 'username': '', 'password': ''},{'index': '5', 'username': '', 'password': ''},]
    return render_template("account.html", value=accounts)


@app.route("/reddit")
def reddit():
    data = [{'id': '1', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '2', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '3', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '4', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '5', 'sub': 'reddit.com', 'num_msg': '0'},]
    return render_template("reddit.html", value=data)


@app.route('/reddit', methods=['POST'])
def reddit_post():
    use_default = False
    use_proxy = False
    sub_link = request.form['link']
    msg1 = request.form['msg1']
    msg2 = request.form['msg2']
    num_msg = request.form['num_msg']
    
    checkboxes = list(request.form.getlist('checkbox'))
    for i in checkboxes:
        if i == '1':
            use_default = True
        elif i == '2':
            use_proxy = True

    data = [{'id': '1', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '2', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '3', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '4', 'sub': 'reddit.com', 'num_msg': '0'},{'id': '5', 'sub': 'reddit.com', 'num_msg': '0'},]
    return render_template("reddit.html", value=data)


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
def default_accounts():
    # AddLineBreaks()
    return render_template("/txt/default.txt")


@app.route('/account', methods=['POST'])
def form_post():
    emails1 = request.form['email1']
    emails2 = request.form['email2']
    emails3 = request.form['email3']
    emails4 = request.form['email4']
    emails5 = request.form['email5']
    usernames = [emails1, emails2, emails3, emails4, emails5]
    accounts = [{'index': '0', 'username': '', 'password': ''},]
    accounts = run(usernames, False, False)
    return render_template("account.html", value=accounts)


if __name__ == "__main__":
    app.run(debug=True)

