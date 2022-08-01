from typing import Dict
from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE: str = ('Тип тренировки: {}; '
                    + 'Длительность: {:.3f} ч.; '
                    + 'Дистанция: {:.3f} км; '
                    + 'Ср. скорость: {:.3f} км/ч; '
                    + 'Потрачено ккал: {:.3f}.')

    def get_message(self) -> str:
        return self.MESSAGE.format(self.training_type,
                                   self.duration,
                                   self.distance,
                                   self.speed,
                                   self.calories)


class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        if type(self).__name__ == 'Training':
            return 0
        raise NotImplementedError(
            f'Определите get_spent_calories в {type(self).__name__}')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(type(self).__name__,
                              self.duration,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories())
        return message


class Running(Training):
    """Тренировка: бег."""
    CALORIES_COEF_1: int = 18
    CALORIES_COEF_2: int = 20
    MIN_IN_HOUR = 60

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        duration_minutes = self.duration * self.MIN_IN_HOUR
        mean_speed = self.get_mean_speed()
        spent_calories = ((self.CALORIES_COEF_1 * mean_speed
                           - self.CALORIES_COEF_2)
                          * self.weight / self.M_IN_KM * duration_minutes)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float
    CALORIES_COEF_1: int = 0.035
    CALORIES_COEF_2: int = 0.029
    MIN_IN_HOUR = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        duration_minutes = self.duration * self.MIN_IN_HOUR
        mean_speed = self.get_mean_speed()
        spent_calories = ((self.CALORIES_COEF_1 * self.weight
                           + (mean_speed**2 // self.height)
                           * self.CALORIES_COEF_2 * self.weight)
                          * duration_minutes)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    length_pool: float
    count_pool: int
    LEN_STEP: float = 1.38
    CALORIES_COEF_1: int = 1.1
    CALORIES_COEF_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        mean_speed = self.get_mean_speed()
        spent_calories = ((mean_speed + self.CALORIES_COEF_1)
                          * self.CALORIES_COEF_2 * self.weight)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_types: Dict[str, Training] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type in training_types.keys():
        return training_types[workout_type](*data)
    print('Неизвестный тип тренировки. Подсчет калорий невозможен.')
    return Training(*data[:3])


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
