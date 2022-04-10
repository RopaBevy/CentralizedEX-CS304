import cs304dbi as dbi

# add to member table, use in signup
# def insert_member(email, password, name):


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
    sql = '''SELECT email, password
                    FROM member
                    WHERE email = %s'''
    curs.execute(sql, [email])
    return curs.fetchone()



# check the member table for someone

# to be used for testing code in this module
# if __name__ == '__main__':