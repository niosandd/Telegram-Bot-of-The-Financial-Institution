# a = (1, 2, 3, 0 , 2, 2, 1, 2, 1)

def sadness(a: tuple): #
    pechal = 0
    if a[2] >= 0:
        pechal += abs(a[2])
    if a[6] >= 0:
        pechal += abs(a[6])
    if a[8] >= 0:
        pechal += abs(a[8])

    if a[0] >= 0 and a[1] >= 0 and abs((a[2]) + (a[6]) + (a[8])) > abs((a[3]) + (a[4]) + (a[7])):
        pechal += 2

    return (pechal)


def fear(a: tuple):
    strax = 0

    if a[4] >= 0:
        strax += abs(a[4])
    if a[7] >= 0:
        strax += abs(a[7])
    if a[0] >= 0 and a[1] < 0:
        strax += 2

    return (strax)


def rage(a: tuple):  # 3 - 4, 4 - 3

    gnev = 0

    if a[3] <= 0:
        gnev += abs(a[3])
    if a[5] <= 0:
        gnev += abs(a[5])
    if a[2] >= 0:
        gnev += abs(a[2])
    if a[0] <= 0 and a[1] < 0:
        gnev += 2

    return (gnev)


def happiness(a: tuple):
    schaste = 0

    if a[5] <= 0:
        schaste += abs(a[5])
    if a[6] <= 0:
        schaste += abs(a[6])
    if a[8] <= 0:
        schaste += abs(a[8])

    if a[0] <= 0 and a[1] >= 0:
        schaste += 2

    return (schaste)


def calm(a: tuple):
    chill = 0

    if a[3] >= 0:
        chill += abs(a[3])
    if a[4] <= 0:
        chill += abs(a[4])
    if a[7] >= 0:
        chill += abs(a[7])

    if a[0] >= 0 and a[1] >= 0 and abs(a[3] + a[4] + a[7]) < abs(a[3] + a[4] + (a[7])):
        chill += 2

    return (chill)
