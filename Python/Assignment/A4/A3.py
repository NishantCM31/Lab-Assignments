""" import numpy as np

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
 """

import numpy as np

# Example DNA sequence (A, T, C, G)
dna_sequence = np.array(['A', 'T', 'C', 'G', 'A', 'A', 'A','T', 'G', 'C', 'C', 'A', 'T', 'G'])

# 1. Count frequency of each base (A, T, C, G)
bases, counts = np.unique(dna_sequence, return_counts=True)
base_counts = dict(zip(bases, counts))
print("Base Counts:")
for base, count in base_counts.items():
    print(f"- {base}: {count}")

# 2. Find the most common base
most_common_base = bases[np.argmax(counts)]
print(f"\nMost Common Base: {most_common_base}")

# 3. Find base pair sequences longer than a threshold (e.g., 2)
threshold = 2
# Identify sequences where base stays the same and split based on changes
sequences = []
current_sequence = [dna_sequence[0]]
for i in range(1, len(dna_sequence)):
    if dna_sequence[i] == dna_sequence[i-1]:
        current_sequence.append(dna_sequence[i])
    else:
        if len(current_sequence) > threshold:
            sequences.append(current_sequence)
        current_sequence = [dna_sequence[i]]
if len(current_sequence) > threshold:
    sequences.append(current_sequence)

print(f"\nBase Sequences Longer than {threshold}:")
for seq in sequences:
    print(f"- {''.join(seq)}")

# 4. Reverse the DNA sequence
reversed_dna = np.flip(dna_sequence)
print("\nReversed DNA Sequence:")
print(''.join(reversed_dna))
