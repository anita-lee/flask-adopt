"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE_URL = "https://images.unsplash.com/photo-1541364983171-a8ba01e95cfc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default='')
    age = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False, default='')
    available = db.Column(db.Boolean, nullable=False, default=True)


    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"