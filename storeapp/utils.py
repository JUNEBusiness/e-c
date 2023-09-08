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
    try:
        product1 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Creamy Woman", category="fashion", url="https://images.pexels.com/photos/2043590/pexels-photo-2043590.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product1.insert()
        product2 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Onions", category="fashion", url="https://images.pexels.com/videos/8020671/pexels-photo-8020671.jpeg?auto=compress&cs=tinysrgb&h=204&fit=crop&w=228&dpr=1", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product2.insert()
        product3 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Polar bear", category="fashion", url="https://images.pexels.com/photos/1381556/pexels-photo-1381556.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product3.insert()
        product4 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Flower handbag", category="fashion", url="https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product4.insert()
        product5 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Coat", category="fashion", url="https://images.pexels.com/photos/1721558/pexels-photo-1721558.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product5.insert()
        product6 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Big stripe Bag", category="fashion", url="https://images.pexels.com/photos/1374910/pexels-photo-1374910.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product6.insert()
        product7 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Woolly Jacket", category="fashion", url="https://images.pexels.com/photos/1040173/pexels-photo-1040173.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product7.insert()
        product8 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Blue jade Jacket", category="fashion", url="https://images.pexels.com/photos/1375736/pexels-photo-1375736.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product8.insert()
        product9 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Bluebird shirt", category="fashion", url="https://images.pexels.com/photos/2466756/pexels-photo-2466756.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product9.insert()
        product10 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Creamy attire", category="fashion", url="https://images.pexels.com/photos/3317434/pexels-photo-3317434.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product10.insert()
        product11 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Blue pants", category="fashion", url="https://images.pexels.com/photos/4937224/pexels-photo-4937224.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product11.insert()
        product12 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Wine suit", category="fashion", url="https://images.pexels.com/photos/1300550/pexels-photo-1300550.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product12.insert()
        product13 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Yellow bird", category="fashion", url="https://images.pexels.com/photos/1858488/pexels-photo-1858488.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product13.insert()
        product14 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="On the road", category="fashion", url="https://images.pexels.com/photos/3263460/pexels-photo-3263460.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product14.insert()
        product15 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Milky shoe", category="fashion", url="https://images.pexels.com/photos/298863/pexels-photo-298863.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product15.insert()
        product16 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Suits", category="fashion", url="https://images.pexels.com/photos/325876/pexels-photo-325876.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product16.insert()
        product17 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Jeans", category="fashion", url="https://images.pexels.com/photos/52518/jeans-pants-blue-shop-52518.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product17.insert()
        product18 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Denim", category="fashion", url="https://images.pexels.com/photos/1176618/pexels-photo-1176618.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product18.insert()
        product19 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Dark room", category="furniture", url="https://images.pexels.com/photos/777001/pexels-photo-777001.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product19.insert()
        product20 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Mac desktop", category="electronics", url="https://images.pexels.com/photos/38568/apple-imac-ipad-workplace-38568.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product20.insert()
        product21 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Keyboard", category="electronics", url="https://images.pexels.com/photos/1714205/pexels-photo-1714205.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product21.insert()
        product22 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Ipad 2", category="mobile phone", url="https://images.pexels.com/photos/2237797/pexels-photo-2237797.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product22.insert()
        product23 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Geeforce", category="electronics", url="https://images.pexels.com/photos/2399840/pexels-photo-2399840.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product23.insert()
        product24 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Ipad 1", category="mobile phones", url="https://images.pexels.com/photos/2351844/pexels-photo-2351844.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product24.insert()
        product25 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Ram", category="electronics", url="https://images.pexels.com/photos/2588757/pexels-photo-2588757.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product25.insert()
        product26 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Wireless keyboard", category="accessories", url="https://images.pexels.com/photos/1419924/pexels-photo-1419924.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product26.insert()
        product27 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Mac combo", category="electronics", url="https://images.pexels.com/photos/414548/pexels-photo-414548.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product27.insert()
        product28 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Night light", category="furniture", url="https://images.pexels.com/photos/3937174/pexels-photo-3937174.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product28.insert()
        product29 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Condo View", category="furniture", url="https://images.pexels.com/photos/2343473/pexels-photo-2343473.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product29.insert()
        product30 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Ram", category="accessories", url="https://images.pexels.com/photos/2582931/pexels-photo-2582931.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product30.insert()
        product31 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="MacBook pro", category="electronics", url="https://images.pexels.com/photos/303383/pexels-photo-303383.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product31.insert()
        product32 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Floppy disk", category="accessories", url="https://images.pexels.com/photos/117729/pexels-photo-117729.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product32.insert()
        product33 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Dell all-in-one", category="electronics", url="https://images.pexels.com/photos/400678/pexels-photo-400678.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product33.insert()
        product34 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Keyboard (Lights)", category="accessories", url="https://images.pexels.com/photos/3103199/pexels-photo-3103199.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product34.insert()
        product35 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Mouse", category="accessories", url="https://images.pexels.com/photos/2272759/pexels-photo-2272759.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product35.insert()
        product36 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Dell Pc", category="electronics", url="https://images.pexels.com/photos/2861984/pexels-photo-2861984.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product36.insert()
        product37 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Iphone 6", category="mobile phones", url="https://images.pexels.com/photos/237708/pexels-photo-237708.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product37.insert()
        product38 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Techno Povouir", category="mobile phones", url="https://images.pexels.com/photos/1092644/pexels-photo-1092644.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product38.insert()
        product39 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Samsung S8", category="mobile phones", url="https://images.pexels.com/photos/47261/pexels-photo-47261.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product39.insert()
        product40 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Samsung Note9", category="mobile phones", url="https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product40.insert()
        product41 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Iphone 11pro", category="mobile phones", url="https://images.pexels.com/photos/3981749/pexels-photo-3981749.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product41.insert()
        product42 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Iphone 12", category="mobile phones", url="https://images.pexels.com/photos/9555131/pexels-photo-9555131.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product42.insert()
        product43 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Rubix walls", category="furnitures", url="https://images.pexels.com/photos/6691671/pexels-photo-6691671.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product43.insert()
        product44 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Type-c chargers", category="accessories", url="https://images.pexels.com/photos/4387770/pexels-photo-4387770.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product44.insert()
        product45 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Samsung Note10", category="mobile phones", url="https://images.pexels.com/photos/13429657/pexels-photo-13429657.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product45.insert()
        product46 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Iphone cover", category="accessories", url="https://images.pexels.com/photos/12072362/pexels-photo-12072362.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product46.insert()
        product47 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Chandelier", category="furniture", url="https://images.pexels.com/photos/447592/pexels-photo-447592.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product47.insert()
        product48 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Living room", category="furniture", url="https://images.pexels.com/photos/2227832/pexels-photo-2227832.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product48.insert()
        product49 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Kitchen stand", category="furniture", url="https://images.pexels.com/photos/6021777/pexels-photo-6021777.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product49.insert()
        product50 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Reading corner", category="furniture", url="https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product50.insert()
        product51 = Product(price=random.randint(10, 100), product_code= random.randrange(10000, 90000, 1234), name="Dinning table", category="furniture", url="https://images.pexels.com/photos/2995012/pexels-photo-2995012.jpeg?auto=compress&cs=tinysrgb&w=600", description="Lorem ipsum dolor sit amet, adipiscing elit.")
        product51.insert()
        print("These product has been added!")
        return True
    except:
        print("Something went wrong")
    