"""Models and database functions for cars database."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# -------------------------------------------------------------------
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    brand_name = db.Column(db.String(50), db.ForeignKey('brands.name'), nullable=True)
    year = db.Column(db.Integer, nullable=True)

    brand = db.relationship("Brand", backref="models")


class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    founded = db.Column(db.Integer, nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)

    # models_that_belong_to_this_brand = db.relationship("Model", backref="brand")

    def display_brand(self):
        return "This is a cool brand called %s" % self.name

    def get_num_models(self):
        return len(self.models)



# End part 1
# -------------------------------------------------------------------
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
