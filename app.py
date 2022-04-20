from flask import (Flask, render_template, make_response,
                   request, session, redirect, url_for, flash)
import cs304dbi as dbi
import bcrypt
import queries
import random, re

app = Flask(__name__)

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# home page
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if(request.method == 'GET'):
        return render_template("signup.html")
    else:
        conn = dbi.connect()
        # code to validate and add user to database goes here
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user_type = request.form.get('type')

        #add an if statement that verifies that email as a wellesley email
        email_pattern = re.compile('@wellesley.edu$')
        if(len(email_pattern.findall(email)) == 0):
            flash('Please use your Wellesley College email.')
            return redirect(url_for('signup'))
        
        if(password != password2):
            flash('passwords do not match')
            return redirect(url_for('signup'))

        # if user is already in database, redirect back to login page
        if (queries.user_exists(conn, email)):
            flash('An account with this email already exists. Please login.')
            return redirect(url_for('login'))
        else:
            # create a new user with the form data.
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                            bcrypt.gensalt())
            stored_password = hashed_password.decode('utf-8')
            # add the new user to the database
            queries.insert_member(conn, email, stored_password, name, user_type)
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    print(request.method)
    if(request.method == 'GET'):
        return render_template("login.html")
    if(request.method == 'POST'):
        print('post method')
        conn = dbi.connect()
        email = request.form.get('email')
        password = request.form.get('password')

        print("we are at the login and printing email",email)
        
        member = queries.login(conn, email)
        print("we are at the login and printing password",member)
        if(member is None):
            print("this should not be true")
            flash('Login credentials are incorrect. Please try again or sign up.')
            return redirect(url_for('login'))


        print("member is not none")
        stored_password = member['password']
        print('database has stored: {} {}'.format(stored_password,type(stored_password)))
        print('form supplied passwd: {} {}'.format(password,type(password)))
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                stored_password.encode('utf-8'))

        hashed_str = hashed_password.decode('utf-8')
                            
        if(hashed_str == stored_password):
            print("yayyyyyyyyyyyyyy")
            flash('Successfully logged in.')
            #redirect them to the page for logged in people
            session['email'] = email
            session['logged_in'] = True
            session['visits'] = 1
            return render_template('welcomePage.html')
        else:
            flash('Login unsuccessful. Please try again or sign up.')
            return redirect(url_for('login'))


@app.route('/logout/', methods=['GET'])
def logout():
    if 'email' in session:
        email = session['email']
        session.pop('email')
        session.pop('logged_in')
        flash('You are logged out')
        return redirect(url_for('/'))
    else:
        flash('you are not logged in. Please login or join')
        return redirect( url_for('/') )

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if(request.method == 'GET'):
        return render_template("upload.html")
    else:
        conn = dbi.connect()
        
        # check if user is logged in, if not redirect them to login first
        # otherwise, find user's email

        # code to gather experience info to add to the database
        title = request.form.get('title')
        institution = request.form.get('institution')
        start = request.form.get('start')
        location = request.form.get('location')
        experienceType = request.form.get('experienceType')
        field = request.form.get('field')
        description = request.form.get('description')
        link = request.form.get('link')
        sponsorship = request.form.get('sponsorship')


if __name__ == '__main__':
    dbi.cache_cnf()
    dbi.use('yafifi_db') #centralex_db

    import os
    port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)