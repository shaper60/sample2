# -*- encoding:utf-8 -*-
import unicodedata
import mysql.connector

cnn = mysql.connector.connect(host='localhost',
                              port=3306,
                              db='warrantee-db',
                              user='warrantee',
                              passwd='7qHpUN3K')
cur = cnn.cursor()

#img_bigのサイズを変更
cur.execute("UPDATE product SET img_big=replace(img_big,'128x128','600x600') ")

#product_nameがNULLのレコードを削除
cur.execute("DELETE FROM product WHERE product_name is null")
cur.execute("DELETE FROM product WHERE product_name = %s", ("",))
cur.execute("DELETE FROM product WHERE product_name = %s", ("null",))

#product_name, kataban, makerを正規表現に変換
#select
cur.execute("SELECT * FROM product ")
rows = cur.fetchall()
#update_kataban
for row in rows:
	if row[2] != None:
		ROW2 = unicodedata.normalize('NFKC', row[2].strip())
		print (row[2], ROW2)
		QUERY = "UPDATE product SET kataban = %s WHERE id = %s"
		cur.execute(QUERY, (ROW2,row[0],))	
#update_product_name
for row in rows:
	if row[3] != None:
		ROW3 = unicodedata.normalize('NFKC', row[3].strip())
		print (row[3], ROW3)
		QUERY = "UPDATE product SET product_name = %s WHERE id = %s"
		cur.execute(QUERY, (ROW3,row[0],))	
#update_maker
for row in rows:
	if row[9] != None:
		ROW9 = unicodedata.normalize('NFKC', row[9].strip())
		print (row[9], ROW9)
		QUERY = "UPDATE product SET maker = %s WHERE id = %s"
		cur.execute(QUERY, (ROW9,row[0],))	

cnn.commit()

cur.close()
cnn.close()

