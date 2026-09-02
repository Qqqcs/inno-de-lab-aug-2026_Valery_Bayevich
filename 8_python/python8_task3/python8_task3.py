from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(
        movie_name: str,
        days: Any,
        fine_rate: float
) -> tuple[float, float] | None:
    
    """
    Рассчитывает штраф за задержку проката и индекс возврата

    Функция обрабатывает ошибки входных данных:
    TypeError - если передан некорректный тип данных
    ValueError - если значение дней невозможно преобразовать в число
    ZeroDivisionError - если количество дней просрочки равно нулю

    Args:
        movie_name: Название фильма
        days: Количество просроченных дней
        fine_rate: Штраф за один день просрочки

    Returns:
        Кортеж из итогового штрафа и индекса возврата
        При ошибке возвращает None
    
    """

    try:

        numeric_days = float(days)

        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{movie_name}' | "
              f"Итоговый штраф {total_fine}$ | "
              f"Индекс: {return_index} \n")

        return total_fine, return_index
        
    except TypeError as e:
        print(
            "[ОШИБКА ТИПА] Некорректный тип данных"
            f" для '{movie_name}': {e} \n"
              )
        
    except ValueError as e:
        print(
            "[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни"
            f" в число для '{movie_name}': {e} \n"
            )
        
    except ZeroDivisionError as e:
        print(
            "[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки"
              f" для '{movie_name}': {e} \n"
              )
    finally:
        print("--- Проверка транзакции возврата завершена ---")

print("*** ПРОВЕРКА ВОЗВРАТОВ *** \n ")

calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3], 3.0)
