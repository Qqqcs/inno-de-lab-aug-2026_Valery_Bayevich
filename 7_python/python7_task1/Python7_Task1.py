# Исходная необработанная строка из источника данных  
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# разделение строки на 4 отдельных значения 
user_id, name, city, status = raw_user_record.strip().split(";")

user_id = user_id.strip()                       #убрать пробелы по краям
name = name.strip().replace("_", " ").title()   #убрать пробел и заменить _ на "пробел"
city = city.strip().upper()                     #убрать пробел и привести к верхнему регистру
status = status.strip().lower()                 # тоже убрать пробел и привести к нижнему регистру

user_id = f"UID-{user_id}"
name = name.replace("_", " ").title()
city = city.upper()
status = status.lower()

user_record = " | ".join([user_id, name, city, status]) # объединяем все значения в одну строку через join

print(f"Нормализованная запись: {user_record}")