def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    index = 0
    count = 0

    for tupple in permanence_period:
        if not (type(tupple[index]) is int and type(tupple[index + 1]) is int):
            return None

        valuesList = list(range(tupple[index], tupple[index + 1] + 1))

        if target_time in valuesList:
            count += 1

    return count
