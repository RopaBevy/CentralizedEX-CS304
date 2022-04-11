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

# to be used for testing code in this module
if __name__ == '__main__':
<<<<<<< HEAD
    pass
    conn = dbi.connect()
    print(login(conn, 'rs2@wellesley.edu'))
    print(login(conn, 'nothing here'))
