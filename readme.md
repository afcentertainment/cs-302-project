# Needleman-Wunsch Algorithm 
## [RESEARCH PAPER LINK](https://github.com/afcentertainment/cs-302-project/blob/main/A%20general%20method%20applicable%20to%20the%20search%20for%20similarities%20in%20the%20amino%20acid%20sequence%20of%20two%20proteins.pdf)
This is a Python implementation of the Needleman-Wunsch algorithm, which is used for global sequence alignment. The algorithm finds the optimal alignment between two sequences, taking into account match scores, mismatch scores, and gap penalties. The code also includes a sequence generator and a function to save test cases for benchmarking.

Usage
Here's how to use the NeedlemanWunsch class and the provided example:

### Example usage:
```python
seq1 = "TREE"
seq2 = "REED"
nw = NeedlemanWunsch(seq1, seq2)
alignment1, alignment2, score = nw.align()
print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
print("Alignment Score:", score)
```


## NeedlemanWunsch Class
The NeedlemanWunsch class provides the core functionality for sequence alignment:

Initialization
To create an instance of the NeedlemanWunsch class, provide the two sequences you want to align and optional match, mismatch, and gap penalty scores:

```python
nw = NeedlemanWunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1)
```

## Alignment
You can align the sequences by calling the align method:

```python
alignment1, alignment2, score = nw.align()
```
The align method returns the aligned sequences and the alignment score.

## Here's an explanation of each function in the NeedlemanWunsch class:

### 
```python
__init__(self, seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1)
```
This is the class constructor, which initializes the NeedlemanWunsch object with the input sequences seq1 and seq2, as well as optional parameters for match score, mismatch score, and gap penalty.

### initialize_matrix(self)
This method initializes the dynamic programming matrix used in the Needleman-Wunsch algorithm. The matrix is a 2D array with dimensions (len(seq1) + 1) x (len(seq2) + 1). It sets the values in the first row and first column based on gap penalties.

### fill_matrix(self, matrix)
This function fills in the dynamic programming matrix based on the alignment scores for the given sequences. It iterates through the matrix, calculating scores for each cell based on match, mismatch, and gap penalties.

### traceback(self, matrix)
The traceback function reconstructs the optimal alignment by backtracking through the filled matrix. Starting from the bottom-right corner of the matrix, it follows the path with the highest alignment score and records the characters for the aligned sequences.


### align(self)
The align method orchestrates the entire sequence alignment process. It calls initialize_matrix to create the dynamic programming matrix, then fill_matrix to populate it, and finally, traceback to find the optimal alignment. It returns the aligned sequences and their alignment score.


## Sequence Generator
The SequenceGenerator class is used to generate random sequences for testing the Needleman-Wunsch algorithm.

Generating Random Sequences
You can generate a random sequence of a specified length using the generate_random_sequence method:

```python
generator = SequenceGenerator(length)
random_seq = generator.generate_random_sequence()
```
## Generating Test Cases
The generate_test_case method generates two random sequences of the given length. You can use it to create test cases for alignment:

```python
seq1, seq2 = generator.generate_test_case()
```
## Benchmarking
The main function in the code performs benchmarking of the Needleman-Wunsch algorithm for different sequence lengths and prints the alignment results along with execution times.

Saving Test Cases
The code includes a function save_test_cases that allows you to save generated test cases to a file. You can use it as follows:

```python
test_cases = [(seq1, seq2), ...]
filename = "test_cases.txt"
save_test_cases(test_cases, filename)
```

## Running the Code
To run the code and benchmark the algorithm, execute the following block in your Python environment:

```python
if __name__ == "__main__":
    main()
```

command: python filename.py

This will test the Needleman-Wunsch algorithm with sequences of different lengths and provide alignment results and execution times.
