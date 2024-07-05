import requests
import pytest

BASE_URL = "https://poetrydb.org"


def test_get_poem_by_title():
    title = "Ozymandias"
    response = requests.get(f"{BASE_URL}/title/{title}")
    assert response.status_code == 200, "Status code is not 200"

    data = response.json()
    assert data[0]["title"] == title, "Title does not match"
    assert data[0]["author"] == "Percy Bysshe Shelley", "Author does not match"
    assert "I met a traveller from an antique land" in data[0]["lines"][0], "Content does not match"


def test_get_poems_by_author():
    author = "Emily Dickinson"
    response = requests.get(f"{BASE_URL}/author/{author}")
    assert response.status_code == 200, "Status code is not 200"

    data = response.json()
    assert len(data) > 0, "No poems found for the author"
    for poem in data:
        assert poem["author"] == author, f"Author does not match for poem: {poem['title']}"


if __name__ == "__main__":
    pytest.main()
