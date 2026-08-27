# Список ролей, переданный в запросе на авторизацию (содержит повторы) 
requested_roles = ["guest", "developer", "guest", "admin", 
"developer", "guest"] 
# Набор обязательных ролей для выполнения административных функций 
required_admin_roles = {"admin", "security_officer", 
"audit_manager"} 
# Ваш код здесь 
unique_requested_roles = set(requested_roles) # получаем уникальные роли через set, чтобы убрать повторы
general_admin_roles = unique_requested_roles.intersection(required_admin_roles) # общие админ роли через уникальные и обязательные админ роли через intersection
missing_admin_roles = required_admin_roles.difference(unique_requested_roles) # недостающие админ роли через обязат. админ роли и уникальные через difference
is_security_officer_present = "security_officer" in unique_requested_roles # проверяем наличие роли security_officer в уникальных ролях через in

print(f"Уникальные запрошенные роли: {unique_requested_roles}")
print(f"Общие административные роли: {general_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(f"Наличие роли security_officer в запросе: {is_security_officer_present}")