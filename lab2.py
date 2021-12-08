import math


def get_function(x) -> float:
    return math.pow(math.e, x) - 1.8 + math.pow(x, 2)


def get_first_derivative(x) -> float:
    return math.pow(math.e, x) + 2 * x


def get_second_derivative(x) -> float:
    return math.pow(math.e, x) - 2


def get_fi_function(x) -> float:
    return math.pow(math.e, x) / (2 * math.sqrt(1.8 - math.pow(math.e, x)))


class Resolver:
    def __init__(self, a, b, epsilon, stat_point):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.stat_point = stat_point

    def seperate_segment_on_two_halves_method(self):
        a = self.a
        b = self.b
        x = (a + b) / 2
        iteration_count = math.ceil(math.log((self.b - self.a) / self.epsilon, 2))
        print(f"Число итераций: {iteration_count}")
        for _ in range(iteration_count):
            if get_function(a) * get_function(x) < 0:
                b = x
            elif get_function(b) * get_function(x) < 0:
                a = x
            elif get_function(a) == 0:
                return a
            elif get_function(b) == 0:
                return b
            elif get_function(x) == 0:
                return get_function(x)
            x = (a + b) / 2
        print(f"Ответ: a = {a} b = {b}")

    def newton_method(self):
        iteration_count = 0
        x = self.stat_point
        while True:
            iteration_count += 1
            x_new = x - (get_function(x) / get_first_derivative(x))
            if abs(x_new - x) < self.epsilon:
                print(f'Число итераций: {iteration_count}')
                print(f'Результат: {x_new}')
                break
            x = x_new

    def modified_newton_method(self):
        iteration_count = 0
        x = self.stat_point
        while True:
            iteration_count += 1
            x_new = x - (get_function(x) / get_first_derivative(self.stat_point))
            if abs(x_new - x) < self.epsilon:
                print(f'Число итераций: {iteration_count}')
                print(f'Результат: {x_new}')
                break
            x = x_new

    def motionless_chord_method(self):
        iteration_count = 0
        x = 0
        while True:
            iteration_count += 1
            x_new = x - (get_function(x) / (get_function(x) - get_function(self.stat_point))) * (x - self.stat_point)
            if abs(x_new - x) < self.epsilon:
                print(f'Число итераций: {iteration_count}')
                print(f'Результат: {x_new}')
                break
            x = x_new

    def mobile_chord_method(self):
        iteration_count = 0
        x = 0
        x_previous = self.stat_point
        while True:
            iteration_count += 1
            x_n_plus_1 = x - (get_function(x) * (x - x_previous)) / (
                    get_function(x) - get_function(x_previous))
            if abs(x_n_plus_1 - x) < self.epsilon:
                print(f'Число итераций: {iteration_count}')
                print(f'Результат: {x_n_plus_1}')
                break
            x_previous = x
            x = x_n_plus_1

    def iteration_method(self):
        x = self.stat_point
        n = 0
        while True:
            n += 1
            x_new = get_fi_function(x)
            if abs(x_new - x) < self.epsilon:
                print(f'Число итераций: {n}')
                print(f'Результат с точностью epsilon: {x_new}')
                break
            x = x_new


if __name__ == '__main__':
    resolver = Resolver(a=0, b=1, epsilon=0.5 * 10 ** (-5), stat_point=1)
    print(f"Результаты с точностью эпсилон: {resolver.epsilon}")
    print("\nМетод деления отрезка пополам")
    resolver.seperate_segment_on_two_halves_method()
    print('\nМетод Ньютона')
    resolver.newton_method()
    print('\nМодифицированный метод Ньютона')
    resolver.modified_newton_method()
    print('\nМетод неподвижных хорд')
    resolver.mobile_chord_method()
    print('\nМетод подвижных хорд')
    resolver.motionless_chord_method()
    print('\nМетод простой итерации')
    resolver.iteration_method()
