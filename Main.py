from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
import hashlib
import datetime
import yagmail

x = datetime.datetime.now()
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

#blockchain = Blockchain()






@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/admin")
def admin():

    return render_template('adlog.html')
@app.route("/viewblock")
def viewblock():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
    cursor = conn.cursor()
    cursor.execute("select * from datablock")
    data = cursor.fetchall()

    return render_template('viewblock.html',data=data)

@app.route("/user")
def user():

    return render_template('user.html')
@app.route("/register")
def register():

    return render_template('register.html')
@app.route("/viewdata")
def viewdata():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
    cursor = conn.cursor()
    cursor.execute("SELECT * from iotdata ")
    data = cursor.fetchall()


    return render_template('viewdata.html',data=data)



@app.route("/login")
def emp():
    return render_template('login.html')
@app.route("/adminhome")
def adminhome():



    return render_template('adminhome.html')
@app.route("/accessmachin")
def accessmachin():



    return render_template('accessmachin.html')
@app.route("/adduser")
def adduser():
    return render_template('adduser.html')

@app.route("/viewsatellite")
def viewsatellite():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
    cursor = conn.cursor()
    cursor.execute("SELECT * from satelliteinfo ")
    data = cursor.fetchall()
    return render_template('viewsatellite.html',data=data)
@app.route("/userinfo")
def userinfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register ")
    data = cursor.fetchall()

    return render_template('userinfo.html',data=data)



@app.route("/reports")
def reports():
    return render_template('reports.html')



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':



           return render_template('adminhome.html')

       else:
        return render_template('index.html', error=error)



@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
     if request.method == 'POST':
          name = request.form['name']


          pnumber = request.form['phone']
          email = request.form['email']
          maddress = request.form['maddress']
          uname = request.form['uname']
          password = request.form['password']

          sa=request.form['acontrol']


          conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
          cursor = conn.cursor()
          cursor.execute("insert into register values('','"+name+"','"+pnumber+"','"+email+"','"+maddress+"','"+uname+"','"+password +"','"+str(sa)+"')")
          conn.commit()
          conn.close()


     return render_template('adduser.html')

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['password']
        session['uname'] = name

        # Establish DB connection
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()

        # Check credentials
        cursor.execute("SELECT * FROM register WHERE uname=%s AND password=%s", (name, password))
        data = cursor.fetchone()

        if data is None:
            # Increment login attempt count in session
            session['count'] = session.get('count', 0) + 1
            print("Failed attempt count:", session['count'])

            if session['count'] >= 3:
                # Send email notification after 3 failed attempts
                mail = 'testsam360@gmail.com'
                mail_password = 'rddwmbynfcbgpywf'
                dest = "mohamedaz1602@gmail.com"
                body = "Unknown User Trying to Access Your Site (3 failed login attempts)"

                yag = yagmail.SMTP(mail, mail_password)
                yag.send(to=dest, subject="Login Notification ...!", contents=body)
                print("Mail sent")

                # Reset the counter after email
                session['count'] = 0

            return "Username And Password Wrong"
        else:
            # Reset the failed attempt counter on successful login
            session['count'] = 0

            # Get full data again for rendering
            cursor.execute("SELECT * FROM register WHERE uname=%s AND password=%s", (name, password))
            data = cursor.fetchall()

            cursor.execute("SELECT * FROM register WHERE uname=%s AND password=%s", (name, password))
            data1 = cursor.fetchone()

            print(data1)
            d = data1[7]
            session['aname'] = d

            return render_template('UserHome.html', data=data)


@app.route("/userhome")
def userhome():
    uname=session['uname']
    aname=session['aname']
    if aname=="Full Access 1":
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + uname + "' ")
        data = cursor.fetchall()
        return render_template('userhome.html', data=data)
    elif aname=="Full Access 2":
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + uname + "' ")
        data = cursor.fetchall()
        return render_template('userhome.html', data=data)
    else:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + uname + "' ")
        data = cursor.fetchall()
        return render_template('userhome.html', data=data)




@app.route("/uviewdata")
def uviewcyberiot1():
    uname=session['uname']
    aname = session['aname']
    if aname == "Full Access 1":
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from iotdata ")
        data = cursor.fetchone()
        print(data)
        if data is None:
            data = "No data Found"
            print("test")
        else:
            return render_template('uviewdata.html', data=data)
    elif aname=="Full Access 2":
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from iotdata1 ")
        data = cursor.fetchone()
        print(data)
        if data is None:
            data = "No data Found"
            print("test")
        else:
            return render_template('uviewdata.html', data=data)
    else:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from iotdata")
        data = cursor.fetchone()
        print(data)
        return render_template('uviewdata.html', data=data)









