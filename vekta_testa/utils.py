from typing import List, Tuple, Any, Dict

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
    for index, (entry, score) in enumerate(entries):
        if entry['id'] == target_id:
            return index
    return -1
