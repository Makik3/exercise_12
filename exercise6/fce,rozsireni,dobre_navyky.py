def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)


print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1

# parametr (tp cp je uvedene v hlavicce) vs argument (konkretni hodnoty)

