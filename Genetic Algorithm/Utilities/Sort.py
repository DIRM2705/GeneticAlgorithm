from Genetics.Individuals import Individual

def by_score(individual_list):
    minor_list = []
    mayor_list = []
    pivot = individual_list[0]
    for individual in individual_list:
        if individual == pivot:
            continue

        if individual.score >= pivot.score:
            mayor_list.append(individual)
        else:
            minor_list.append(individual)

    if len(mayor_list) > 1:
        mayor_list = by_score(mayor_list)

    if len(minor_list) > 0:
        minor_list = by_score(minor_list)

    mayor_list.append(pivot)
    for item in minor_list:
        mayor_list.append(item)
    return mayor_list
