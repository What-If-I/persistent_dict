# Persistent dictionary for Python
**Python >= 3.5 required**

## Install
    pip install . --user
    
## Usage
    from persistent_dict import PersistentDict
    d = PersistentDict()
    d['a'] = 'test'

## Install for development
    pip install .[dev] --user

## Run tests
    pytest .

## Tests coverage
    pytests . --cov=./
    coverage html