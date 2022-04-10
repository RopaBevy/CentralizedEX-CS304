from flask import (Flask, render_template, make_response,
                   request, redirect, url_for, flash)
import cs304dbi as dbi
import bcrypt
import queries
import cs304dbi as dbi

app = Flask(__name__)

# home page
@app.route('/')
def get_login():
    return render_template("login.html")


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

        #add an if statement that varifies that email as a wellesley email
        if (password != password2):
            flash('passwords do not match')
            return redirect( url_for('signup'))

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
    if(request.method == 'GET'):
        return render_template("login.html")
    else:
        conn = dbi.connect()
        email = request.form.get('email')
        password = request.form.get('password')

        login_result = queries.login(conn, email)
        if(login_result is None):
            flash('Login is incorrect. Please try again or sign up.')
            return redirect( url_for('login'))

        stored_password = login_result['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                stored_password.encode('utf-8'))
                            
        if(hashed_password == stored_password):
            flash('Successfully logged in.')
            #redirect them to the page for logged in people
            return redirect('user', username=username) 
        else:
            flash('Login unsuccessful. Please try again or sign up.')
            return redirect(url_for('get_login'))



if __name__ == '__main__':
    dbi.cache_cnf()
    dbi.use('rs2_db') #centralex_db

    import os
    port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)