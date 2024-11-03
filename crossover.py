import random
import numpy as np

def custom_randomized_segment_preserving_crossover(parent1, parent2):
    
    child1 = [-1] * len(parent1)  
    child2 = [-1] * len(parent2)  
    
    protected_indices_p1 = find_protected_indices(parent1)
    protected_indices_p2 = find_protected_indices(parent2)
    
    
    for i in protected_indices_p1:
        child1[i] = parent1[i]
    for i in protected_indices_p2:
        child2[i] = parent2[i]

    unused_elements_child1 = [parent2[i] for i in range(len(parent2)) if parent2[i] not in child1]
    unused_elements_child2 = [parent1[i] for i in range(len(parent1)) if parent1[i] not in child2]
    
    fill_randomly(child1, unused_elements_child1)
    fill_randomly(child2, unused_elements_child2)

    return child1, child2

def fill_randomly(child, unused_elements):
    """Mengisi elemen yang kosong di anak dengan elemen yang tidak digunakan secara acak."""
    random.shuffle(unused_elements)  
    missing_elements = iter(unused_elements)
    
    for i in range(len(child)):
        if child[i] == -1: 
            child[i] = next(missing_elements)

def custom_probabilistic_randomized_segment_preserving_crossover(parent1, parent2, initial_prob=0.0001, peak_prob=0.01, final_prob=0.0001, iterations=1000, current_iteration=1, prob_unprotected=1.0):
    
    midpoint = iterations / 8
    if current_iteration <= midpoint:
        prob_protected = initial_prob + (peak_prob - initial_prob) * (current_iteration / midpoint)
    else:
        prob_protected = peak_prob - (peak_prob - final_prob) * ((current_iteration - midpoint) / midpoint)
       
    n = int(round(len(parent1) ** (1/3)))  
    child1 = [-1] * len(parent1)  
    child2 = [-1] * len(parent2) 

    protected_indices_p1 = find_protected_indices(parent1)
    protected_indices_p2 = find_protected_indices(parent2)
    
    # Pertahankan elemen dari segmen yang terlindungi di masing-masing child
    for i in range(len(parent1)):
        if i in protected_indices_p1 and random.random() > prob_protected:  # Gunakan > untuk mempertahankan
            child1[i] = parent1[i]
        if i in protected_indices_p2 and random.random() > prob_protected:  # Gunakan > untuk mempertahankan
            child2[i] = parent2[i]

    unused_elements_child1 = [parent2[i] for i in range(len(parent2)) if parent2[i] not in child1]
    unused_elements_child2 = [parent1[i] for i in range(len(parent1)) if parent1[i] not in child2]
    
    fill_remaining_elements_random(child1, unused_elements_child1)
    fill_remaining_elements_random(child2, unused_elements_child2)

    return child1, child2

def fill_remaining_elements_random(child, unused_elements):
    """Mengisi elemen yang kosong di anak dengan elemen yang tidak digunakan secara acak."""
    random.shuffle(unused_elements)  
    used_elements = set(child) - {-1} 
    missing_elements = [elem for elem in unused_elements if elem not in used_elements] 
    missing_elements = iter(missing_elements)
    
    for i in range(len(child)):
        if child[i] == -1:  
            child[i] = next(missing_elements, None)
            if child[i] is None:
                raise ValueError("Tidak cukup elemen unik untuk mengisi semua posisi kosong dalam child.")

