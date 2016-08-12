from flask import Flask, render_template, request
from model import connect_to_db, Brand, Model

app = Flask(__name__)

app.jinja_env.auto_reload = True

@app.route("/")
def show_homepage():
    all_brands = Brand.query.all()
    print "\n\n\n %s \n\n\n" % all_brands
    return render_template("index.html", brands=all_brands)

@app.route('/search')
def search_brands():
    search_term = request.args.get("search_term")
    results = Brand.query.filter_by(name=search_term).all()
    return render_template("search_results.html", results=results)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")