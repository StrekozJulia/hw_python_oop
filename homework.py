class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность: {self.duration:.3f} ч.; '
                   f'Дистанция: {self.distance:.3f} км; '
                   f'Ср. скорость: {self.speed:.3f} км/ч; '
                   f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65  # Human step length, m
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,  # Training duration, hours
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        distance = self.get_distance()
        mean_speed = distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = type(self).__name__
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        message = InfoMessage(training_type, self.duration, distance, speed,
                              calories)
        return message


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories_coef_1 = 18
        calories_coef_2 = 20
        duration_minutes = self.duration * 60
        mean_speed = self.get_mean_speed()
        spent_calories = ((calories_coef_1 * mean_speed
                           - calories_coef_2)
                          * self.weight / self.M_IN_KM * duration_minutes)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories_coef_1 = 0.035
        calories_coef_2 = 0.029
        duration_minutes = self.duration * 60
        mean_speed = self.get_mean_speed()
        spent_calories = ((calories_coef_1 * self.weight
                           + (mean_speed**2 // self.height)
                           * calories_coef_2 * self.weight)
                          * duration_minutes)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38  # Length of human stroke, m

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool  # Pool length, m
        self.count_pool = count_pool  # How many times swimmer crossed the pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories_coef_1 = 1.1
        calories_coef_2 = 2
        mean_speed = self.get_mean_speed()
        spent_calories = ((mean_speed + calories_coef_1)
                          * calories_coef_2 * self.weight)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_types = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    current_training = training_types[workout_type](*data)
    return current_training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
