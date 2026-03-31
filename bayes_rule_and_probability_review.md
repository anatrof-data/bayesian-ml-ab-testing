# Section Summary: Bayes' Rule and Probability Review

## 1. Fundamentals of Probability
Probability is a number between 0 and 1 that quantifies our uncertainty about an event.

* **$P(A)$**: The probability of event A.
* **Joint Probability $P(A, B)$**: The probability that both A and B occur.
    * If events are **independent**: $P(A, B) = P(A) \cdot P(B)$.
* **Conditional Probability $P(A | B)$**: The probability of A occurring *given* that B has already occurred.
[Image of conditional probability Venn diagram]

## 2. The Product Rule
Joint probability can be expressed using conditional probability:
$$P(A, B) = P(A | B) \cdot P(B)$$
And conversely:
$$P(A, B) = P(B | A) \cdot P(A)$$

## 3. Bayes' Rule
By equating the two expressions above, we derive Bayes' Rule:
$$P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)}$$

### Components:
1. **Prior $P(A)$**: Our belief in A *before* seeing new data.
2. **Likelihood $P(B | A)$**: How likely the data B is, assuming hypothesis A is true.
3. **Posterior $P(A | B)$**: Our updated belief in A *after* seeing data B.
4. **Evidence $P(B)$**: The total probability of the data (often acts as a normalizing constant).
[Image of Bayes theorem formula components diagram]

---

## 4. Frequentist vs. Bayesian Approaches
The key difference is how we treat model parameters:

| Feature | Frequentist | Bayesian |
| :--- | :--- | :--- |
| **Parameter** | A fixed, unknown constant. | A **random variable** with a distribution. |
| **Inference** | Based only on observed data frequencies (MLE). | Updates a "Prior" belief with new data. |
| **Philosophy** | "If I repeat this 100 times..." | "Based on what I know now..." |

---

## 5. Probability Distributions Review
For A/B testing and click data, two distributions are vital:

### A. Bernoulli Distribution
Describes a single event with two outcomes (1 = click, 0 = no click).
* **Parameter $p$**: Probability of success.
* **Mean $E[X] = p$**.
* **Variance $Var(X) = p(1 - p)$**.

### B. Normal (Gaussian) Distribution
The "Bell Curve" defined by Mean ($\mu$) and Variance ($\sigma^2$).
* **Central Limit Theorem (CLT)**: With enough data (large $N$), the sample mean (CTR) will follow a Normal Distribution, even if the underlying data is Bernoulli (0s and 1s).
[Image of Central Limit Theorem showing binomial distribution approaching normal distribution as n increases]