def find_protected_indices(arr):
    """Mengembalikan indeks dari segmen yang mencapai magic number."""
    protected_indices = set()
    
    for i in range(25):
        sumRow = arr[5*i] + arr[5*i + 1] + arr[5*i + 2] + arr[5*i + 3] + arr[5*i + 4]
        if sumRow == 315:
            protected_indices.update([5*i, 5*i + 1, 5*i + 2, 5*i + 3, 5*i + 4])

    for i in range(5):
        for j in range(5):
            sumColumn = arr[i*25 + j] + arr[i*25 + 5 + j] + arr[i*25 + 10 + j] + arr[i*25 + 15 + j] + arr[i*25 + 20 + j]
            if sumColumn == 315:
                protected_indices.update([i*25 + j, i*25 + 5 + j, i*25 + 10 + j, i*25 + 15 + j, i*25 + 20 + j])

    for i in range(25):
        sumPillar = arr[i] + arr[i + 25] + arr[i + 50] + arr[i + 75] + arr[i + 100]
        if sumPillar == 315:
            protected_indices.update([i, i + 25, i + 50, i + 75, i + 100])

    for i in range(5):
        sumDiagonal1 = arr[25*i] + arr[25*i + 6] + arr[25*i + 12] + arr[25*i + 18] + arr[25*i + 24]
        if sumDiagonal1 == 315:
            protected_indices.update([25*i, 25*i + 6, 25*i + 12, 25*i + 18, 25*i + 24])

        sumDiagonal2 = arr[25*i + 4] + arr[25*i + 8] + arr[25*i + 12] + arr[25*i + 16] + arr[25*i + 20]
        if sumDiagonal2 == 315:
            protected_indices.update([25*i + 4, 25*i + 8, 25*i + 12, 25*i + 16, 25*i + 20])

    for i in range(5):
        sumDiagonal1 = arr[5*i] + arr[5*i + 26] + arr[5*i + 52] + arr[5*i + 78] + arr[5*i + 104]
        if sumDiagonal1 == 315:
            protected_indices.update([5*i, 5*i + 26, 5*i + 52, 5*i + 78, 5*i + 104])

        sumDiagonal2 = arr[5*i + 4] + arr[5*i + 28] + arr[5*i + 52] + arr[5*i + 76] + arr[5*i + 100]
        if sumDiagonal2 == 315:
            protected_indices.update([5*i + 4, 5*i + 28, 5*i + 52, 5*i + 76, 5*i + 100])

    for i in range(5):
        sumDiagonal1 = arr[i] + arr[i + 30] + arr[i + 60] + arr[i + 90] + arr[i + 120]
        if sumDiagonal1 == 315:
            protected_indices.update([i, i + 30, i + 60, i + 90, i + 120])

        sumDiagonal2 = arr[i + 20] + arr[i + 40] + arr[i + 60] + arr[i + 80] + arr[i + 100]
        if sumDiagonal2 == 315:
            protected_indices.update([i + 20, i + 40, i + 60, i + 80, i + 100])

    spaceDiagonal1 = arr[0] + arr[31] + arr[62] + arr[93] + arr[124]
    spaceDiagonal2 = arr[20] + arr[41] + arr[62] + arr[83] + arr[104]
    spaceDiagonal3 = arr[4] + arr[33] + arr[62] + arr[91] + arr[120]
    spaceDiagonal4 = arr[24] + arr[43] + arr[62] + arr[81] + arr[100]

    if spaceDiagonal1 == 315:
        protected_indices.update([0, 31, 62, 93, 124])
    if spaceDiagonal2 == 315:
        protected_indices.update([20, 41, 62, 83, 104])
    if spaceDiagonal3 == 315:
        protected_indices.update([4, 33, 62, 91, 120])
    if spaceDiagonal4 == 315:
        protected_indices.update([24, 43, 62, 81, 100])

    return protected_indices


