def check_rate(val):
    minrate = 370 #minrate =
    avgrate = 2000 #avgrate =
    if val < minrate:
        return 0
    elif val < avgrate:
        return 5
    else:
        return 10