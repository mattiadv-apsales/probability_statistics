from probability_statistic import * 

s = [1, 0, 0, 1, 1, 0, 1]
statistic_planner(s)

sample = {0, 1}  # coin flips
events = [{1}, {0}]  # heads, tails
favorables = [(3, 7), (4, 7)]  # like 3 heads in 7 flips, 4 heads in 7 flips

probability_planner(events=events, sample_space=sample, favorables=favorables)