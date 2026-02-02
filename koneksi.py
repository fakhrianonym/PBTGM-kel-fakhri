import mysql.connector

# 1. Koneksi ke database db_latihan
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_latihan"
)

cursor = db.cursor()

# 2. INSERT data
sql = "INSERT INTO siswa (nama, kelas, jurusan) VALUES (%s, %s, %s)"
val = ("Alex", "11", "RPL")
cursor.execute(sql, val)
db.commit() # Menyimpan perubahan

sql = "INSERT INTO siswa (nama, kelas, jurusan) VALUES (%s, %s, %s)"
val = ("Rizky", "11", "RPL")
cursor.execute(sql, val)
db.commit() # Menyimpan perubahan

# 3. SELECT data
cursor.execute("SELECT * FROM siswa")
results = cursor.fetchall()

# 4. Tampilkan hasil di terminal
for row in results:
    print(row)

# [span_14](start_span)Menutup koneksi[span_14](end_span)
cursor.close()
db.close()