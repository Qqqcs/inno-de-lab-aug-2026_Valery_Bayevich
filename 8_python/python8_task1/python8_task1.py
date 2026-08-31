MAX_RENTAL_BATCH_LIMIT = 150.0 

def calculate_rental_batch(
        quantity: int,
        rental_rate: float,
        discount: float = 0.0) -> tuple[float, bool]:

    """
    Функция для расчета итоговой стоимости парии дисков с учетом скидки

    Args:
        quantity: Количество дисков в партии
        rental_rate: Стоимость одного диска
        discount: Скидка в виде десятичного числа (По умолчанию 0.0)

    Returns: 
        Кортеж из итоговой суммы и признака превышения лимита. final_sum, is_limit_exceeded
    """

    final_sum = round(quantity * rental_rate * (1 - discount), 2)

    is_limit_exсeeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exсeeded

print ("*** ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ***")

final_sum, is_limit_exсeeded = calculate_rental_batch (30, 2.99)
print(f"Партия 1 (Аcademy Dinosaur): Сумма: {final_sum}$. Превышение лимита: {is_limit_exсeeded}")

final_sum, is_limit_exceeded = calculate_rental_batch (
    quantity=40, 
    rental_rate=4.99, 
    discount=0.1
)
print(f"Партия 2 (Affair Prejudice): Сумма: {final_sum}$. Превышение лимита: {is_limit_exсeeded}")

final_sum, is_limit_exceeded = calculate_rental_batch (10, 1.99)
print(f"Партия 3 (Аgent Truman): Сумма: {final_sum}$. Превышение лимита: {is_limit_exсeeded}")
final_sum, is_limit_exceeded = calculate_rental_batch (
    quantity=50, 
    rental_rate=3.5, 
    discount=0.2)

print(f"Партия 4 (African Egg): Сумма: {final_sum}$. Превышение лимита: {is_limit_exсeeded}")