@app.route("/dataview")
def dataview():
    uname=session['uname']

    id=request.args.get('id')
    aname=session['aname']
    key="aab12fye2312345y"
    session['key']=key
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register where uname='"+uname+"'")
    data = cursor.fetchone()
    email=data[3]
    print(email)
    mail = 'testsam360@gmail.com';
    password = 'rddwmbynfcbgpywf';
    # list of email_id to send the mail
    conn2 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')

    dest = email
    body = "Data Decryption Key:" + str(key)
    yag = yagmail.SMTP(mail, password)
    yag.send(to=dest, subject="Data Decryption Key  Details ...!", contents=body)







    return render_template('key.html')
@app.route("/keydata", methods=['GET', 'POST'])
def keydata():
    import mysql.connector
    from Crypto.Cipher import AES
    import base64

    # -------- AES Utility Functions --------
    BLOCK_SIZE = 16
    # 16-byte key for AES-128

    def pad(s):
        pad_len = BLOCK_SIZE - len(s.encode('utf-8')) % BLOCK_SIZE
        return s + (chr(pad_len) * pad_len)

    def unpad(s):
        return s[:-ord(s[-1:])]

    def encrypt(raw_text):
        raw_padded = pad(raw_text)
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_bytes = cipher.encrypt(raw_padded.encode('utf-8'))
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(enc_text):
        cipher = AES.new(key, AES.MODE_ECB)
        decoded = base64.b64decode(enc_text)
        decrypted = cipher.decrypt(decoded).decode('utf-8')
        return unpad(decrypted)

    if request.method == 'POST':
         keydata=request.form['keydata']
         key=session['key']
         if key==keydata:
             key=keydata.encode()
             aname=session['aname']
             if aname == "Full Access 1":
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("SELECT * from iotdata ")
                 data = cursor.fetchone()
                 print(data)
                 if data is None:
                     data = "No data Found"
                     print("test")
                 else:
                     print(data)
                     display_data = []
                     date = str(data[1])
                     load_temperature = decrypt(str(data[2]))
                     envi_humidity = decrypt(str(data[3]))
                     display_data.append({
                         'date': date,
                         'load_temperature': load_temperature,
                         'envi_humidity': envi_humidity
                     })


                     return render_template('uviewdata1.html', data=display_data)
             if aname == "Full Access 2":
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("SELECT * from iotdata1 ")
                 data = cursor.fetchone()
                 print(data)
                 if data is None:
                     data = "No data Found"
                     print("test")
                 else:
                     print(data)
                     display_data = []
                     date = str(data[1])
                     load_temperature = decrypt(str(data[2]))
                     envi_humidity = decrypt(str(data[3]))
                     display_data.append({
                         'date': date,
                         'load_temperature': load_temperature,
                         'envi_humidity': envi_humidity
                     })


                     return render_template('uviewdata1.html', data=display_data)

@app.route("/download")
def download():
    path = request.args.get('id')



    return send_file(path, as_attachment=True)

@app.route("/motorstatus", methods=['GET', 'POST'])
def motorstatus():
     if request.method == 'POST':
          if request.form["submit"] == "ON":
              conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
              cursor = conn.cursor()
              cursor.execute("update iotdata1 set status='1' where id='1'")
              conn.commit()
              conn.close()
              return render_template("accessmachin.html",data='1')
          if request.form["submit"] == "OFF":
              conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
              cursor = conn.cursor()
              cursor.execute("update iotdata1 set status='2' where id='1'")
              conn.commit()
              conn.close()
              return render_template("accessmachin.html", data='2')



              print("test")




@app.route("/am1")
def am1():
    aname = session['aname']
    if aname == "Full Access 1":
        conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor111 = conn111.cursor()
        cursor111.execute("select * from iotdata")
        da11 = cursor111.fetchone()
        da = da11[4]

        return render_template('am1.html', data=da)
    if aname == "Full Access 2":
        conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
        cursor111 = conn111.cursor()
        cursor111.execute("select * from iotdata1")
        da11 = cursor111.fetchone()
        da = da11[4]

        return render_template('am1.html', data=da)
    else:
        return render_template('am1.html', data=1)



