def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    index = 0
    count = 0

    for tupple in permanence_period:
        point1 = tupple[index]
        point2 = tupple[index + 1]

        if not (type(tupple[index]) is int and type(tupple[index + 1]) is int):
            return None

        valuesList = list(range(point1, point2 + 1))

        if target_time in valuesList:
            count += 1

    return count
    # print(valuesList)
    # print("point1:", point1, "point2:", point2)


# print(study_schedule([(2, 4), (4, 6), (6, 8), [2, 4]], 4))
