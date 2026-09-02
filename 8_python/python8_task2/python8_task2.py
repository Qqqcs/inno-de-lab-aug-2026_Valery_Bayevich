import time
from typing import Callable, Any
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

def performance_logger (func: Callable) -> Callable:

    """
    Декоратор для измерения времени выполнения функции

    Args:
        func: Функция, время которой нужно измерить

    Returns:
        Обернутая функция wrapper
    
    """

    def wrapper (*args: Any, **kwargs: Any) -> Any:

        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time, TIME_DECIMALS)

        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed_time} секунд.")

        return result
    
    return wrapper

@performance_logger
def get_sorted_report( sales_data: list[dict[str, str | float]] ) -> list[dict[str, str | float]] :

    """
    Сортирует категории по выручке в порядке убывания

    Args:
        sales_data: Список словарей с названием категории и общей выручкой

    Returns: 
        Отсортированный список словарей по total_sales
    """
    return sorted (
        sales_data,
        key=lambda item: item["total_sales"],
        reverse=True
    )
print("===ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ===")
print("---Тест 1---")

sales_data = [
    {"category": "Action", "total_sales": 4311.85}, 
    {"category": "Animation", "total_sales": 4656.30}, 
    {"category": "Children", "total_sales": 3655.55} 
]

result = get_sorted_report(sales_data)

print("Топ категорий по выручке:")
for number, item in enumerate(result, start = 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")


print("---Тест 2---")

sales_data = [
    {"category": "Classics", "total_sales": 1200.10}, 
    {"category": "Comedy", "total_sales": 4000.00}, 
    {"category": "Documentary", "total_sales": 4000.00}
]

result = get_sorted_report(sales_data)

print("Топ категорий по выручке:")
for number, item in enumerate(result, start = 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")

print("---Тест 3---")

sales_data = [
    {"category": "Drama", "total_sales": 500.00} 
]

result = get_sorted_report(sales_data)

print("Топ категорий по выручке:")
for number, item in enumerate(result, start = 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")