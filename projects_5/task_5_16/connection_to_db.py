import psycopg2



try:

    # Устанавливаем соединение

    connection = psycopg2.connect(

        host="localhost",          # База в контейнере, но доступна через localhost

        port="5434",               # Порт из секции ports

        user="postgres_task",           # POSTGRES_USER

        password="student",        # POSTGRES_PASSWORD

        database="student"          # POSTGRES_DB

    )

    print("Подключение к базе данных прошло успешно!")



except Exception as error:

    print(f"Ошибка при подключении: {error}")

cursor = connection.cursor()

cursor.execute("select name, product_id from suppliers;")
suppliers = cursor.fetchall()
for name in suppliers:
    print(f"Поставщик: {name[0]} {name[1]}")
cursor.close()