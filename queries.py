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
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
    curs.execute(sql, [email, field, title, institution, startDate, location, 
                        experienceType, experienceLevel, description, appLink, 
                        sponsorship])
    conn.commit()


'''inserts and updates '''
def insert_and_update_rating(conn,email,pid,userRating):
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO rating(email,pid,rating) VALUES (%s,%s,%s)
                            ON DUPLICATE KEY UPDATE rating = %s''', 
                            [email, pid, userRating, userRating])
    conn.commit()


'''compute average rating for opportunities'''
def average_rating(conn,pid):
    curs = dbi.dict_cursor(conn)
    curs.execute('''SELECT avg(rating)
                FROM rating
                WHERE pid = %s''', [pid])
    dic = curs.fetchone()
    if dic['avg(rating)'] == None:
        return "None"
    avgRating = float(dic['avg(rating)'])
    return avgRating

# update overall rating of an opportunity 
def update_pid_average(conn,avgRating,pid):
    curs = dbi.dict_cursor(conn)
    curs.execute('''update opportunity set averageRating = %s
                            where pid = %s''', 
                            [avgRating, pid])
    conn.commit()

def get_opportunities(conn):
    '''
    Gets and returns all opportunities in the database.
    '''
    curs = dbi.dict_cursor(conn)
    sql = ' SELECT * FROM opportunity'
    curs.execute(sql)
    return curs.fetchall()

def look_oppor_title(conn, title):
    curs = dbi.dict_cursor(conn)
    sql = "select * from opportunity where title like %s"
    curs = dbi.dict_cursor(conn)
    title = '%' + title + '%'
    curs.execute(sql, [title]) 
    return curs.fetchall()

def look_oppor_field(conn, field):
    curs = dbi.dict_cursor(conn)
    sql = "select * from opportunity where field like %s"
    curs = dbi.dict_cursor(conn)
    field = '%' + field + '%'
    curs.execute(sql, [field]) 
    return curs.fetchall()

def look_oppor_institution(conn, institution):
    curs = dbi.dict_cursor(conn)
    sql = "select * from opportunity where institution like %s"
    curs = dbi.dict_cursor(conn)
    institution = '%' + institution + '%'
    curs.execute(sql, [institution]) 
    return curs.fetchall()
    

if __name__ == '__main__':
    dbi.cache_cnf()
    dbi.use('centralex_db')
    conn = dbi.connect()
