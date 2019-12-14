import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext 
	picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
	output_size = (125,125)
	newImage = Image.open(form_picture)
	newImage.thumbnail(output_size)
	newImage.save(picture_path)
	return picture_fn


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request',sender='noreply@gmail.com',recipients=[user.email])
	msg.body = f'''To reset your password click on below link:
{url_for('users.reset_token',token=token,_external=True)}
If you didnt requested for, please ignore the mail.
'''
	mail.send(msg)
