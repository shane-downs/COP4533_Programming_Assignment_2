# Question 3: Prove OPTFF is Optimal

### Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

### Explanation


invariant: Let S be a reduced schedule that makes the same eviction decisions
as S<sub>FF</sub> through the first j items in the sequence, for a number j. Then there is a
reduced schedule S’ that makes the same eviction decisions as S<sub>FF</sub> through the
first j + 1 items, and incurs no more misses than S does.

Let s be a reduced schedule that is the same as S<sub>FF</sub> through j steps

We produce s' that satisfies invariant after j+1 steps

let d be the item requested on step j+1

Since S and S<sub>FF</sub> have agreed up until now, they have the same cache contents before 
step j+1

Case 1: d is already in the cache
    
    s' = s and satisfies the invariant as d is in both s and s'

Case 2: d is not in the cache but s and S<sub>FF</sub> evict the same element

    s' = s as the same element is removed

Case 3: d is not in the cache; S<sub>FF</sub> evicts e; S evicts f != e

    Construct S' by evicting e instead of f resulting in the following:
    
    S = [same,e,d]
    S' = [same,f,d]

    now Sʹ agrees with SFF for first j + 1 steps; we show that having item f
    in cache is no worse than having item e in cache

    Let Sʹ behave the same as S until Sʹ is forced to take a different action
    (because either S evicts e; or because either e or f is requested)

Case 3a: g != e,f

    g is not in cache S or S'. S will evict e to make room for it and S' 
    will evict f making the caches S and S' similar to each other.

Case 3b: g = f

    Assume S evicts item e'. If e' = e then S evicts e and replaces it with f
    making S and S' similar to each other.

     If e’ != e, then we have S' evict e' as well, and bring in e from main memory; 
    this too results in S and S’ having the same caches. 

    However, since S’ is no longer a reduced schdule, we further transform S’ to its reduced state,
    this doesn’t increase the number of items brought in by S’, and it still agrees with SFF through step j + 1. 

Hence, in both these cases, we have a new reduced schedule S’ that agrees
with S<sub>FF</sub> through the first j + 1 items and incurs no more misses than S does.