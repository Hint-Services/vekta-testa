# Vekta Testa
A test library for vector database search testing.

## About
To architect systems that deliver advanced search capabilities, we need to be able to measure and understand search results. Only through testing can we determine which approach is appropriate for our data and problem space. This library evaluates how well searches locate an expected value from a vector store and graphs the result to help communicate our findings.

![Screenshot 2023-08-20 at 6 56 31 PM](https://github.com/Hint-Services/vekta-testa/assets/2348974/8bf9620c-4c88-4886-bb71-a4110034c349)
View our [Jupyter Notebook](https://github.com/Hint-Services/vekta-testa/blob/main/tests/test_book.ipynb) for more details on this graph.

## Vecta Testa Runner
The runner is the main component of the library. It defines how the tests are run and their properties. 

```py
from vekta_testa import runner
```

Here's an example of using the runner:

```py
results = runner.run_vecta_tests(
  [
      runner.EmbeddingIndex(
          index_name='openai',
          search_function=lambda scenario: faiss_index_openai.similarity_search_with_score(scenario, k=900),
          find_result=lambda values, target: find_id(values, target),
          post_processor=lambda scenario, scored_values: post_processor(scenario, scored_values)
      ),
      runner.EmbeddingIndex(
          index_name='deepset/all-mpnet-base-v2',
          search_function=lambda scenario: mpnet_index.similarity_search_with_score(scenario, k=900),
          find_result=lambda values, target: find_id(values, target),
          post_processor=lambda scenario, scored_values: post_processor(scenario, scored_values)
      ),
  ],
  [
      runner.Testcase(
          case_id='1 - exact matching text',
          scenario="Thane has an appealing 2 BHK flat for sale with various amenities. Situated in the excellent Swastik Alps township."
      ),
      runner.Testcase(
          case_id='2 - partial match',
          scenario="Thane has an appealing 2 BHK flat for sale with various amenities. It's located in the exquisite township near the mountains."
      ),
      runner.Testcase(
          case_id='3 -  using other words',
          scenario='Offers a charming two bedroom apartment available, equipped with numerous features. Located in the prime Swastik Heights community.'
      ),
  ],
  '284'
)
```

### `EmbeddingIndex` Class

This class defines a vector solution to be used for testing.

#### Usage

```py
from vekta_testa import runner
runner.EmbeddingIndex(
    index_name='openai',
    search_function=lambda scenario: faiss_index_openai.similarity_search_with_score(scenario, k=900),
    find_result=lambda values, target: find_id(values, target),
    post_processor=lambda scenario, scored_values: post_processor(scenario, scored_values)
),
```

#### Attributes

##### `index_name: str`

The name of the index.

---

##### `search_function: Callable[[str], List[Tuple[Any, float]]]`

The function used to perform a search.

---

##### `post_processor: Optional[Callable[[str, List[Tuple[Any, float]]], List[Tuple[Any, float]]]] = None`

An optional function to post-process the results from the search function.

---

##### `find_result: Optional[Callable[[List[Tuple[Any, float]], str], int]] = None`

An optional function to find a result based on a key within the results.

---

### `Testcase` Class

This class defines the structure for a test case.

#### Usage

```python
from vekta_testa import runner

runner.Testcase(
    case_id='1-exact',
    scenario="Thane has an appealing 2 BHK flat for sale with various amenities. Situated in the excellent Swastik Alps township."
)
```

#### Attributes

##### `case_id: str`

The ID of the test case.

---

##### `scenario: str`

The scenario to test. Usually a query to search for.

---
