import json # для красивого вывода словаря в консоль
# Поток данных телеметрии от серверов кластера 
system_telemetry = [ 
("srv_01", 12.5, 64, "online"), 
("srv_02", 85.0, 92, "online"), 
("srv_03", 0.0, 0, "offline"), 
("srv_04", 45.2, 78, "online"), 
("srv_05", 95.1, 99, "online") 
] 
# Реализация конвейера агрегации метрик 
active_nodes = []
cpu_loads = []
ram_usages = []

for node_name, cpu_load, ram_usage, status in system_telemetry: #распаковка кортежей в цикле for
    if status != "online": #не трогаем офлайн узлы 
        continue

    active_nodes.append(node_name) # узлы которые в сети добавляем в список active_nodes
    cpu_loads.append(cpu_load) # та же логика только для cpu_loads и ram_usages
    ram_usages.append(ram_usage)

active_nodes_count = len(active_nodes) #вычисление итоговых метрик с помощью sum(), len(), max()
average_cpu = round(sum(cpu_loads) / len(cpu_loads), 2)
max_ram = max(ram_usages)

telemetry_report = {
    "active_nodes_count": active_nodes_count,
    "metrics": {
        "average_cpu": average_cpu,
        "max_ram": max_ram
    }
}

print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
print(json.dumps(telemetry_report, indent=4, ensure_ascii=False)) #Это для того, чтобы красиво вывести словарь (он выводился в одну строчку)