class Trainee:
    """ Класс Trainee представляет стажера с именем, фамилией, баллами (score) и проходным баллом (passing_grade)"""
    def __init__ (
            self,
            name: str,
            surname: str,
            score: int = 0, 
            passing_grade: int = 10
            ):
        """ Инициализация данных стажера: имя, фамилия, баллы и проходной балл """
        self.name: str = name
        self.surname: str = surname
        self.score = score
        self.passing_grade: int = passing_grade

    #получение текущего значения score
    @property
    def score (self) -> int:
        """Возвращает текущее значение score"""
        return self.__score

    #Изменение score с проверкой на тип и значение
    @score.setter
    def score (self, value: int) -> None:
        """Устанавливает новое значение score с проверкой на тип и значение"""
        if type(value) is not int:
            raise ValueError(f"Expected value of type int, got {type(value )}") #в случае если передан не int, то ошибка

        if value < 0:
            raise ValueError(f"The score shouldn't be less than 0!") #очевидно меньше нуля быть не может
    
        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1 

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        """Возвращает True, если текущий score больше или равен passing_grade, иначе False"""
        return self.score >= self.passing_grade

class HardworkingTrainee(Trainee): # добавили трудоголиков
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2

class AuditTrainee(Trainee): # добавили вольнослушателей
    def is_passing(self) -> bool:
        """Always returns True"""
        return True

class Cohort():

    def __init__(self, title: str):
        self.title: str = title # название группы
        self.trainees: list[Trainee] = []

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет учащегося в группу"""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """ Имитирует поведение лекции - вызывает метод visit_lecture() у каждого учащегося в группе (Демонстрация полиморфизма)"""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Возвращает список всех учащихся группы, у которых метод is_passing() возвращает True"""
        passing_students = []
        for trainee in self.trainees:
            if trainee.is_passing():
                passing_students.append(trainee)
        return passing_students

# Проверка (Код с файла дз)
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10) 
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10) 
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

cohort = Cohort("Python Advanced") 
cohort.add_trainee(std_trainee) 
cohort.add_trainee(hard_trainee) 
cohort.add_trainee(audit_trainee) 

# 3. Проводим лекцию для всей группы (+1 балл всем) 
cohort.conduct_lecture() 

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла) 
hard_trainee.do_homework() 

# 5. Выводим список тех, кто проходит курс 
passing_students = cohort.get_passing_students() 
print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===") 
for student in cohort.trainees: 
    print(f"{student.name} {student.surname} | Баллы: "
   f"{student.score} | Проходит: {student.is_passing()}") 

print("\nУспешно зачислены на следующий модуль:") 
for student in passing_students: 
    print(f"- {student.name} {student.surname}") 