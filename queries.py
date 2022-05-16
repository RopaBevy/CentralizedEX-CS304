import cs304dbi as dbi

def insert_member(conn, user_email, profession, institution, user_password, user_name, user_type, about):
    '''
    Inserts a new member into the database. 
    '''
    curs = dbi.dict_cursor(conn)
    sql = ''' INSERT INTO  member (email, profession, institution, password, name, type, about)
            values (%s, %s, %s, %s,%s,%s,%s)
        '''
    curs.execute(sql, [user_email, profession, institution, user_password, user_name, user_type, about])
    conn.commit()


def update_member(conn, user_email, profession, institution,stored_password, user_name, user_type, about):
    '''
    update a member in the database. 
    '''
    curs = dbi.dict_cursor(conn)

    sql = ''' UPDATE member SET profession = %s, institution = %s, password = %s, name = %s, type = %s, about= %s
            where email = %s
        '''
    curs.execute(sql, [profession, institution, stored_password,user_name, user_type, about, user_email])
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

def insert_and_update_rating(conn,email,pid,userRating):
    '''inserts and updates '''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO rating(email,pid,rating) VALUES (%s,%s,%s)
                            ON DUPLICATE KEY UPDATE rating = %s''', 
                            [email, pid, userRating, userRating])
    conn.commit()

def insert_comment(conn, email, pid, userComment):
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO comment(email,pid,comment) VALUES (%s,%s,%s)''', 
                            [email, pid, userComment])
    conn.commit()


def average_rating(conn,pid):
    '''compute average rating for opportunities'''
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
    sql = 'SELECT * FROM opportunity'
    curs.execute(sql)
    return curs.fetchall()

def get_fields(conn):
    '''
    Gets and returns all fields in the database.
    '''
    curs = dbi.dict_cursor(conn)
    sql = 'SELECT distinct field from opportunity'
    curs.execute(sql)
    return curs.fetchall()

def get_institutions_opportunity(conn):
    curs = dbi.dict_cursor(conn)
    sql = 'SELECT distinct institution from opportunity'
    curs.execute(sql)
    return curs.fetchall()

def get_professions(conn):
    curs = dbi.dict_cursor(conn)
    sql = 'SELECT distinct profession from member'
    curs.execute(sql)
    return curs.fetchall()

def get_institutions_member(conn):
    curs = dbi.dict_cursor(conn)
    sql = 'SELECT distinct institution from member'
    curs.execute(sql)
    return curs.fetchall()

def get_affiliations(conn):
    curs = dbi.dict_cursor(conn)
    sql = 'SELECT distinct `type` from member'
    curs.execute(sql)
    return curs.fetchall()

def get_filtered_oppor(conn, field, kind, exp,institution, sponsorship,keyword):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    sql = '''
        select * from opportunity where field like %s and field in (
            select field from opportunity where experienceType like  %s and experienceType in (
                select experienceType from opportunity where experienceLevel like %s and experienceLevel in (
                    select experienceLevel from opportunity where institution like %s and institution in (
                        select institution from opportunity where sponsorship like %s and sponsorship in (
                            select sponsorship from opportunity where title like %s
                        )
                    )
                )
            )
        )
        '''
    curs.execute(sql, ['%'+field+'%', '%'+kind+'%', '%'+exp+'%', '%'+institution+'%', '%'+sponsorship+'%','%'+keyword+'%'])
    return curs.fetchall()


def get_filtered_members(conn, affiliation, profession, institution, name):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    sql = '''
        select * from member where `type` like %s and `type` in (
            select `type` from member where profession like  %s and profession in (
                select profession from member where institution like %s and institution in (
                    select institution from member where `name` like %s
                    )
                )
            )
        '''
    curs.execute(sql, ['%'+affiliation+'%', '%'+profession+'%', '%'+institution+'%', '%'+name+'%'])
    return curs.fetchall()

def get_all_members(conn):
    curs = dbi.dict_cursor(conn)
    sql = "select * from member"
    curs.execute(sql) 
    return curs.fetchall()

def get_one_member(conn,email):
    curs = dbi.dict_cursor(conn)
    sql = "select * from member where email = %s"
    curs = dbi.dict_cursor(conn)
    curs.execute(sql, [email]) 
    return curs.fetchone()

def isFavorite(conn, email, pid):
    '''Checks whether an opportunity has been favorited'''
    curs = dbi.cursor(conn)
    sql = '''select * from favorites where email = %s and pid = %s'''
    curs.execute(sql, [email, pid])
    result = curs.fetchone()
    return result != None

def getFavorites(conn, email):
    curs = dbi.dict_cursor(conn)
    sql = '''select * from opportunity inner join favorites using (pid) where favorites.email = %s;'''
    curs.execute(sql, [email])
    return curs.fetchall()

def addFavorite(conn, email, pid):
    '''Adds opportunity to users' list of favorites, or removes if needed'''
    curs = dbi.cursor(conn)
    curs.execute('''insert into favorites(email, pid)
                values (%s, %s);''', [email, pid])
    conn.commit()

def removeFavorite(email, pid):
    '''Removes opportunity from users' list of favorites'''
    conn = dbi.connect()
    curs = dbi.cursor(conn)
    sql = '''delete from favorites where email = %s and pid = %s'''
    curs.execute(sql, [email, pid])
    conn.commit()

def look_member_name(conn, name):
    curs = dbi.dict_cursor(conn)
    sql = "select * from member where name like %s"
    curs = dbi.dict_cursor(conn)
    name = '%' + name + '%'
    curs.execute(sql, [name]) 
    return curs.fetchall()

def look_member_profession(conn, profession):
    curs = dbi.dict_cursor(conn)
    sql = "select * from member where profession like %s"
    curs = dbi.dict_cursor(conn)
    profession = '%' + profession + '%'
    curs.execute(sql, [profession]) 
    return curs.fetchall()

def look_member_type(conn, type):
    curs = dbi.dict_cursor(conn)
    sql = "select * from member where type = %s"
    curs = dbi.dict_cursor(conn)
    curs.execute(sql, [type]) 
    return curs.fetchall()


