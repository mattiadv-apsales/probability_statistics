from math import sqrt

def factorial(number: float):
    """ Calculate factorial of n """
    ris = 1
    normalize_number = int(number)
    for x in range(1, normalize_number + 1):
        ris *= x
    return ris

def calculate_probability(n, r):
    """Combinazioni C(n, r)"""
    ris = factorial(n) / (factorial(r) * factorial(n - r))
    return ris

def classical_probability(e, s):
    """P(E) = |E| / |S|"""
    ris = len(e) / len(s)
    return ris

def union_insiems(a, b):
    return a.union(b)

def intersection_insiems(a, b):
    """Intersezione A ∩ B"""
    return a.intersection(b)

def disjunt_insiems(e, b):
    """Disgiunzione simmetrica"""
    return e.symmetric_difference(b)

def complement_probability(pa):
    """Complementare: 1 - P(A)"""
    return 1 - pa

def classical_probability_numeric(eventi_favorevoli, eventi_possibili):
    """P(E) = casi favorevoli / casi possibili"""
    ris = eventi_favorevoli / eventi_possibili
    return ris

def conditional_probability(a, b, s):
    """P(A|B) = P(A ∩ B) / P(B)"""
    inter = intersection_insiems(a, b)
    pab = classical_probability(inter, s)
    pb = classical_probability(b, s)
    return pab / pb

def suchasab(a, b, s):
    """P(B|A)"""
    inter = intersection_insiems(a, b)
    pba = classical_probability(inter, s) / classical_probability(a, s)
    return pba

def bayes(a, b, s):
    """Teorema di Bayes: P(A|B) = (P(B|A) * P(A)) / P(B)"""
    pba = suchasab(a, b, s)
    pa = classical_probability(a, s)
    pb = classical_probability(b, s)
    return (pba * pa) / pb

# parte di statistica

def mean(sample):
    """ Return the mean of a sample """
    u = 0
    d = len(sample)
    for e in sample:
        u += e
    
    mean = u / d
    return round(mean, 2)

def variance(sample, absolute_x):
    """ Return the variance of a sample """
    u = 0
    d = len(sample)

    for e in sample:
        u += (e - absolute_x)**2
    
    return round(u / d, 2)

def variance_campionary(sample, absolute_x):
    """ Return the campionary variance of a sample """
    u = 0
    d = len(sample) - 1

    for e in sample:
        u += (e - absolute_x)**2

    return round(u / d, 2)

def deviation(variance_sample):
    """ Return the deviation of a sample """
    return round(sqrt(variance_sample), 2)

def confidence_interval_95(sample, absolute_x, deviation_s):
    """ Return the confidence interval (95%) of a sample """
    n = len(sample)
    x = absolute_x
    o = deviation_s

    x_positive = x + 1.96 * (o / sqrt(n))
    x_negative = x - 1.96 * (o / sqrt(n))

    result = [x_negative, x_positive]
    ris = [round(e, 2) for e in result]
    return ris

def confidence_interval_90(sample, absolute_x, deviation_s):
    """ Return the confidence interval (95%) of a sample """
    n = len(sample)
    x = absolute_x
    o = deviation_s

    x_positive = x + 1.645 * (o / sqrt(n))
    x_negative = x - 1.645 * (o / sqrt(n))

    result = [x_negative, x_positive]
    ris = [round(e, 2) for e in result]
    return ris

def confidence_interval_99(sample, absolute_x, deviation_s):
    """ Return the confidence interval (95%) of a sample """
    n = len(sample)
    x = absolute_x
    o = deviation_s

    x_positive = x + 2.576 * (o / sqrt(n))
    x_negative = x - 2.576 * (o / sqrt(n))

    result = [x_negative, x_positive]
    ris = [round(e, 2) for e in result]
    return ris

def probability_planner(events=None, sample_space=None, favorables=None):
    """
    Print common probability calculations:
    - Classical probability using sets
    - Classical probability using numbers
    - Complement
    - Conditional probability (if events given)
    """
    
    if sample_space is None:
        print("Sample space required!")
        return
    
    n = len(sample_space)
    
    if events is not None:
        for i, e in enumerate(events, 1):
            p = classical_probability(e, sample_space)
            comp = complement_probability(p)
            print(f"P(Event {i}): {round(p, 4)} | Complement: {round(comp, 4)}")
    
    if favorables is not None:
        for i, (fav, total) in enumerate(favorables, 1):
            p_num = classical_probability_numeric(fav, total)
            comp_num = complement_probability(p_num)
            print(f"P(Favorable {i} / Total {total}): {round(p_num, 4)} | Complement: {round(comp_num, 4)}")
    
    # Conditional probability if two events
    if events is not None and len(events) >= 2:
        for i in range(len(events)-1):
            a, b = events[i], events[i+1]
            cond = conditional_probability(a, b, sample_space)
            print(f"P(Event {i+1} | Event {i+2}): {round(cond, 4)}")
    
    return 0

def statistic_planner(sample):
    """ The function will print all necessarly for statistic calulation """
    mean_sample = mean(sample)
    variance_sample = variance(sample, mean_sample)
    campionary_variance = variance_campionary(sample, mean_sample)
    deviation_sample = deviation(variance_sample)
    confindence_interval_sample = confidence_interval_95(sample, mean_sample, deviation_sample)

    print(f"mean of sample: {mean_sample}")
    print(f"Variance of sample: {variance_sample}")
    print(f"Campionary variance of sample: {campionary_variance}")
    print(f"Deviation of sample: {deviation_sample}")
    print(f"Confidence interval of sample: [{confindence_interval_sample[0]}] - [{confindence_interval_sample[1]}]")

    return 0