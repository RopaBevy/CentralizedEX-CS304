import cs304dbi as dbi

def insert_member(conn, user_email, user_password, user_name, user_type):
    '''
    Inserts a new member into the database. 
    '''
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  member (email, password, name, type)
            values (%s, %s, %s, %s)
        '''
    curs.execute(sql, [user_email, user_password, user_name, user_type])
    conn.commit()

def user_exists(conn, email):
    '''
    Verifies if a user already exists in the database.
    '''
    curs = dbi.dict_cursor(conn)
    sql = '''SELECT email
                    FROM member
                    WHERE email = %s'''
    curs.execute(sql, [email])
    if(curs.fetchone() is None):
        return False
    return True

def login(conn, email):
    '''
    Collects the password from the database allowing the user to login.
    '''
    curs = dbi.dict_cursor(conn)
    sql = '''SELECT email, password, name, type
                    FROM member
                    WHERE email = %s'''
    curs.execute(sql, [email])
    return curs.fetchone()

def insert_opportunity(conn, email, field, title, institution, startDate, location, 
                    experienceType, experienceLevel, description, appLink, 
                    sponsorship):
    '''
    Adds opportunity posting into database.
    '''
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  opportunity (email, field, title, institution, 
            startDate, `location`, experienceType, experienceLevel, 
            `description`, appLink, sponsorship)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
    curs.execute(sql, [email, field, title, institution, startDate, location, 
                        experienceType, experienceLevel, description, appLink, 
                        sponsorship])
    conn.commit()

def get_opportunities(conn):
    '''
    Gets and returns all opportunities in the database.
    '''
    curs = dbi.dict_cursor(conn)
    sql = ' SELECT * FROM opportunity'
    curs.execute(sql)
    return curs.fetchall()

if __name__ == '__main__':
    dbi.cache_cnf()
    dbi.use('rs2_db') #centralex_db
    conn = dbi.connect()
