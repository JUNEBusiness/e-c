import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
import random

from .extensions import mail
from .models import User, Product, Cart

# saves pictures and resize uploaded pictures to the filesystem
def save_picture(form_picture):
    # creates a random 8 bit hex
    random_hex = secrets.token_hex(8)
    # split the extension from the file name
    _, f_ext = os.path.splitext(form_picture.filename)
    # create a new filename with the extension and the hex
    picture_fn = random_hex + f_ext
    # create a piture path up until the package
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # set the piture dimension
    output_size = (125, 125)
    # open the image
    i = Image.open(form_picture)
    # set its size based on the dimension given
    i.thumbnail = (output_size)
    # save it to the root path created
    i.save(picture_path)
    return picture_fn


# removes profile pictures that are not needed
def delete_picture(previous_picture):
    # trace the piture path up until the package
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', previous_picture)
    # delete/remove picture from filesystem
    os.remove(picture_path)

    return 0


# handles sending mail to authenticate user
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@tchelberwrites.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('views.reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


def add_data():
    product1 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product1.insert()
    product2 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product2.insert()
    product3 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product3.insert()
    product4 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product4.insert()
    product5 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product5.insert()
    product6 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product6.insert()
    product7 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product7.insert()
    product8 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product8.insert()
    product9 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product9.insert()
    product10 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product10.insert()
    product11 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product11.insert()
    product12 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product12.insert()
    product13 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product13.insert()
    product14 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product14.insert()
    product15 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product15.insert()
    product16 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product16.insert()
    product17 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product17.insert()
    product18 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product18.insert()
    product19 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product19.insert()
    product20 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product20.insert()
    product21 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product21.insert()
    product22 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product22.insert()
    product23 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product23.insert()
    product24 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product24.insert()
    product25 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product25.insert()
    product26 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product26.insert()
    product27 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product27.insert()
    product28 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product28.insert()
    product29 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product29.insert()
    product30 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product30.insert()
    product31 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product31.insert()
    product32 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product32.insert()
    product33 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product33.insert()
    product34 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product34.insert()
    product35 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product35.insert()
    product36 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product36.insert()
    product37 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product37.insert()
    product38 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product38.insert()
    product39 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product39.insert()
    product40 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product40.insert()
    product41 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product41.insert()
    product42 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product42.insert()
    product43 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product43.insert()
    product44 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product44.insert()
    product45 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product45.insert()
    product46 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product46.insert()
    product47 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product47.insert()
    product48 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product48.insert()
    product49 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product49.insert()
    product50 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product50.insert()
    product51 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name=name, category=category, url=url, description="Lorem ipsum dolor sit amet, adipiscing elit.")
    product51.insert()
    return True