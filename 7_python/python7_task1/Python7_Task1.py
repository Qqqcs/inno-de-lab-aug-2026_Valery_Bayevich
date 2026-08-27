# Исходная необработанная строка из источника данных  
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# разделение строки на 4 отдельных значения 
user_id, name, city, status = raw_user_record.strip().split(";")

name = name.strip().replace("_", " ").title()   #убрать пробел и заменить _ на "пробел"
city = city.strip().upper()                     #убрать пробел и привести к верхнему регистру
status = status.strip().lower()                 # тоже убрать пробел и привести к нижнему регистру

user_record = f"UID-{user_id.strip()} | Name: {name} | City: {city} | Status: {status}"

print(user_record)