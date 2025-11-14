from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="iqbal",
        password="#semarangwhj354iqbal#",
        database="flask1"
    )
    return conn

# READ: menampilkan semua pasien
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pasien")
    pasien_list = cursor.fetchall()
    conn.close()
    return render_template('index.html', pasien=pasien_list)

# CREATE: form tambah pasien
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        umur = request.form['umur']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pasien (nama, umur) VALUES (%s, %s)", (nama, umur))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('tambah.html')

# UPDATE: form edit pasien
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        nama = request.form['nama']
        umur = request.form['umur']
        cursor.execute("UPDATE pasien SET nama=%s, umur=%s WHERE id=%s", (nama, umur, id))
        conn.commit()
        conn.close()
        return redirect('/')
    cursor.execute("SELECT * FROM pasien WHERE id=%s", (id,))
    pasien = cursor.fetchone()
    conn.close()
    return render_template('edit.html', pasien=pasien)

# DELETE: hapus pasien
@app.route('/hapus/<int:id>', methods=['POST'])
def hapus(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pasien WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

