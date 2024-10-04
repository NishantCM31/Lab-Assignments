import numpy as np

# Example DNA sequence (A, T, C, G)
dna_sequence = np.array(['A', 'T', 'C', 'G', 'A', 'A', 'T', 'G', 'C', 'C', 'A', 'T', 'G'])

# 1. Count frequency of each base (A, T, C, G)
bases, counts = np.unique(dna_sequence, return_counts=True)
print("Base counts:", dict(zip(bases, counts)))

# 2. Find the most common base
most_common_base = bases[np.argmax(counts)]
print("Most common base:", most_common_base)

# 3. Find base pair sequences longer than a threshold (e.g., 2)
threshold = 2
sequences = [sequence for sequence in np.split(dna_sequence, np.where(np.diff(dna_sequence) != 0)[0] + 1) if len(sequence) > threshold]
print("Long base sequences:", sequences)

# 4. Reverse the DNA sequence
reversed_dna = np.flip(dna_sequence)
print("Reversed DNA sequence:", reversed_dna)
