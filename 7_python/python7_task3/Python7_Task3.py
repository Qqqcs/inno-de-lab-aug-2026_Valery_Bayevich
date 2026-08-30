# Конфигурационный словарь, полученный от сервиса инициализации 
db_config = { 
"connection": { 
"host": "production-db.internal", 
"port": 5432, 
"user": "postgres" 
} 
} 

connection = db_config.get("connection", {}) # Получение словаря с параметрами соединения
host = connection.get("host") # Получение значения параметра host
port = connection.get("port") # Ну и port 

ssl_mode = connection.get("ssl_settings", {}).get( # Получили значение параметра ssl_mode
    "ssl_mode", "verify-full" # если параметр ssl_mode отсутствует, то по умолчанию будет verify-full
) 

connection["user"] = "admin" # Изменение значения параметра user
connection["max_connections"] = 100 # Изменение значения параметра max_connections (добавил новый параметр в словарь connection)

print(f"SSL Mode: {ssl_mode} ")
print("Параметры соединения:")

for key, value in connection.items(): #выводим все ключи и значения словаря connection
    print(f"--- {key}: {value}")