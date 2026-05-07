# Bayesian Machine Learning in Python: A/B Testing — exercises & notes

Учебный репозиторий с конспектами, ноутбуками и упражнениями по курсу
[Bayesian Machine Learning in Python: A/B Testing](https://www.udemy.com/course/bayesian-machine-learning-in-python-ab-testing/).

Здесь собраны материалы по классическому A/B testing, доверительным интервалам,
Z-test, байесовскому мышлению и multi-armed bandit алгоритмам:

- `epsilon-greedy`
- `optimistic initial values`
- `UCB1`
- `Thompson Sampling`

Репозиторий используется как рабочая тетрадь: часть файлов — это готовые реализации,
часть — starter-упражнения с `TODO`, часть — краткие теоретические заметки.

---

## Что изучается в этом репозитории

### 1. Probability & Bayes' Rule

Базовая вероятность, условная вероятность, теорема Байеса, MLE, Bernoulli/Gaussian
распределения и связь этих идей с CTR.

Файлы:

- `bayes_rule_and_probability_review.md`
- `bayes_rule_and_probability_review_ru.md`

### 2. Classical / Frequentist A/B Testing

Классический подход к A/B тестированию:

- confidence intervals;
- hypothesis testing;
- null / alternative hypothesis;
- Z-test;
- P-value;
- statistical significance;
- ограничения frequentist-подхода.

Файлы:

- `traditional_ab_testing.md`
- `traditional_ab_testing_ru.md`
- `Confidence_Intervals.ipynb`
- `Z_test.ipynb`
- `tratidional_ab_testing_excercise.ipynb`
- `advertisement_clicks.csv`

### 3. Explore / Exploit Dilemma и Bandit Algorithms

Алгоритмы, которые вместо фиксированного A/B теста динамически распределяют трафик
между вариантами и постепенно фокусируются на лучшем.

Файлы:

- `algorithm_epsilon_greedy.md`
- `algorithm_optimistic_initial_value.md`
- `algorithm_ubc1.md`
- `algorithm_thompson_sampling.md`
- `epsilon_greedy.py`
- `comparing_epsilons.py`
- `optimistic.py`
- `ucb1.py`
- `bayesian_bandit.py`
- `bayesian_normal.py`
- `bayesian_starter.py`

---

## Структура файлов

| Файл | Что внутри |
|---|---|
| `README.md` | Описание репозитория и инструкции по запуску |
| `advertisement_clicks.csv` | Датасет A/B теста: `advertisement_id` и бинарный `action` |
| `bayes_rule_and_probability_review.md` | Конспект на английском по probability review и Bayes' Rule |
| `bayes_rule_and_probability_review_ru.md` | Русская версия конспекта по probability review и Bayes' Rule |
| `traditional_ab_testing.md` | Конспект на английском по classical / frequentist A/B testing |
| `traditional_ab_testing_ru.md` | Русская версия конспекта по classical / frequentist A/B testing |
| `algorithm_epsilon_greedy.md` | Теория Epsilon-Greedy |
| `algorithm_optimistic_initial_value.md` | Теория Optimistic Initial Values |
| `algorithm_ubc1.md` | Теория UCB1 / Upper Confidence Bound |
| `algorithm_thompson_sampling.md` | Теория Thompson Sampling |
| `epsilon_greedy.py` | Готовая реализация Epsilon-Greedy для Bernoulli bandits |
| `epsilon_greedy_starter.py` | Starter-упражнение для Epsilon-Greedy |
| `comparing_epsilons.py` | Сравнение разных значений `epsilon` на Gaussian rewards |
| `optimistic.py` | Готовая реализация Optimistic Initial Values |
| `optimistic_starter.py` | Starter-упражнение для Optimistic Initial Values |
| `ucb1.py` | Готовая реализация UCB1 |
| `ucb1_starter.py` | Starter-упражнение для UCB1 |
| `bayesian_bandit.py` | Решение Thompson Sampling (Bernoulli rewards) |
| `bayesian_normal.py` | Решение Thompson Sampling (Gaussian/Normal rewards) |
| `bayesian_starter.py` | Starter-упражнение для Thompson Sampling |
| `Confidence_Intervals.ipynb` | Ноутбук с расчётом Z/t confidence intervals |
| `Z_test.ipynb` | Ноутбук с one-sample и two-sample Z-test |
| `tratidional_ab_testing_excercise.ipynb` | Практическое A/B test упражнение на `advertisement_clicks.csv` |

---

## Данные

### `advertisement_clicks.csv`

Файл содержит результаты A/B теста рекламы.

Колонки:

| Колонка | Описание |
|---|---|
| `advertisement_id` | Вариант рекламы: `A` или `B` |
| `action` | Результат: `1` — клик, `0` — нет клика |

Используется в ноутбуке `tratidional_ab_testing_excercise.ipynb` для проверки,
есть ли статистически значимая разница между CTR рекламы `A` и рекламы `B`.

---

## Установка окружения

Минимальные зависимости для запуска скриптов и ноутбуков:

- `numpy`
- `matplotlib`
- `pandas`
- `scipy`
- `statsmodels`
- `seaborn`
- `jupyter`

Создать виртуальное окружение и установить зависимости можно так:

```zsh
cd /Users/anastasiia.trofymova/Work/courses/bayesian-ml-ab-testing
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy matplotlib pandas scipy statsmodels seaborn jupyter
```

---

## Как запускать Python-скрипты

Из корня папки:

```zsh
cd /Users/anastasiia.trofymova/Work/courses/bayesian-ml-ab-testing
source .venv/bin/activate
```

### Epsilon-Greedy

```zsh
python epsilon_greedy.py
```

Симулирует выбор между тремя bandit arms с вероятностями успеха:

```text
[0.2, 0.5, 0.75]
```

Алгоритм иногда исследует случайный вариант с вероятностью `EPS = 0.1`,
а в остальное время выбирает вариант с лучшей текущей оценкой.

### Comparing Different Epsilons

```zsh
python comparing_epsilons.py
```

Сравнивает `epsilon = 0.1`, `0.05`, `0.01` на задаче с Gaussian rewards.
Показывает, как уровень исследования влияет на cumulative average reward.

### Optimistic Initial Values

```zsh
python optimistic.py
```

Использует завышенные начальные оценки, чтобы заставить greedy-алгоритм
исследовать разные варианты без явного случайного `epsilon`.

### UCB1

```zsh
python ucb1.py
```

Использует Upper Confidence Bound:

```text
UCB = mean + sqrt(2 * log(N) / n_j)
```

Алгоритм выбирает вариант с лучшей комбинацией текущей оценки и неопределённости.

### Thompson Sampling (Bayesian Bandits)

```zsh
python bayesian_bandit.py
python bayesian_normal.py
```

Сэмплирование Томпсона на основе байесовского подхода:
- `bayesian_bandit.py` для бинарных исходов (Bernoulli-Beta).
- `bayesian_normal.py` для непрерывных исходов (Normal-Normal).

---

## Как запускать notebooks

```zsh
cd /Users/anastasiia.trofymova/Work/courses/bayesian-ml-ab-testing
source .venv/bin/activate
jupyter notebook
```

После запуска можно открыть:

- `Confidence_Intervals.ipynb`
- `Z_test.ipynb`
- `tratidional_ab_testing_excercise.ipynb`

---

## Статус упражнений

| Файл | Статус |
|---|---|
| `epsilon_greedy.py` | Готовое решение |
| `epsilon_greedy_starter.py` | Starter-файл с `TODO` |
| `comparing_epsilons.py` | Готовый эксперимент |
| `optimistic.py` | Готовое решение |
| `optimistic_starter.py` | Starter-файл с `TODO` |
| `ucb1.py` | Готовое решение |
| `ucb1_starter.py` | Starter-файл с `TODO` |
| `bayesian_bandit.py` | Готовое решение |
| `bayesian_normal.py` | Готовое решение |
| `bayesian_starter.py` | Starter-файл с `TODO` |
| `tratidional_ab_testing_excercise.ipynb` | Практическое упражнение по A/B testing |

Starter-файлы предназначены для самостоятельного заполнения после просмотра prompt-лекций
курса. В текущем виде они могут не запускаться, потому что содержат незаполненные
участки вида `# TODO`.

---

## Связь с разделами курса

| Раздел курса | Локальные материалы |
|---|---|
| Probability and Bayes' Rule Review | `bayes_rule_and_probability_review.md`, `bayes_rule_and_probability_review_ru.md` |
| Confidence Intervals | `Confidence_Intervals.ipynb` |
| Z-Test Theory / Code | `Z_test.ipynb` |
| A/B Test Exercise | `tratidional_ab_testing_excercise.ipynb`, `advertisement_clicks.csv` |
| Classical A/B Testing Section Summary | `traditional_ab_testing.md`, `traditional_ab_testing_ru.md` |
| Epsilon-Greedy Theory / Code | `algorithm_epsilon_greedy.md`, `epsilon_greedy.py`, `epsilon_greedy_starter.py` |
| Comparing Different Epsilons | `comparing_epsilons.py` |
| Optimistic Initial Values | `algorithm_optimistic_initial_value.md`, `optimistic.py`, `optimistic_starter.py` |
| UCB1 | `algorithm_ubc1.md`, `ucb1.py`, `ucb1_starter.py` |
| Bayesian Bandits / Thompson Sampling | `algorithm_thompson_sampling.md`, `bayesian_bandit.py`, `bayesian_normal.py`, `bayesian_starter.py` |

---

## Краткое описание алгоритмов

### Epsilon-Greedy

Простой baseline для explore/exploit:

- с вероятностью `epsilon` выбирает случайный вариант;
- с вероятностью `1 - epsilon` выбирает лучший известный вариант.

Плюс: очень простой.
Минус: при постоянном `epsilon` продолжает тратить часть трафика на плохие варианты.

### Optimistic Initial Values

Greedy-подход с завышенными начальными оценками.

Алгоритм пробует разные варианты, потому что каждый из них сначала выглядит
искусственно привлекательным. После реальных наблюдений оценки снижаются.

### UCB1

Выбирает вариант с максимальной верхней доверительной границей.

Балансирует:

- exploitation — высокий текущий mean;
- exploration — высокая неопределённость из-за малого числа наблюдений.

### Thompson Sampling

Байесовский bandit-подход.

Для каждого варианта хранится распределение вероятной награды. На каждом шаге
алгоритм сэмплирует значение из каждого распределения и выбирает вариант с
максимальным sample.
