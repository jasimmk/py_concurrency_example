import time
from multiprocessing.pool import ThreadPool

import urllib2


def timeit(method):
    """
    A decorator to calculate the function completion time
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed


def fib(n):
    """
    Recursive fibnocci computation

    # Heavy recursion
    """
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


def calculate(x):
    """
    Multiply sum of upto fibnocci series of number
    """
    result = fib(x)
    # Deliberate sleep
    print "Fibnocci sum of {} is {}\n".format(x, result)
    return result


def fetch_url(url):
    """
    Fetches url and ensures the response code is 200
    """
    result = urllib2.urlopen(url)
    assert result.getcode() == 200, "Invalid response"
    print "Fetched url: {}".format(url)


@timeit
def process_calculate():
    """
    Function to compute an operation of number
    Aiming to use computation without IO
    """
    inputs = [1, 2, 3, 4, 5, 35, 40]
    pool_count = 5
    t = ThreadPool(pool_count)
    t.map(calculate, inputs)

@timeit
def process_fetch_url():
    """
    Function to fetch urls from server

    Limits number of threads
    """
    inputs = ['http://google.com', 'http://yahoo.com', 'http://facebook.com', 'http://abc.xyz', 'http://youtube.com', 'http://msn.com', 'http://hotmail.com', 'http://linkedin.com']
    pool_count = 3
    t = ThreadPool(pool_count)
    t.map(fetch_url, inputs)


if __name__ == '__main__':
    process_calculate()
    process_fetch_url()

