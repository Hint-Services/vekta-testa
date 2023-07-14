import matplotlib.pyplot as plt
import matplotlib
from collections import defaultdict
from typing import Dict, List

from vekta_testa.types import TestResult


def plot_results(results: Dict[str, List[TestResult]], color_map: Dict[str, str], number_of_results=1000):
    '''
    Plots the results of the test cases using matplotlib.

    :param results: The results of the test cases.
    :param color_map: Colors to use for each embedding name. Must use exact names from the results.
    :param number_of_results: The number of results to show in the legend for the plot. Default is 1000.
    '''

    font = {'family': 'helvetica',
            'size': 10}

    matplotlib.rc('font', **font)

    # Initialize lists and dictionaries
    x_labels = []
    scores = defaultdict(list)
    rankings = defaultdict(list)
    graphPositions = defaultdict(list)

    # Extract scores and x_labels for each embedding
    for test_case, result_list in results.items():
        for result in result_list:
            embedding_name = result['embedding_name']  # type: ignore
            score = result['score']  # type: ignore
            ranking = result['ranking']  # type: ignore
            position = number_of_results - \
                result['ranking'] if result['ranking'] > 0 else 0
            x_labels.append(test_case)
            scores[embedding_name].append(score)
            rankings[embedding_name].append(ranking)
            graphPositions[embedding_name].append(position)

            if (embedding_name not in color_map):
                color_map[embedding_name] = 'black'

    # Create bar chart
    fig, ax = plt.subplots(figsize=(15, 6))

    x = list(set(x_labels))  # get the unique test cases
    x.sort()  # ensure they're in a consistent order
    bar_width = 0.3
    total_width = len(color_map) * bar_width
    base_positions = [i - total_width / 2 for i in range(len(x))]

    for i, (embedding_name, color) in enumerate(color_map.items()):
        positions = [base + i * bar_width for base in base_positions]
        bars = ax.bar(positions, graphPositions[embedding_name],
                      bar_width, label=embedding_name, color=color)

        # Add the ranking above each bar
        for j, bar in enumerate(bars):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f'{str(round(scores[embedding_name][j], 3))}\n({rankings[embedding_name][j]})', ha='center', va='bottom')

    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x)

    # Give extra space at the top of the graph
    y_max = ax.get_ylim()[1]
    ax.set_ylim(top=y_max*1.1)

    ax.set_ylabel(
        f"Position - Distance (Ranking # / {number_of_results} )")
    ax.yaxis.set_ticks([])

    ax.set_title("Embedding Test Results")

    # Set legend outside the plot to the right
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Show the plot
    plt.show()
