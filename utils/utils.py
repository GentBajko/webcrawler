from time import perf_counter

import numpy as np


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(result, f'{(finish - start):0.12f}')
        return result

    return wrapper


def get_selectors(columns: list, xpaths: list):
    if len(columns) == len(xpaths):
        return {k: v for k, v in zip(columns, xpaths)}
    raise AttributeError


def concat_keys_values(tupl):
    k, values = tupl
    return (k + v for v in values)


def split_urls(urls_list, batch_size):
    for i in np.arange(0, len(list(urls_list)), batch_size):
        yield list(urls_list)[i:i + batch_size]


if __name__ == "__main__":
    pass