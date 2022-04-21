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
def insert_opportunity(conn, email, field, title, institution, startDate, location, 
                    experienceType, experienceLevel, description, appLink, 
                    sponsorship):
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  opportunity (pid, email, field, title, institution, 
            startDate, `location`, experienceType, experienceLevel, 
            `description`, appLink, sponsorship)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
    #generate a pid and pass it ==> autoincrement maybe with concurrency handling
    curs.execute(sql, [pid, email, field, title, institution, startDate, location, 
                        experienceType, experienceLevel, description, appLink, 
                        sponsorship])
    conn.commit()

def get_opportunities(conn):
    curs = dbi.dict_cursor(conn)
    sql = ' SELECT * FROM opportunity'
    curs.execute(sql)
    return curs.fetchall()


# to be used for testing code in this module
if __name__ == '__main__':
    dbi.cache_cnf()
    dbi.use('rs2_db') #centralex_db

    conn = dbi.connect()
    print(get_opportunities(conn))
