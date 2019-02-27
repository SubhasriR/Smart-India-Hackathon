import psycopg2
import psycopg2.extras

from flask import Flask, redirect, url_for, request, render_template, flash, abort

app = Flask(__name__)

@app.route("/")
@app.route("/first_nav")
def first_nav():
    return render_template('first_nav.html')

@app.route("/p_loginpage")
def p_loginpage():
    return render_template('p_loginpage.html')

@app.route("/d_loginpage", methods=['GET','POST'])
def d_loginpage():
	return render_template('d_loginpage.html')

@app.route("/doc_nav", methods=['GET','POST'])
def doc_nav():
	return render_template('doc_nav.html')


@app.route('/d_mypage',methods = ['POST', 'GET'])
def d_mypage():
    print("in d_mypg func")
    if request.method == 'POST':
        d_email = request.form['d_email']
        d_pass = request.form['d_pass']
        
        # return redirect(url_for('success'))
    else:
        d_email = request.form['d_email']
        d_pass = request.form['d_pass']
        # return redirect(url_for('success'))

    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",database="doctors", user="postgres", password="Subhasri123")
        # create a cursor
        cur = conn.cursor()
        print("Connection established")

    except (Exception, psycopg2.DatabaseError) as error:
            print(error) 

    try:
        sql = """SELECT "d_email" FROM doc_login WHERE "d_email" = %s and "d_pass" = %s; """
        # sql = """INSERT INTO medicines VALUES (%s, %s, %s); ; """
        # cur.execute(sql)
        cur.execute(sql,(d_email,d_pass,))
        print("select executed")
        x=cur.rowcount
        print(x)
        print(d_email)
        print(d_pass)
        if(x==0):
            print("invalid login")
        else:
            print("within else")
            return render_template('try.html')

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    finally:
        cur.close()
        if conn is not None:
            conn.close()
            print('Database connection closed.')    
    # return str(res)
    


if __name__ == '__main__':
    app.run(debug = True)