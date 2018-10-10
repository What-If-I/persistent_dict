# Persistent dictionary for Python
**Python >= 3.5 required**

## Install
    pip install git+https://github.com/What-If-I/persistent_dict --user
    
## Usage
    from persistent_dict import PersistentDict
    d = PersistentDict()
    d['a'] = 'test'

## Install for development
    git clone https://github.com/What-If-I/persistent_dict
    cd persistent_dict
    pip install .[dev] --user

## Run tests
    pytest .

## Tests coverage
    pytests . --cov=./
    coverage html