class NeedlemanWunsch:
    def __init__(self, seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match_score = match_score
        self.mismatch_score = mismatch_score
        self.gap_penalty = gap_penalty

    def initialize_matrix(self):
        rows, cols = len(self.seq1) + 1, len(self.seq2) + 1
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            matrix[i][0] = i * self.gap_penalty
        for j in range(cols):
            matrix[0][j] = j * self.gap_penalty
        return matrix

    def fill_matrix(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if self.seq1[i - 1] == self.seq2[j - 1]:
                    match = matrix[i - 1][j - 1] + self.match_score
                else:
                    match = matrix[i - 1][j - 1] + self.mismatch_score

                gap1 = matrix[i - 1][j] + self.gap_penalty
                gap2 = matrix[i][j - 1] + self.gap_penalty

                matrix[i][j] = max(match, gap1, gap2)

    def traceback(self, matrix):
        alignment1, alignment2 = [], []
        i, j = len(self.seq1), len(self.seq2)

        while i > 0 and j > 0:
            current_score = matrix[i][j]
            diagonal_score = matrix[i - 1][j - 1]
            left_score = matrix[i][j - 1]
            up_score = matrix[i - 1][j]

            if current_score == diagonal_score + (self.match_score if self.seq1[i - 1] == self.seq2[j - 1] else self.mismatch_score):
                alignment1.append(self.seq1[i - 1])
                alignment2.append(self.seq2[j - 1])
                i -= 1
                j -= 1
            elif current_score == up_score + self.gap_penalty:
                alignment1.append(self.seq1[i - 1])
                alignment2.append('-')
                i -= 1
            else:
                alignment1.append('-')
                alignment2.append(self.seq2[j - 1])
                j -= 1

        while i > 0:
            alignment1.append(self.seq1[i - 1])
            alignment2.append('-')
            i -= 1

        while j > 0:
            alignment1.append('-')
            alignment2.append(self.seq2[j - 1])
            j -= 1

        alignment1.reverse()
        alignment2.reverse()

        return ''.join(alignment1), ''.join(alignment2)

    def align(self):
        matrix = self.initialize_matrix()
        self.fill_matrix(matrix)
        alignment1, alignment2 = self.traceback(matrix)
        return alignment1, alignment2, matrix[-1][-1]

# Example usage:
seq1 = "TREE"
seq2 = "REED"
nw = NeedlemanWunsch(seq1, seq2)
alignment1, alignment2, score = nw.align()
print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
print("Alignment Score:", score)


import random
import time

class SequenceGenerator:
    def __init__(self, length):
        self.length = length

    def generate_random_sequence(self):
        # Generate a random sequence of letters (A, C, G, T) of the specified length.
        return ''.join(random.choice("ACGT") for _ in range(self.length))

    def generate_test_case(self):
        # Generate two random sequences of the given length.
        seq1 = self.generate_random_sequence()
        seq2 = self.generate_random_sequence()
        return seq1, seq2

def save_test_cases(test_cases, filename):
    with open(filename, 'w') as file:
        for seq1, seq2 in test_cases:
            file.write(f"{seq1}\n{seq2}\n")

def main():
    test_case_lengths = [10, 50, 100, 500, 1000, 5000, 10000, 50000,100000]  # Specify different sequence lengths, including 10000
    match_score = 1
    mismatch_score = -2
    gap_penalty = -4

    for length in test_case_lengths:
        generator = SequenceGenerator(length)
        seq1, seq2 = generator.generate_test_case()
        # Measure execution time
        start_time = time.time()
        nw = NeedlemanWunsch(seq1, seq2, match_score, mismatch_score, gap_penalty)
        alignment1, alignment2, score = nw.align()
        end_time = time.time()

        execution_time = end_time - start_time

        print(f"Sequence Length: {length}")
        print("Sequence 1:", alignment1)
        print("Sequence 2:", alignment2)
        print("Alignment Score:", score)
        print(f"Execution Time: {execution_time} seconds")
        print("-" * 50)

if __name__ == "__main__":
    main()