@app.route("/motorstatus1", methods=['GET', 'POST'])
def motorstatus1():
     aname=session['aname']
     uname=session['uname']
     fname="Try To Access Machine Controls"
     import re, uuid
     print("The MAC address in formatted and less complex way is : ", end="")
     print('-'.join(re.findall('..', '%012x' % uuid.getnode())))
     s = '-'.join(re.findall('..', '%012x' % uuid.getnode()))
     s1 = s.upper()
     print(s1)
     if request.method == 'POST':

         if aname=="Full Access 1":
             print("test1")

             if request.form["submit"] == "ON":
                 print("on")
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("update iotdata set status='1' where id='1'")
                 conn.commit()
                 conn.close()
                 data=1
                 from firebase import firebase

                 firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com', None)

                 def update_firebase():
                     # Path in Firebase to update data
                     path = '/ESP321'  # Change this path to where you want to update data in Firebase

                     # Update data in Firebase
                     result = firebase.put(path, 'relay_state', int(data))

                     print("Data successfully updated in Firebase!")
                     return result

                 # Example data to update

                 # Update data in Firebase
                 update_firebase()
                 return render_template("am1.html", data='1')

             if request.form["submit"] == "OFF":

                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("update iotdata set status='0' where id='1'")
                 conn.commit()
                 conn.close()
                 data=0
                 from firebase import firebase

                 firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com',
                                                         None)

                 def update_firebase():
                     # Path in Firebase to update data
                     path = '/ESP321'  # Change this path to where you want to update data in Firebase

                     # Update data in Firebase
                     result = firebase.put(path, 'relay_state', int(data))

                     print("Data successfully updated in Firebase!")
                     return result

                 # Example data to update

                 # Update data in Firebase
                 update_firebase()
                 return render_template("am1.html", data='0')
         if aname=="Full Access 2":
             print("test")

             if request.form["submit"] == "ON":
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("update iotdata1 set status='1' where id='1'")
                 conn.commit()
                 conn.close()
                 data = 1
                 from firebase import firebase

                 firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com',
                                                         None)

                 def update_firebase():
                     # Path in Firebase to update data
                     path = '/ESP322'  # Change this path to where you want to update data in Firebase

                     # Update data in Firebase
                     result = firebase.put(path, 'relay_state', int(data))

                     print("Data successfully updated in Firebase!")
                     return result

                 # Example data to update

                 # Update data in Firebase
                 update_firebase()
                 return render_template("am1.html", data='1')

             if request.form["submit"] == "OFF":

                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute("update iotdata1 set status='0' where id='1'")
                 conn.commit()
                 conn.close()
                 data = 0
                 from firebase import firebase

                 firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com',
                                                         None)

                 def update_firebase():
                     # Path in Firebase to update data
                     path = '/ESP322'  # Change this path to where you want to update data in Firebase

                     # Update data in Firebase
                     result = firebase.put(path, 'relay_state', int(data))

                     print("Data successfully updated in Firebase!")
                     return result

                 # Example data to update

                 # Update data in Firebase
                 update_firebase()
                 return render_template("am1.html", data='0')
         else:
             str1 = str(aname) + str(uname)
             result = hashlib.sha1(str1.encode())

             # printing the equivalent hexadecimal value.
             print("The hexadecimal equivalent of SHA1 is : ")
             conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
             cursor = conn.cursor()
             cursor.execute("update iotdata1 set status='3' where id='1' ")
             conn.commit()
             conn.close()
             print(result.hexdigest())
             b = result.hexdigest()
             conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
             cursor = conn.cursor()
             cursor.execute("select * from datablock");
             data = cursor.fetchone()
             print(data)
             if data is None:
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute(
                     "insert into datablock values('','" + uname + "','" + str(s1) + "','" + str(
                         fname) + "','0','" + str(
                         b) + "','','" + str(x) + "')")
                 conn.commit()
                 conn.close()
             else:
                 conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor1 = conn1.cursor()
                 cursor1.execute("select max(id) from datablock")
                 da = cursor1.fetchone()
                 print(da)
                 for i in da:
                     d = i
                 print(d)
                 # str()

                 conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor111 = conn111.cursor()
                 cursor111.execute("select * from datablock where id='" + str(d) + "'")
                 da11 = cursor111.fetchall()
                 for item11 in da11:
                     df1 = item11[5]
                     print(df1)
                 conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
                 cursor = conn.cursor()
                 cursor.execute(
                     "insert into datablock values('','" + uname + "','" + str(s1) + "','" + str(fname) + "','" + str(
                         df1) + "','" + str(
                         b) + "','','" + str(x) + "')")
                 conn.commit()
                 conn.close()
             data = "Access Denied: Invalid Credentials"
             return render_template('result.html', data=data)
             print("test")





@app.route("/admindatadwnd")
def admindatadwnd():






             import csv

             conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot1')
             cursor = conn.cursor()
             cursor.execute("select * from iotdata");
             #data = cursor.fetchone()

             # Get column names
             columns = [i[0] for i in cursor.description]

             # Write data to CSV
             with open("output.csv", "w", newline="") as file:
                 writer = csv.writer(file)
                 writer.writerow(columns)  # Write column headers
                 writer.writerows(cursor.fetchall())  # Write data rows

             # Close connection
             cursor.close()
             conn.close()
             path="output.csv"

             print("Data exported successfully to output.csv")
             return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)