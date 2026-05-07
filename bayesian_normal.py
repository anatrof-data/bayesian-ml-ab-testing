# https://deeplearningcourses.com/c/artificial-intelligence-reinforcement-learning-in-python
# https://www.udemy.com/artificial-intelligence-reinforcement-learning-in-python
from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


np.random.seed(1)
NUM_TRIALS = 2000
BANDIT_MEANS = [1, 2, 3]


class Bandit:
  def __init__(self, true_mean):
    # Истинное среднее значение награды. В реальности неизвестно, нужно только для генерации данных.
    self.true_mean = true_mean
    # Параметры для оценки среднего: prior (априорное распределение) принимается как Нормальное N(0,1)
    # m — наша текущая оценка среднего значения
    self.m = 0
    # lambda_ — точность (precision) нашей оценки. Точность обратно пропорциональна дисперсии (1/variance).
    self.lambda_ = 1
    # tau — точность самого распределения наград (насколько сильно шумят данные). Здесь фиксируем = 1.
    self.tau = 1
    # N — количество раз, которое мы выбрали этого бандита.
    self.N = 0

  def pull(self):
    # Получаем реальную награду из распределения N(true_mean, 1/tau)
    return np.random.randn() / np.sqrt(self.tau) + self.true_mean

  def sample(self):
    # Thompson Sampling: генерируем сэмпл из нашего текущего (posterior) убеждения N(m, 1/lambda_)
    return np.random.randn() / np.sqrt(self.lambda_) + self.m

  def update(self, x):
    # Байесовское обновление (сопряженное нормальное распределение / Normal-Normal priors):
    # Новое среднее — взвешенная сумма старого знания и нового наблюдения.
    self.m = (self.tau * x + self.lambda_ * self.m) / (self.tau + self.lambda_)
    # Точность увеличивается с каждым полученным наблюдением.
    self.lambda_ += self.tau
    self.N += 1


def plot(bandits, trial):
  x = np.linspace(-3, 6, 200)
  for b in bandits:
    # Рисуем график плотности вероятности (PDF) для текущего убеждения о среднем бандита
    y = norm.pdf(x, b.m, np.sqrt(1. / b.lambda_))
    plt.plot(x, y, label=f"real mean: {b.true_mean:.4f}, num plays: {b.N}")
  plt.title(f"Bandit distributions after {trial} trials")
  plt.legend()
  plt.show()


def run_experiment():
  bandits = [Bandit(m) for m in BANDIT_MEANS]

  # Точки (номер итерации), на которых мы визуализируем posterior распределения
  sample_points = [5,10,20,50,100,200,500,1000,1500,1999]
  rewards = np.empty(NUM_TRIALS)
  for i in range(NUM_TRIALS):
    # Thompson sampling: для каждого бандита берём сэмпл из posterior и выбираем максимальный
    j = np.argmax([b.sample() for b in bandits])

    # Отрисовываем posterior-графики
    if i in sample_points:
      plot(bandits, i)

    # Дёргаем "ручку" выбранного бандита и получаем реальную награду (Gaussian)
    x = bandits[j].pull()

    # Обновляем параметры распределения (m и lambda_) для выбранного бандита
    bandits[j].update(x)

    # Сохраняем награду в общий лог
    rewards[i] = x

  # Рассчитываем кумулятивное среднее (moving average) полученных наград на каждом шаге
  cumulative_average = np.cumsum(rewards) / (np.arange(NUM_TRIALS) + 1)

  # Рисуем график кумулятивного среднего, оно должно со временем приблизиться к 3 (лучшему true_mean)
  plt.plot(cumulative_average)
  for m in BANDIT_MEANS:
    plt.plot(np.ones(NUM_TRIALS)*m)
  plt.show()

  return cumulative_average

if __name__ == '__main__':
  run_experiment()
