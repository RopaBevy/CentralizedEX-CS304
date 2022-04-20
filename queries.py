import cs304dbi as dbi
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify, Response)

# add to member table, use in signup
def insert_member(conn, user_email, user_password, user_name, user_type):
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  member (email, password, name, type)
            values (%s, %s, %s, %s)
        '''
    curs.execute(sql, [user_email, user_password, user_name, user_type])
    conn.commit()

def user_exists(conn, email):
    curs = dbi.dict_cursor(conn)
    sql = '''SELECT email
                    FROM member
                    WHERE email = %s'''
    curs.execute(sql, [email])
    if(curs.fetchone() is None):
        return False
    return True

def login(conn, email):
    curs = dbi.dict_cursor(conn)
    sql = '''SELECT email, password, name, type
                    FROM member
                    WHERE email = %s'''
    curs.execute(sql, [email])
    return curs.fetchone()

# check the member table for someone


# Adds opportunity posting into database
# Returns comfirmation
""" def insert_opportunity(user_email, user_password, user_name, user_type):
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  opportunity (email, password, name, type)
          #  values (%s, %s, %s, %s)
       # '''
   # curs.execute(sql, [user_email, user_password, user_name, user_type])
   # conn.commit()
        email = request.form.get('email')
        field = request.form.get('field')
        title = request.form.get('title')
        institution = request.form.get('institution')
        startDate = request.form.get('startDate')
        location = request.form.get('location')
        experienceType = request.form.get('experienceType')
        experienceLevel = request.form.get('experienceLevel')
        description = request.form.get('description')
        appLink = request.form.get('appLink')
        sponsorship = request.form.get('sponsorship') """


def upload():
    '''Displays upload page, and allows user to submit an internship link to database.'''  
    conn = dbi.connect()
    try: 
        uid = session['uid']
        # These forms go to the upload route
        if (session.get('uid')): #if it exists
            if request.method == 'GET':
                return render_template('upload.html')

            else:
                institution = request.form.get('institution')
                title = request.form['title']
                startDate = request.form.get('startDate')
                location = request.form.get('location')
                expType = request.form.get('experienceType')
                expLevel = request.form.get('experienceLevel')
                description = request.form.get('description')
                appLink = request.form.get('appLink')
                sponsorship = request.form.get('sponsorship')
                seasonList = request.form.getlist('season')
                season= ','.join([str(elem) for elem in seasonList])
                year = request.form['year']
                experienceList = request.form.getlist('experience')
                experience = ','.join([str(elem) for elem in experienceList])
                print(experience)
                print(uid)
                # Insert to database
                #lock.acquire()
                if sqlHelper.companyExists(compName) == 0:
                    sqlHelper.insertCompany(compName)
                lock.release()
                sqlHelper.insertApplication(link,compName,city,uid,role,season,year,experience)
                flash('Opportunity at ' + compName + ' was uploaded successfully')
                return render_template('upload.html')
            
            #User must login before uploading 
    except KeyError:
        flash('You must be logged in to upload information.')
        return redirect(url_for('index'))



# to be used for testing code in this module
if __name__ == '__main__':
    pass
