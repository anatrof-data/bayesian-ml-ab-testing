# Section Summary: Traditional (Frequentist) A/B Testing

## 1. The Core Concept: Statistical Significance
In Frequentist testing, we don't just compare two averages (Mean A vs. Mean B). We must determine if the difference is "real" or just "random noise."

### Three Factors of Significance:
1. **Effect Size**: The distance between the two means (larger is better).
2. **Sample Size ($N$)**: The amount of data collected (more is better).
3. **Variance ($\sigma^2$)**: The spread of the data (less is better).



---

## 2. Confidence Intervals (CI)
A Confidence Interval is a range of values that likely contains the true parameter (like the true CTR).
* **Formula (Z-Interval)**: $\hat{\mu} \pm Z \cdot \frac{\sigma}{\sqrt{N}}$
* **Interpretation**: "If we repeat this experiment 100 times, 95 of the resulting intervals will contain the true mean."
* **Note**: A 95% CI is narrower than a 99% CI because we are allowing for more uncertainty.

---

## 3. Hypothesis Testing Framework
We use a structured "Legal Trial" logic to make decisions:

* **Null Hypothesis ($H_0$)**: "There is no effect." Ad A and Ad B are the same. Any difference is luck.
* **Alternative Hypothesis ($H_1$)**: "There is a significant difference."
* **The Goal**: To find enough evidence to **Reject $H_0$**. 



### Sidedness:
* **Two-Sided**: Testing if A is *different* from B (either better or worse).
* **One-Sided**: Testing specifically if A is *better* than B.

---

## 4. The Z-Test API Approach
The Z-test is the standard tool for large datasets ($N > 30$).

### The Process:
1. **Input**: Data from Group A and Group B.
2. **Z-Statistic**: A score representing how many "Standard Errors" the groups are apart.
   $$Z = \frac{\hat{\mu}_A - \hat{\mu}_B}{\sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}}}$$
3. **P-Value**: The probability of seeing our data if $H_0$ were actually true.

### Decision Rule:
* **If $P < 0.05$**: Reject $H_0$. The result is **Statistically Significant**.
* **If $P \geq 0.05$**: Fail to reject $H_0$. Not enough evidence.



---

## 5. Key Terminology & Strict Rules
* **Type I Error (False Alarm)**: Rejecting $H_0$ when it was actually true (claiming a win by mistake). Controlled by the 5% threshold.
* **Type II Error (Miss)**: Failing to reject $H_0$ when a real difference existed.
* **"Fail to Reject" vs. "Accept"**: Statisticians never "Accept" $H_0$. We just say we haven't found enough evidence yet.

---

## 6. Limitations of the Frequentist Paradigm
While powerful, this approach has strict rules that are hard to follow in the real world:

1. **The Peeking Problem**: You are NOT allowed to look at the P-value and stop the test early. You must reach the pre-defined $N$.
2. **Hard to Interpret**: Businesses want to know "What is the probability A is better?". Frequentists can only say "We reject the idea that they are the same."
3. **The Multiple Testing Problem**: If you test 20 different ads at a 5% threshold, one will look "Significant" just by pure luck (**Bonferroni Correction** is needed).



---

**Summary for Developers:**
Traditional A/B testing is like an API: You put in the data, you get a P-value, and you make a Binary (Yes/No) decision. In the next section, we move to **Bayesian A/B Testing**, which is more flexible and answers business questions directly.