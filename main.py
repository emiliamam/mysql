import pymysql
from config import mycursor, mydb, broker, topic, name
import paho.mqtt.client as mqtt

# создаем новый экземпляр
client = mqtt.Client(name)
client.connect(broker)

while True:

    material = []
    message = material.pop()

    # подписываемся к теме
    def on_connect(client, userdata, flags, rc):
        # введите тему, на которую нужно подписаться
        client.subscribe(topic)

    # получаем сообщения и сразу добаляем в список
    def on_message(client, userdata, msg):
        material.append(message)

    client.on_connect = on_connect
    client.on_message = on_message


    # создаем 1 таблицу со списком всех классов и столбцы
    query = "CREATE TABLE IF NOT EXISTS title_all_classes(Id INT PRIMARY KEY AUTO_INCREMENT , Class TEXT)"
    mycursor.execute(query)

    # заполняем столбцы 1 таблицы
    sql_formula = "INSERT INTO title_all_classes (id, Class) VALUES(%s, %s)"
    user1 = (material[0], material[1])
    mycursor.execute(sql_formula, user1)
    mydb.commit()



    # создаем 2 таблицу с технической составляющей класса(номер класса, этаж, кол-во парт, кол-во ламп, кол-во компьютеров)
    query2 = "CREATE TABLE IF NOT EXISTS component_classes(number_class INT, floor INT, number_desks INT , " \
             "number_lights INT , number_computers INT)"
    mycursor.execute(query2)

    # заполняем столбцы 2 таблицы
    sql_formula2 = "INSERT INTO component_classes (number_class , floor , number_desks , number_lights , number_computers)"\
                   "VALUES(%s, " \
                   "%s, %s, %s, %s)"
    user2 = (material[1], material[2], material[3], material[4], material[5])
    mycursor.execute(sql_formula2, user2)
    mydb.commit()



    # создаем 3 таблицу с параметрами(дата, время, уровень, заряд, температура, влажность, кол-во исправных ламп, углекислый
    # газ
    query3 = "CREATE TABLE IF NOT EXISTS options(date DATE, time TIME, level INT, charge INT, temperature INT, humidity "\
             "INT, light INT, carbon_dioxide INT)"
    mycursor.execute(query3)

    # заполняем столбцы 3 таблицы
    sql_formula3 = "INSERT INTO options (date, time , level , charge , temperature, humidity, light, " \
                   "carbon_dioxide) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    user3 = (material[6], material[7], material[8], material[9], material[10], material[11], material[12], material[13])
    mycursor.execute(sql_formula3, user3)
    mydb.commit()

    mycursor.close()
