
def the_sum_of_net_indicators(a: tuple):
    additional_chill = 0
    additional_pechal = 0
    pechal = 0
    strax = 0
    gnev = 0
    schaste = 0
    chill = 0
    pechal_additional_points = 0
    strax_additional_points = 0
    gnev_additional_points = 0
    schaste_additional_points = 0
    chill_additional_points = 0
    elimination_pechal = 0
    elimination_chill = 0
    additional_pechal = 0


    if a[0] > 0 and a[1] > 0:
        pechal_additional_points+=2
    if a[0] > 0 and a[1] < 0:
        strax_additional_points+=2
    if a[0] < 0 and a[1] < 0:
        gnev_additional_points+=2
    if a[0] < 0 and a[1] > 0:
        schaste_additional_points+=2
    if a[0] > 0 and a[1] > 0:
        chill_additional_points+=2


    if a[2] > 0:
        pechal+=abs(a[2])
    if a[2] < 0:
        gnev+=abs(a[2])
    if a[3] < 0:
        gnev+=abs(a[3])
    if a[3] > 0:
        chill+=abs(a[3])
    if a[4] < 0:
        strax += abs(a[4])
    if a[4] > 0:
        chill+=abs(a[4])
    if a[5] > 0:
        gnev+=abs(a[5])
    if a[5] < 0:
        schaste+=abs(a[5])
    if a[6] > 0:
        pechal+=abs(a[6])
    if a[6] < 0:
        schaste+=abs(a[6])
    if a[7] > 0:
        strax+=abs(a[7])
    if a[7] < 0:
        chill+=abs(a[7])
    if a[8] > 0:
        pechal+=abs(a[8])
    if a[8] < 0:
        schaste+=abs(a[8])


    if chill < pechal:
        elimination_pechal -= 2
    if pechal > chill:
        elimination_chill -= 2

    if pechal_additional_points > 0:
        additional_pechal = pechal_additional_points + elimination_pechal
    if chill_additional_points > 2:
        additional_chill = chill_additional_points + elimination_chill

    result_pechal = pechal + additional_pechal
    result_strax = strax + strax_additional_points
    result_gnev = gnev + gnev_additional_points
    result_schaste = schaste + strax_additional_points
    result_chill = chill + additional_chill

    return result_pechal, result_strax, result_gnev, result_schaste, result_chill









