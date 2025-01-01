import time
from typing import Callable


def stopwatch(func: 'function') -> 'function':
    """
##### A decorator that measures the execution time of a function.
    
### Args: 
func(function)

### Returns:
result of original function.

### Usage example:
```python
@stopwatch
def sec_timer():
    for i in range(1, 2, 1):
        time.sleep(1)
```
### Note:
Use it in a decorator syntax.
    
"""

    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"overall elapsed time: {round(end - start, 3)}")

        return result
    
    return wrapper



if __name__ == "__main__":

    @stopwatch
    def sec_timer():
        for i in range(1, 2, 1):
            time.sleep(1)

    sec_timer()

    print(stopwatch.__doc__)