# COP4533 Programming Assignment 2 — Cache Eviction Policies

## Overview

This program implements and compares three cache eviction policies on a given request sequence:

- **FIFO** (First-In, First-Out)
- **LRU** (Least Recently Used)
- **OPTFF** (Belady's Farthest-in-Future, optimal offline)

## Project Structure

```
COP4533_Programming_Assignment_2/
├── src/
│   ├── main.py
│   ├── FIFO.py
│   ├── LRU.py
│   └── OPTFF.py
├── input/
│   ├── example.in
│   ├── question_2.in
│   ├── test1.in
│   ├── test2.in
│   └── test3.in
├── output/
│   └── (generated .out files)
├── tests/
├── Written_Responses/
│   ├── Question_1.md
│   └── Question_2.md
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9+
- No external dependencies (uses only standard library: `collections`, `sys`, `os`)

## Input Format

Each `.in` file contains two lines:

```
k m
r1 r2 r3 ... rm
```

Where `k` is the cache capacity, `m` is the number of requests, and `r1` through `rm` are integer request IDs.

## Output Format

Each `.out` file contains:

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## Running the Program

From the project root directory:

```bash
python3 src/main.py input/<filename>.in
```

For example:

```bash
python3 src/main.py input/test1.in
python3 src/main.py input/test2.in
python3 src/main.py input/test3.in
```

Output files will be written to the `output/` directory with the corresponding `.out` extension (e.g., `test1.out`).

## Running All Test Files

```bash
for f in input/*.in; do
    python3 src/main.py ${f}
done
```