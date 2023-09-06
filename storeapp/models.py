from datetime import datetime
from .extensions import db
from .extensions import login_manager

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.Text, nullable=False, default="default.jpg")
    phone_number = db.Column(db.String(14), unique=True, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    products = db.relationship('Product', backref = "Distributor", lazy=True)
    cart = db.relationship('Cart', backref = "Buyer", lazy=True)

    def get_reset_token(self):
        s = Serializer(current_app.config["SECRET_KEY"], salt="Reset_password")
        return s.dumps({"user_id": self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"], salt="Reset_password")
        try: 
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    product_code = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    carts = db.relationship('Cart', backref = "Products", lazy=True)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.date_posted}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    is_purchased = db.Column(db.Boolean, nullable=False, default=False)
    quantity = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    product_code = db.Column(db.Integer, db.ForeignKey("product.product_code"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.date_added}')"
    