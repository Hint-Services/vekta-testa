from collections import defaultdict
from typing import List, Dict

from vekta_testa.types import EmbeddingIndex, Testcase, TestResult
from vekta_testa.utils import default_find_id


def run_vecta_tests(embeddingIndexes: List[EmbeddingIndex], testcases: List[Testcase], target_id: str) -> Dict[str, List[TestResult]]:
    '''
    Runs the test cases against the embedding indexes and returns a test result for each index for each test case.

    :param embeddingIndexes: The list of embedding indexes to run the test cases against.
    :param testcases: The list of test cases to run.
    :param target_id: The target ID to find in the results.

    :returns: A dictionary of test results for each test case.

    If the target ID is not found in the results, the score will be 0.
    Default values for the post processor and find result functions are provided but assume search function returns a [List[Tuple[Dict[str, Any]], float]] and the target ID is a string at key 'id'.
    '''
    results = defaultdict(list)

    for testcase in testcases:
        print('Starting test - ', testcase.case_id)

        for index in embeddingIndexes:
            # Run the search function
            scoredValues = index.search_function(testcase.scenario)

            # Run the post processor
            if (index.post_processor != None):
                scoredValues = index.post_processor(
                    testcase.scenario, scoredValues)

            # Find the result
            result_index = -1
            if index.find_result != None:
                result_index = index.find_result(scoredValues, target_id)
            else:
                result_index = default_find_id(scoredValues, target_id)

            # Get the score
            if result_index == -1:
                score = 0
            else:
                (_, score) = scoredValues[result_index]

            # On first pass, initialize the list
            if testcase.case_id not in results:
                results[testcase.case_id] = []

            # Append the result
            results[testcase.case_id].append({
                "id": testcase.case_id,
                "scenario": testcase.scenario,
                "score": score,
                "embedding_name": index.index_name,
                "ranking": result_index + 1,
                "all_results": scoredValues
            })

    return results
