def validStartingCity(distances, fuel, mpg):
    low_i = 0
    low_rest = 0
    rest = 0
    for i in range(len(distances)):
        rest = rest + mpg * fuel[i] - distances[i]
        if rest < low_rest:
            low_rest = rest
            low_i = i + 1

    return low_i
