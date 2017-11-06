import psycopg2

def prueba ():
    conn = None
    try:
        conn = psycopg2.connect(database = 'world',user='postgres',password='',host='localhost')
        cur = conn.cursor()
        #cur.callproc('avgcities', ("AFG",))
        cur.callproc('avgcities2')
        row = cur.fetchone()
        while row is not None:
            print (row[0])
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    finally:
        if conn is not None:
            conn.close()

prueba()
