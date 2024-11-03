import matplotlib.pyplot as plt

def plot_iteration_scores_GA(iteration_scores):
    """
    Membuat plot perkembangan skor terbaik di setiap iterasi.

    Parameters:
    iteration_scores (list of tuples): Daftar skor terbaik di setiap iterasi.
                                       Setiap tuple terdiri dari (score, index).
    """
    # Ekstrak skor dari iteration_scores
    scores = [score for score, _ in iteration_scores]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='-', color='b')
    plt.title('Best Score per Iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Best Score')
    plt.grid(True)
    plt.show()