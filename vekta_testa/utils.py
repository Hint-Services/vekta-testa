from typing import Callable, List, Optional, Tuple, Any, Dict

from vekta_testa.types import TestResult


def flatten_json(y):
    '''
    Takes a JSON object and flattens it so that the keys are the paths of the
    nested keys and the value is the value of the nested key.
    '''

    out = {}

    # recursively flatten json structures
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        elif x is not None:
            out[name[:-1]] = x

    flatten(y)
    return out


def default_find_id(entries: List[Tuple[Dict[str, Any], float]], target_id: str):
    for index, (entry, ) in enumerate(entries):
        if entry['id'] == target_id:
            return index
    return -1


def tabularize_results(results: Dict[str, List[TestResult]], test_case: str, index_of_result: int, custom_scraper: Optional[Callable[[Any, float], List[Any]]] = None):
    '''
    Takes the results of a test case and returns a pandas dataframe with the top 10 results.

    :param results: The results of the test cases.
    :param test_case: The test case to tabularize.
    :param index_of_result: The index of the result to tabularize.
    :param custom_scraper: A function to scrape the results. Must return a list of values.

    :returns: A pandas dataframe with the top 10 results.
    '''

    import pandas as pd
    data = []
    for (value, score) in (results[test_case][index_of_result]['all_results'][:10]):
        if custom_scraper != None:
            data.append(custom_scraper(value, score))
        else:
            data.append([score, value])

    pd.set_option("display.max_colwidth", 10000)
    df = pd.DataFrame(data)
    return df
