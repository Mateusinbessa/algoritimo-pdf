from db.conn import connectDB
db = connectDB()

def savePDF(fileName):
    with open(fileName, "rb") as file:
        pdf_data = file.read()
    
    sql = "INSERT INTO pdf_table (pdf_data) VALUES (%s)"

    cursor = db.cursor()
    cursor.execute(sql, (pdf_data,))

    db.commit()

    print(cursor.rowcount, "record inserted")

def getPDF():
  sql = "SELECT pdf_data FROM pdf_table ORDER BY id DESC LIMIT 1"
  cursor = db.cursor()
  cursor.execute(sql)
  result = cursor.fetchone()
  if result:
    pdf_data = result[0]
      
    with open("retrieved_pdf.pdf", "wb") as file:
        file.write(pdf_data)

    print("BLOB data has been saved to retrieved_pdf.pdf for verification.")
  else:
    print("No BLOB data found.")