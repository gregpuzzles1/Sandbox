def my_function():
    return results

if __name__ == '__main__':
    import timeit
    t = timeit.Timer("my_function()", "from __main__ import my_function")
    print t.timeit(1000)
