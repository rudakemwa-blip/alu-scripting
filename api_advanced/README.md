# Reddit API Advanced

This project uses the Reddit API and Python Requests to retrieve and process
subreddit information.

## Requirements

- Python 3
- Requests library
- Internet connection

## Tasks

- `0-subs.py`: Returns the number of subreddit subscribers.
- `1-top_ten.py`: Prints the first ten hot post titles.
- `2-recurse.py`: Recursively retrieves all hot post titles using pagination.
- `3-count.py`: Recursively counts keyword occurrences in hot post titles.

## Usage

Import the functions from their respective modules.

Example:

```python
from importlib.machinery import SourceFileLoader

module = SourceFileLoader("subs", "0-subs.py").load_module()
print(module.number_of_subscribers("python"))
```
