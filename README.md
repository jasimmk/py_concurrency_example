## Concurrent Operations @ Python 2.7 example
Run the samples on python 2.7 and findout async example is faster compared to Multiprocessing and Multithreading when IO operations are involved(URL Fetch).

Libaries used
- multiprocessing
- theading
- gevent

### Requirements
- Python 2.7
- `pip install -r requiements.txt`

### Running
#### Gevent Result
```
$ python multi_gevent.py
Fibnocci sum of 1 is 1
Fibnocci sum of 2 is 1
Fibnocci sum of 3 is 2
Fibnocci sum of 4 is 3
Fibnocci sum of 5 is 5
Fibnocci sum of 35 is 9227465
Fibnocci sum of 40 is 102334155
'process_calculate' ((), {}) 34.75 sec

Fetched url: http://google.com
Fetched url: http://abc.xyz
Fetched url: http://youtube.com
Fetched url: http://msn.com
Fetched url: http://linkedin.com
Fetched url: http://yahoo.com
Fetched url: http://facebook.com
Fetched url: http://hotmail.com
'process_fetch_url' ((), {}) 5.82 sec
```
#### Multiprocessing
```
$ python multi_process.py
Fibnocci sum of 1 is 1
Fibnocci sum of 2 is 1
Fibnocci sum of 3 is 2
Fibnocci sum of 4 is 3
Fibnocci sum of 5 is 5
Fibnocci sum of 35 is 9227465
Fibnocci sum of 40 is 102334155
'process_calculate' ((), {}) 34.08 sec

Fetched url: http://google.com
Fetched url: http://abc.xyz
Fetched url: http://yahoo.com
Fetched url: http://youtube.com
Fetched url: http://facebook.com
Fetched url: http://msn.com
Fetched url: http://linkedin.com
Fetched url: http://hotmail.com
'process_fetch_url' ((), {}) 6.28 sec
```
#### Theading
```
[FetchrTutor] Jasim@T-1000 ~/Devel/FetchrTutor
$ python multi_thread.py
Fibnocci sum of 1 is 1
Fibnocci sum of 2 is 1
Fibnocci sum of 3 is 2
Fibnocci sum of 4 is 3
Fibnocci sum of 5 is 5
Fibnocci sum of 35 is 9227465
Fibnocci sum of 40 is 102334155
'process_calculate' ((), {}) 43.96 sec

Fetched url: http://google.com
Fetched url: http://abc.xyz
Fetched url: http://yahoo.com
Fetched url: http://facebook.com
Fetched url: http://youtube.com
Fetched url: http://msn.com
Fetched url: http://linkedin.com
Fetched url: http://hotmail.com
'process_fetch_url' ((), {}) 7.90 sec

```

### Conclusions
For heavy parallel computations, multiprocessing is clear winner, creating a process is costly. Will consume high amount of memory. While threading is slow, consuming high memory and processing power,  compared to multiprocessing and async model because of GIL.
