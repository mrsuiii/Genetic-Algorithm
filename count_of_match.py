def count_of_match(arr):
    value = 0
    
    # Row Count (x-axis)
    for i in range(25):
        sumRow = arr[5*i] + arr[5*i + 1] + arr[5*i + 2] + arr[5*i + 3] + arr[5*i + 4]
        if sumRow == 315:
            value += 1

    # Column Count (y-axis)
    for i in range(5):
        for j in range(5):
            sumColumn = arr[i*25 + j] + arr[i*25 + 5 + j] + arr[i*25 + 10 + j] + arr[i*25 + 15 + j] + arr[i*25 + 20 + j]
            if sumColumn == 315:
                value += 1

    # Pillar Count (z-axis)
    for i in range(25):
        sumPillar = arr[i] + arr[i + 25] + arr[i + 50] + arr[i + 75] + arr[i + 100]
        if sumPillar == 315:
            value += 1

    # Diagonal of xy-plane Count
    for i in range(5):
        sumDiagonal1 = arr[25*i] + arr[25*i + 6] + arr[25*i + 12] + arr[25*i + 18] + arr[25*i + 24]
        if sumDiagonal1 == 315:
            value += 1

        sumDiagonal2 = arr[25*i + 4] + arr[25*i + 8] + arr[25*i + 12] + arr[25*i + 16] + arr[25*i + 20]
        if sumDiagonal2 == 315:
            value += 1

    # Diagonal of xz-plane Count
    for i in range(5):
        sumDiagonal1 = arr[5*i] + arr[5*i + 26] + arr[5*i + 52] + arr[5*i + 78] + arr[5*i + 104]
        if sumDiagonal1 == 315:
            value += 1

        sumDiagonal2 = arr[5*i + 4] + arr[5*i + 28] + arr[5*i + 52] + arr[5*i + 76] + arr[5*i + 100]
        if sumDiagonal2 == 315:
            value += 1

    # Diagonal of yz-plane Count
    for i in range(5):
        sumDiagonal1 = arr[i] + arr[i + 30] + arr[i + 60] + arr[i + 90] + arr[i + 120]
        if sumDiagonal1 == 315:
            value += 1

        sumDiagonal2 = arr[i + 20] + arr[i + 40] + arr[i + 60] + arr[i + 80] + arr[i + 100]
        if sumDiagonal2 == 315:
            value += 1

    # Space Diagonal Count
    spaceDiagonal1 = arr[0] + arr[31] + arr[62] + arr[93] + arr[124]
    spaceDiagonal2 = arr[20] + arr[41] + arr[62] + arr[83] + arr[104]
    spaceDiagonal3 = arr[4] + arr[33] + arr[62] + arr[91] + arr[120]
    spaceDiagonal4 = arr[24] + arr[43] + arr[62] + arr[81] + arr[100]

    if spaceDiagonal1 == 315:
        value += 1
    if spaceDiagonal2 == 315:
        value += 1
    if spaceDiagonal3 == 315:
        value += 1
    if spaceDiagonal4 == 315:
        value += 1

    return value

def count_SOE(arr):
    value = 0
    
    # Row Count (x-axis)
    for i in range(25):
        sumRow = arr[5*i] + arr[5*i + 1] + arr[5*i + 2] + arr[5*i + 3] + arr[5*i + 4]
        value+=abs(315-sumRow)

    # Column Count (y-axis)
    for i in range(5):
        for j in range(5):
            sumColumn = arr[i*25 + j] + arr[i*25 + 5 + j] + arr[i*25 + 10 + j] + arr[i*25 + 15 + j] + arr[i*25 + 20 + j]
            value+=abs(315-sumColumn)

    # Pillar Count (z-axis)
    for i in range(25):
        sumPillar = arr[i] + arr[i + 25] + arr[i + 50] + arr[i + 75] + arr[i + 100]
        value+=abs(315-sumPillar)

    # Diagonal of xy-plane Count
    for i in range(5):
        sumDiagonal1 = arr[25*i] + arr[25*i + 6] + arr[25*i + 12] + arr[25*i + 18] + arr[25*i + 24]
        value+=abs(315-sumDiagonal1)

        sumDiagonal2 = arr[25*i + 4] + arr[25*i + 8] + arr[25*i + 12] + arr[25*i + 16] + arr[25*i + 20]
        value+=abs(315-sumDiagonal2)

    # Diagonal of xz-plane Count
    for i in range(5):
        sumDiagonal1 = arr[5*i] + arr[5*i + 26] + arr[5*i + 52] + arr[5*i + 78] + arr[5*i + 104]
        value+=abs(315-sumDiagonal1)

        sumDiagonal2 = arr[5*i + 4] + arr[5*i + 28] + arr[5*i + 52] + arr[5*i + 76] + arr[5*i + 100]
        value+=abs(315-sumDiagonal2)

    # Diagonal of yz-plane Count
    for i in range(5):
        sumDiagonal1 = arr[i] + arr[i + 30] + arr[i + 60] + arr[i + 90] + arr[i + 120]
        value+=abs(315-sumDiagonal1)

        sumDiagonal2 = arr[i + 20] + arr[i + 40] + arr[i + 60] + arr[i + 80] + arr[i + 100]
        value+=abs(315-sumDiagonal2)

    # Space Diagonal Count
    spaceDiagonal1 = arr[0] + arr[31] + arr[62] + arr[93] + arr[124]
    spaceDiagonal2 = arr[20] + arr[41] + arr[62] + arr[83] + arr[104]
    spaceDiagonal3 = arr[4] + arr[33] + arr[62] + arr[91] + arr[120]
    spaceDiagonal4 = arr[24] + arr[43] + arr[62] + arr[81] + arr[100]

    value+= abs(315-spaceDiagonal1) + abs(315-spaceDiagonal2) + abs(315-spaceDiagonal3) + abs(315-spaceDiagonal4)

    return value
