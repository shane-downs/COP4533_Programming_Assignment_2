# Question 2: Bad Sequence for LRU or FIFO

### Request Sequence where OPTFF incurs strictly fewer misses than LRU/FIFO

#### Input
`question_2.in`

````
3 12
1 2 3 1 4 5 6 2 7 8 9 3
````

#### Output (miss counts)
`question_2.out`

````
FIFO  : 11
LRU   : 11
OPTFF : 9
````

### Explanation
We start by filling out the caches (k=3) with 3 elements. LRU and FIFO
perform the same as OPTFF until we reach the repeated request for job 2.
At this moment, `LRU = [4, 5, 6]`, `FIFO = [4, 5, 6]`, `OPTFF = [2, 3, 6]`.
OPTFF kept 2 in the cache because it looked ahead and saw that it was requested
again right after job with id 6 (element 6 in input list). LRU and FIFO evicted
2 because it was the least recently used up through job 6 or FIFO evicted 2 by
this point because it was inserted into the cache first compared to 4, 5, 6.
OPTFF will hit on 2 at element 7 (iteration 8) and the other caches will miss.
The same logic applies if we fast-forward 3 iteration steps and come across
job with id 3 once again. OPTFF kept 3 because it looked ahead and saw it came
right after the sequence 7, 8, 9. LRU and FIFO will miss while OPTFF knew 3 was coming
again and kept it in the cache opting to evict 2 because it knows it will
not come up again in the future.