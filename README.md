# Beijing.py TDD workshop starter
 
https://www.meetup.com/Beijing-Python/events/pmtxglyxjbpb/

Purpose: _Everyone starts with the same environment_

## Uses:

* python 3.6
* pipenv
* pytest

## Starting Instructions

(not necessary if using `unittest` instead of `pytest`).

```bash
git clone https://github.com/JayHull/tdd-workshop.git
cd tdd-workshop
pip install pipenv  # in case you don't have it yet ;)
pipenv install
```

### Running Unittests

```bash
python roman_numerals/roman_unittest.py
```

### Running Pytest

```bash
python roman_numerals/roman_pytest.py
```

or

```bash
pytest roman_numerals/roman_pytest.py
```