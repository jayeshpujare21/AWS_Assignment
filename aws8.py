import pymysql
import sys
import logging

logging.basicConfig(format='{asctime}.{msecs:03.0f} {filename}:{lineno} {levelname} {message}',
                    level=logging.DEBUG, style='{', datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log8.txt', filemode='a')
 
def create():#Insert operation
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO recipes (`recipe_id`, `recipe_name`) VALUES (8,'sxscsc')"
            cursor.execute(sql)
            print("Task added successfully")
            #connection.commit()
    finally:
        print("Insert completed")
        logging.debug("Insert completed")

def read():#Read Operation          
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `recipe_id`, `recipe_name` FROM recipes;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("Id\t\t name")
            print("---------------------------------------------------------------------------")
            for row in result:
                print(str(row[0]) + "\t\t" + row[1])
    finally:
        print("Read completed")
        logging.debug("Read completed")

def update():#Update operation
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE recipes SET `recipe_name`=%s WHERE `recipe_id` = %s"
            cursor.execute(sql, ('Vadapav', 1))
        print("Successfully Updated...")
    finally:
        print("update completed")
        logging.debug("Update completed")

def delete():#delete operation
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM recipes WHERE recipe_id = %s"
            cursor.execute(sql, (1,))
            print("Successfully Deleted...")
    finally:
        print("delete completed")
        logging.debug("Delete completed")
 
    connection.commit()
    connection.close()
if __name__ == '__main__':
    connection = pymysql.connect(
    host='dbinstance.csaruqlxxway.us-east-1.rds.amazonaws.com',
    user=sys.argv[1],
    password=sys.argv[2],
    db='testdb',
    )
    create()
    read()
    update()
    delete()