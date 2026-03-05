# Question 1: Empirical Comparison

| Input File | k | m  | FIFO | LRU | OPTFF |
|------------|---|----|------|-----|-------|
| test1.in   | 3 | 60 | 40   | 38  | 28    |
| test2.in   | 4 | 75 | 54   | 55  | 34    |
| test3.in   | 5 | 80 | 66   | 65  | 45    |

*see `/output` dir for results

### Comments
* OPTFF has the fewest misses for each input file. This is because
OPTFF is optimal in that it reads the input ahead to see which requests
are least needed in the future. LRU and FIFO do not perform any lookahead
operations which results in greater misses due to a lack of knowledge about
the future.



* FIFO and LRU have very similar miss counts when `m >= 50`. In test1,
LRU outperformed FIFO with 38 misses opposed to 40 misses. However,
test2 shows that FIFO outperformed LRU with 54 vs 55 misses. Overall,
both algorithms show similar miss results.