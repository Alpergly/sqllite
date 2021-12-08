import function
import sqlite3
db=sqlite3.connect('deneme.db')
#db1=sqlite3.connect('C:/Users/alper/OneDrive/Masaüstü/sqlite/deneme1.db')

imlec=db.cursor()
#imlec.execute("""CREATE TABLE
#veriler(marka,model,yıl)""")

kmt="CREATE TABLE IF NOT EXIST veriler(marka,model,yıl)"
#kmt="INSERT INTO veriler VALUES('Ford','Focus',18)"
#imlec.execute(kmt)
#db.commit()

kmt="Select * from veriler"
imlec.execute(kmt)
"""
bilgiler=imlec.fetchall()
print(bilgiler)
for bilgi in imlec:
    print(bilgi)
"""
"""
kmt="Select * from veriler where marka='Mercedes'"
imlec.execute(kmt)
bilgi = imlec.fetchone()
print("Marka: "+str(bilgi[0]))
print("Model: "+str(bilgi[1]))
print("Yıl: "+str(bilgi[2]))
"""
"""
kmt="select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchmany(3)
print (bilgiler)

kmt="Select * from veriler"
imlec.execute(kmt)
for bilgi in range(2):
    print(imlec.fetchone())
    """
"""
kmt="UPDATE veriler SET yıl=? where marka=?"
imlec.execute(kmt,(14,'Mercedes'))
db.commit()

kmt="Select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchall()
print(bilgiler)
"""
"""
kmt="Delete from veriler where marka = ?"
imlec.execute(kmt,('BMW',))
db.commit()
kmt="Select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchall()
print(bilgiler)
"""

#Kendime Ait Parametre Kısmım

kmt ="Select *from veriler"
bilgiler=function.listele(db,kmt).fetchall()
print(bilgiler)

kmt="INSERT INTO veriler VALUES('Volvo','S90',21)"
ekleme=function.parametreliSorgular(db,kmt).fetchall()
print(ekleme)


komut="UPDATE veriler SET yıl=? where model=?"
imlec.execute(komut,(21,'C200'))
db.commit()
guncelleme=function.parametreliSorgular2(db,komut).fetchall()


db.close()