def find_segments_with_magic_number(arr, magic_number=315):
    segments = {"rows": [], "columns": [], "pillars": [], "xy_diagonals": [], "xz_diagonals": [], "yz_diagonals": [], "space_diagonals": []}

    for i in range(25):
        sumRow = arr[5*i] + arr[5*i + 1] + arr[5*i + 2] + arr[5*i + 3] + arr[5*i + 4]
        if sumRow == magic_number:
            segments["rows"].append([5*i, 5*i + 1, 5*i + 2, 5*i + 3, 5*i + 4])

    for i in range(5):
        for j in range(5):
            sumColumn = arr[i*25 + j] + arr[i*25 + 5 + j] + arr[i*25 + 10 + j] + arr[i*25 + 15 + j] + arr[i*25 + 20 + j]
            if sumColumn == magic_number:
                segments["columns"].append([i*25 + j, i*25 + 5 + j, i*25 + 10 + j, i*25 + 15 + j, i*25 + 20 + j])

    for i in range(25):
        sumPillar = arr[i] + arr[i + 25] + arr[i + 50] + arr[i + 75] + arr[i + 100]
        if sumPillar == magic_number:
            segments["pillars"].append([i, i + 25, i + 50, i + 75, i + 100])

    
    for i in range(5):
        sumDiagonal1 = arr[25*i] + arr[25*i + 6] + arr[25*i + 12] + arr[25*i + 18] + arr[25*i + 24]
        if sumDiagonal1 == magic_number:
            segments["xy_diagonals"].append([25*i, 25*i + 6, 25*i + 12, 25*i + 18, 25*i + 24])

        sumDiagonal2 = arr[25*i + 4] + arr[25*i + 8] + arr[25*i + 12] + arr[25*i + 16] + arr[25*i + 20]
        if sumDiagonal2 == magic_number:
            segments["xy_diagonals"].append([25*i + 4, 25*i + 8, 25*i + 12, 25*i + 16, 25*i + 20])

    
    for i in range(5):
        sumDiagonal1 = arr[5*i] + arr[5*i + 26] + arr[5*i + 52] + arr[5*i + 78] + arr[5*i + 104]
        if sumDiagonal1 == magic_number:
            segments["xz_diagonals"].append([5*i, 5*i + 26, 5*i + 52, 5*i + 78, 5*i + 104])

        sumDiagonal2 = arr[5*i + 4] + arr[5*i + 28] + arr[5*i + 52] + arr[5*i + 76] + arr[5*i + 100]
        if sumDiagonal2 == magic_number:
            segments["xz_diagonals"].append([5*i + 4, 5*i + 28, 5*i + 52, 5*i + 76, 5*i + 100])

    for i in range(5):
        sumDiagonal1 = arr[i] + arr[i + 30] + arr[i + 60] + arr[i + 90] + arr[i + 120]
        if sumDiagonal1 == magic_number:
            segments["yz_diagonals"].append([i, i + 30, i + 60, i + 90, i + 120])

        sumDiagonal2 = arr[i + 20] + arr[i + 40] + arr[i + 60] + arr[i + 80] + arr[i + 100]
        if sumDiagonal2 == magic_number:
            segments["yz_diagonals"].append([i + 20, i + 40, i + 60, i + 80, i + 100])

    spaceDiagonal1 = arr[0] + arr[31] + arr[62] + arr[93] + arr[124]
    spaceDiagonal2 = arr[20] + arr[41] + arr[62] + arr[83] + arr[104]
    spaceDiagonal3 = arr[4] + arr[33] + arr[62] + arr[91] + arr[120]
    spaceDiagonal4 = arr[24] + arr[43] + arr[62] + arr[81] + arr[100]

    if spaceDiagonal1 == magic_number:
        segments["space_diagonals"].append([0, 31, 62, 93, 124])
    if spaceDiagonal2 == magic_number:
        segments["space_diagonals"].append([20, 41, 62, 83, 104])
    if spaceDiagonal3 == magic_number:
        segments["space_diagonals"].append([4, 33, 62, 91, 120])
    if spaceDiagonal4 == magic_number:
        segments["space_diagonals"].append([24, 43, 62, 81, 100])

    return segments


def cycle_crossover(parent1, parent2):
    child1 = [-1] * len(parent1)
    child2 = [-1] * len(parent2)
    
    def create_cycle(child, parent1, parent2):
        index = 0
        while index < len(child) and child[index] != -1:
            index += 1
        
        if index == len(child):
            return
        
        start = index
        while True:
            child[index] = parent1[index]
            index_array = np.where(parent1 == parent2[index])[0]
            if len(index_array) == 0:
                break
            index = index_array[0]
            if index == start:
                break

    create_cycle(child1, parent1, parent2)
    create_cycle(child2, parent2, parent1)

    for i in range(len(child1)):
        if child1[i] == -1:
            child1[i] = parent2[i]
        if child2[i] == -1:
            child2[i] = parent1[i]

    return child1, child2
