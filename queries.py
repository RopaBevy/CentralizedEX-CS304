import cs304dbi as dbi

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
def insert_opportunity(user_email, user_password, user_name, user_type):
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
        sponsorship = request.form.get('sponsorship')


# to be used for testing code in this module
if __name__ == '__main__':
    pass
