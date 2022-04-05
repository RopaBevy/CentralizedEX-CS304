from flask import (Flask, render_template, make_response,
                   request, redirect, url_for, flash)

app = Flask(__name__)

# home page
@app.route('/')
def get_login():
    return render_template("index.html")


# @auth.route('/signup', methods=['POST'])
# def signup_post():
#     # code to validate and add user to database goes here
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')

#     user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

#     if user: # if a user is found, we want to redirect back to signup page so user can try again
#         return redirect(url_for('auth.signup'))

#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for('auth.login'))


if __name__ == '__main__':
    import os
    port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)