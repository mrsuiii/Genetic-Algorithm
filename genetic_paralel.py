import numpy as np
import random
import time
from concurrent.futures import ThreadPoolExecutor
import os
import sys

# Menambahkan path untuk mengimpor fungsi eksternal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.count_of_match import count_of_match
from algorithms.genetic.crossover import *

class GeneticAlgorithm:
    def __init__(self, crossover_func="randomized", population_size=100, iterations=1000, shuffle=False):
        """
        Inisialisasi solver GA.

        Parameters:
            crossover_func (str): Jenis crossover function yang akan digunakan ("randomized" atau "probabilistic").
            population_size (int): Jumlah individu dalam populasi.
            iterations (int): Jumlah iterasi algoritma genetika.
            shuffle (bool): Apakah populasi baru akan diacak setelah setiap iterasi.
        """
        self.n = 5
        self.magic_number = 315
        self.crossover_func = crossover_func
        self.shuffle = shuffle
        self.population_size = population_size
        self.iterations = iterations
        self.initial_population = self.generate_initial_population(population_size)

    def generate_initial_population(self, size=100) -> list:
        """
        Membuat populasi awal dengan elemen unik.

        Parameters:
            size (int): Jumlah individu dalam populasi.

        Returns:
            list: Populasi awal yang terdiri dari individu-individu.
        """
        population = []
        for _ in range(size):
            individual = np.random.permutation(self.n ** 3) + 1
            population.append(individual)
        return population

    def find_best_individual(self, population):
        """
        Menemukan individu terbaik dalam populasi berdasarkan skor.

        Parameters:
            population (list): Daftar individu dalam populasi.

        Returns:
            np.array: Individu dengan skor tertinggi dalam populasi.
        """
        scores = self.count_score(population)
        best_index = np.argmax(scores)
        return population[best_index]

    def count_score(self, population) -> list:
        """
        Menghitung skor untuk setiap individu dalam populasi.

        Parameters:
            population (list): Daftar individu dalam populasi.

        Returns:
            list: Daftar skor untuk setiap individu.
        """
        scores = []
        for individual in population:
            scores.append(count_of_match(individual))
        return scores

    def selection(self, population, scores, k=1) -> list:
        """
        Memilih individu dari populasi dengan weighted selection.

        Parameters:
            population (list): Daftar individu dalam populasi.
            scores (list): Daftar skor untuk setiap individu.
            k (int): Jumlah individu yang dipilih.

        Returns:
            list: Individu yang terpilih dari populasi.
        """
        weights = scores if np.sum(scores) > 0 else None
        selected_population = random.choices(population, weights=weights, k=k)
        return selected_population[0]

    def mutate(self, individual):
        """
        Melakukan mutasi pada individu dengan menukar dua elemen acak.

        Parameters:
            individual (np.array): Individu yang akan dimutasi.

        Returns:
            np.array: Individu yang telah dimutasi.
        """
        idx1, idx2 = random.sample(range(self.n ** 3), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        return individual

    def genetic_algorithm(self):
        """
        Menjalankan algoritma genetika untuk menemukan solusi terbaik.

        Returns:
            dict: Informasi konfigurasi akhir, indeks terbaik, dan skor iterasi.
        """
        best_score = 0
        population = self.initial_population
        iteration_scores = []
        for iter in range(self.iterations):
            scores = self.count_score(population)
            individual_with_best_score = np.argmax(scores)
            best_score = scores[individual_with_best_score]
            # Simpan skor terbaik untuk setiap iterasi
            iteration_scores.append((best_score, individual_with_best_score))
            if (iter + 1) % 10 == 0:
                print(f"Best score in {iter + 1}-iterations: {best_score} state ke: {individual_with_best_score}")

            new_population = []
            with ThreadPoolExecutor() as executor:
                # Membuat anak-anak secara paralel
                futures = [
                    executor.submit(self.create_children, population, scores, self.crossover_func, iter, self.iterations)
                    for _ in range(self.population_size // 2)
                ]
                for future in futures:
                    child1, child2 = future.result()
                    new_population.extend([child1, child2])

            if self.shuffle:
                random.shuffle(new_population)
            population = new_population

        final_solution_index = np.argmax(scores)
        final_solution = population[final_solution_index]
        
        solution = {
            "config": final_solution,
            "index": final_solution_index,
            "iteration_scores": iteration_scores,
            "best_score" : best_score
        }
        return solution

    def create_children(self, population, scores, crossover_func, iter, total_iteration):
        """
        Membuat anak-anak dari dua induk menggunakan crossover dan mutasi.

        Parameters:
            population (list): Daftar individu dalam populasi.
            scores (list): Daftar skor untuk setiap individu.
            crossover_func (str): Jenis crossover yang akan digunakan.
            iter (int): Iterasi saat ini.
            total_iteration (int): Total iterasi yang akan dijalankan.

        Returns:
            tuple: Dua anak yang dihasilkan dari crossover dan mutasi.
        """
        parent1 = self.selection(population, scores)
        parent2 = self.selection(population, scores)

        # Pilih crossover function berdasarkan crossover_func
        if crossover_func == "randomized":
            child1, child2 = custom_randomized_segment_preserving_crossover(parent1, parent2)
        else:
            child1, child2 = custom_probabilistic_randomized_segment_preserving_crossover(parent1, parent2, iterations=total_iteration, current_iteration=iter)

        # Mutasi pada anak-anak dengan probabilitas 10%
        if random.random() < 0.1:
            child1 = self.mutate(child1)
        if random.random() < 0.1:
            child2 = self.mutate(child2)

        return child1, child2

    def solve(self) -> dict:
        """
        Menjalankan algoritma genetika dan memberikan hasil solusi.

        Returns:
        dict: Dictionary dengan informasi solusi berdasarkan opsi yang dipilih dalam `isi`, berisi elemen berikut:
        
            - "elapsed_time" (float): Waktu yang dibutuhkan untuk menjalankan algoritma dalam detik.
            - "best_initial_state" (np.array): Individu terbaik dalam populasi awal.
            - "best_index" (int): Indeks individu terbaik pada akhir iterasi.
            - "best_config" (np.array): Konfigurasi terbaik yang ditemukan oleh algoritma genetika.
            - "iteration_scores" (list of tuples): Daftar skor terbaik di setiap iterasi dalam bentuk tuple, di mana setiap tuple terdiri dari:
                - score (int): Skor terbaik pada iterasi tersebut.
                - index (int): Indeks individu terbaik dalam populasi pada iterasi tersebut.
        """
        start_time = time.time()
        solution = self.genetic_algorithm()
        end_time = time.time()
        elapsed_time = round(end_time - start_time,5)  
        initial_population = self.initial_population
        best_initial_individual = self.find_best_individual(initial_population)
        index = solution['index']
        best_config = solution['config']
        iteration_scores = solution['iteration_scores']
        matched_list = find_segments_with_magic_number(best_config)
        solution = {
            "elapsed_time": elapsed_time,
            "best_initial_state": best_initial_individual,
            "best_index": index,
            "best_config": best_config,
            "iteration_scores": iteration_scores,
            "matched_list": matched_list,
            "best_score": solution["best_score"]
        }
        return solution
