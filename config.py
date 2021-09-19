import pymysql

mydb = pymysql.connect(
              host="localhost",
              user="root",
              passwd="",

            )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS school_ITSH;")
mydb = pymysql.connect(
              host="localhost",
              user="root",
              passwd="",
              database="school_ITSH"
            )
mycursor = mydb.cursor()

# введите имя брокера/ip
broker = ""

# введите название темы, к которой нужно подписаться
topic = ""

# введите имя для экземпляра
name = ""
