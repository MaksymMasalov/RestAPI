# PoetryDB API Test Cases

This repository contains test cases for the PoetryDB API. The test cases are written using Python and pytest.

## Test Cases

| Test Case ID | Description                          | Steps | Expected Result                               | Validation                                                   |
|--------------|--------------------------------------|-------|-----------------------------------------------|--------------------------------------------------------------|
| TC1          | Retrieve a Specific Poem by Title    | 1-2   | Poem "Ozymandias" by Percy Bysshe Shelley     | Status code is 200, title is "Ozymandias", author is "Percy Bysshe Shelley", content matches |
| TC2          | Retrieve Poems by Author             | 1-2   | Poems by Emily Dickinson                      | Status code is 200, author is "Emily Dickinson" for all poems, more than one poem in response |

## Validation

- **Status Code Validation:** Ensures that the API request was successful.
- **Content Validation:** Confirms that the data returned by the API matches the expected values.
- **Author Validation:** Ensures that the correct author is returned for the poems.

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/MaksymMasalov/RestAPI.git
    cd RestAPI
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the tests:
    ```sh
    pytest -v tests/test_poetrydb.py
    ```

## Dependencies

- pytest
- requests
