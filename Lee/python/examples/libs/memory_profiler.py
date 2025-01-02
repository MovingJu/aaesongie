from memory_profiler import memory_usage

def memory_profiler(func: 'function') -> 'function':
    """
##### A decorator to track memory usage of a function.
    
### Args: 
func(function)

### Returns:
result of original function.

### Usage example:
```python
@memory_profiler
def ex():
    data = [i for i in range(10**5)]
    return sum(data)
ex()
```
### Note:
Use it in a decorator syntax.
    
"""

    def wrapper(*args, **kwargs):

        mem_usage = memory_usage((func, args, kwargs))

        print(f"Memory usage during execution: {max(mem_usage)} MiB")

        return func(*args, **kwargs)
    
    return wrapper


if __name__ == '__main__':
    @memory_profiler
    def ex():
        data = [i for i in range(10**5)]
        return sum(data)
    
    ex()