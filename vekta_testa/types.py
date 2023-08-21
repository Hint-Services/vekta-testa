from typing import Callable, List, Tuple, Any, Optional
from dataclasses import dataclass


@dataclass
class EmbeddingIndex:
    """
    Definition of an vector solution to be used for testing.
    """

    index_name: str
    """The name of the index."""

    search_function: Callable[[str], List[Tuple[Any, float]]]
    """
    The function to perform a search.
    """

    post_processor: Optional[Callable[[
        str, List[Tuple[Any, float]]], List[Tuple[Any, float]]]] = None
    """
    The function to post-process the results from the search function.
    """

    find_result: Optional[Callable[[List[Tuple[Any, float]], str], int]] = None
    """
    The function to find a result based on a key within the .
    """


@dataclass
class Testcase:
    '''
    Definition of a test case.
    '''

    case_id: str
    '''
    The ID of the test case.
    '''

    scenario: str
    '''
    The scenario to test. Usually a query to search for.
    '''


@dataclass
class TestResult:
    '''
    A result from a test case.
    '''

    id: str
    '''
    The ID of the related test case.
    '''

    scenario: str
    '''
    The scenario that was tested.
    '''

    score: float
    '''
    The score (relevance) of the result computed during search or in the post-processor.
    '''

    embedding_name: str
    '''
    The name of the embedding that was used.
    '''

    ranking: int
    '''
    The placement of the result in the list of results. 1 is first place. 0 is not found.
    '''

    all_results: List[Tuple[Any, float]]
    '''
    The list of all results from the search function.
    '''
