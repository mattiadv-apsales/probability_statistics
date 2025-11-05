# Probability & Statistics Library

Author: Mattia De Vincentis
Description: A Python library for quick and easy probability and statistical analysis. Compute sample statistics, confidence intervals, and probability events with minimal code. Ideal for students, data enthusiasts, and anyone learning probability and statistics.

---

Features

Statistics

* Compute mean, variance, sample variance, and standard deviation.
* Calculate confidence intervals at 90%, 95%, and 99%.
* Quick statistical summary with statistic_planner.

Probability

* Classical probability calculations.
* Conditional probability and Bayes’ theorem.
* Favorable events, complements, unions, intersections, and symmetric differences.
* Quick probability summary with probability_planner.

---

Installation

Clone the repository and import the module in your project:

```
git clone https://github.com/YourUsername/probability_statistics.git
cd probability_statistics
```

```
from probability_statistic import *
```

---

Usage

Statistics Example

```
from probability_statistic import *

s = [5, 7, 8, 6, 9, 5]
statistic_planner(s)
```

Output:

```
mean of sample: 6.67
Variance of sample: 2.22
Campionary variance of sample: 2.67
Deviation of sample: 1.49
Confidence interval of sample: [5.48] - [7.86]
```

Probability Example

```
sample = {0, 1}  # coin flips
events = [{1}, {0}]  # heads, tails
favorables = [(3, 7), (4, 7)]  # 3 heads in 7 flips, 4 heads in 7 flips

probability_planner(events=events, sample_space=sample, favorables=favorables)
```

Output:

```
P(Event 1): 0.5 | Complement: 0.5
P(Event 2): 0.5 | Complement: 0.5
P(Favorable 1 / Total 7): 0.4286 | Complement: 0.5714
P(Favorable 2 / Total 7): 0.5714 | Complement: 0.4286
P(Event 1 | Event 2): 0.0
```

---

Functions Overview

Statistics Functions

* mean(sample)
* variance(sample, mean)
* variance_campionary(sample, mean)
* deviation(variance)
* confidence_interval_95(sample, mean, deviation)
* confidence_interval_90(sample, mean, deviation)
* confidence_interval_99(sample, mean, deviation)
* statistic_planner(sample) -> prints all statistics at once

Probability Functions

* calculate_probability(n, r)
* classical_probability(event, sample_space)
* classical_probability_numeric(favorables, total)
* conditional_probability(a, b, sample_space)
* suchasab(a, b, sample_space)
* bayes(a, b, sample_space)
* union_insiems(a, b)
* intersection_insiems(a, b)
* disjunt_insiems(a, b)
* complement_probability(probability)
* probability_planner(events, sample_space, favorables) -> prints all probability results at once

---

License
This project is licensed under the MIT License.

---