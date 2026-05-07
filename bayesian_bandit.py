# Из курса: Bayesian Machine Learning in Python: A/B Testing
# https://deeplearningcourses.com/c/bayesian-machine-learning-in-python-ab-testing
# https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing
from __future__ import print_function, division
from builtins import range
# Примечание: возможно, потребуется обновить пакет future
# sudo pip install -U future


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


# Можно зафиксировать seed, чтобы результаты эксперимента воспроизводились
# np.random.seed(2)
NUM_TRIALS = 2000
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]


class Bandit:
  def __init__(self, p):
    # Истинная вероятность выигрыша / клика для этого бандита.
    # В реальной задаче мы её не знаем, здесь она нужна только для симуляции.
    self.p = p

    # Параметры Beta-распределения: Beta(a, b).
    # a — количество успехов + 1, b — количество неудач + 1.
    # Начальное Beta(1, 1) — равномерное распределение от 0 до 1,
    # то есть до наблюдений мы считаем все значения вероятности одинаково возможными.
    self.a = 1
    self.b = 1

    # Сколько раз выбирали этого бандита. Используется только для вывода информации.
    self.N = 0

  def pull(self):
    # Симулируем реальное действие: возвращаем True с вероятностью p.
    # Для рекламы это можно интерпретировать как: True = клик, False = нет клика.
    return np.random.random() < self.p

  def sample(self):
    # Thompson Sampling: берём случайный sample из текущего posterior-распределения.
    # Чем больше данных у бандита, тем уже Beta-распределение и тем увереннее оценка.
    return np.random.beta(self.a, self.b)

  def update(self, x):
    # Байесовское обновление для Bernoulli/Beta модели:
    # если x = 1, увеличиваем количество успехов;
    # если x = 0, увеличиваем количество неудач.
    self.a += x
    self.b += 1 - x
    self.N += 1


def plot(bandits, trial):
  x = np.linspace(0, 1, 200)
  for b in bandits:
    # Рисуем текущий posterior для каждого бандита.
    # Пик распределения показывает, где алгоритм ожидает истинную вероятность клика.
    y = beta.pdf(x, b.a, b.b)
    plt.plot(x, y, label=f"real p: {b.p:.4f}, win rate = {b.a - 1}/{b.N}")
  plt.title(f"Bandit distributions after {trial} trials")
  plt.legend()
  plt.show()


def experiment():
  bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]

  # На этих шагах будем визуализировать posterior-распределения,
  # чтобы увидеть, как алгоритм становится увереннее по мере накопления данных.
  sample_points = [5,10,20,50,100,200,500,1000,1500,1999]
  rewards = np.zeros(NUM_TRIALS)
  for i in range(NUM_TRIALS):
    # Thompson Sampling:
    # 1. Для каждого бандита берём sample из его Beta posterior.
    # 2. Выбираем бандита с самым большим sample.
    #
    # Это автоматически балансирует exploration и exploitation:
    # - малоизученные бандиты имеют широкое распределение и иногда дают высокий sample;
    # - хорошо изученный хороший бандит чаще выигрывает, потому что его posterior
    #   концентрируется около высокой вероятности успеха.
    j = np.argmax([b.sample() for b in bandits])

    # Рисуем posterior-распределения в выбранные моменты эксперимента
    if i in sample_points:
      plot(bandits, i)

    # Дёргаем ручку выбранного бандита и получаем награду: 1 / True или 0 / False
    x = bandits[j].pull()

    # Сохраняем награду для расчёта общей статистики
    rewards[i] = x

    # Обновляем posterior только у того бандита, которого выбрали
    bandits[j].update(x)

  # Выводим итоговую статистику эксперимента
  print("total reward earned:", rewards.sum())
  print("overall win rate:", rewards.sum() / NUM_TRIALS)
  print("num times selected each bandit:", [b.N for b in bandits])


if __name__ == "__main__":
  experiment()
