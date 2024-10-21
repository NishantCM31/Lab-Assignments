import numpy as np

# Function to count the frequency of each base
def count_bases(dna_sequence):
    unique, counts = np.unique(dna_sequence, return_counts=True)
    # Convert NumPy data types to standard Python types
    return {str(base): int(count) for base, count in zip(unique, counts)}

# Function to find the most common base
def most_common_base(dna_sequence):
    base_counts = count_bases(dna_sequence)
    return max(base_counts, key=base_counts.get)

# Function to find base pair sequences longer than a specified threshold
def find_long_sequences(dna_sequence, threshold):
    current_seq = ''
    sequences = []
    for base in dna_sequence:
        if current_seq and base == current_seq[-1]:
            current_seq += base
        else:
            if len(current_seq) > threshold:
                sequences.append(current_seq)
            current_seq = base
    if len(current_seq) > threshold:  # Add the last sequence if it exceeds the threshold
        sequences.append(current_seq)
    return sequences

# Function to reverse the DNA sequence
def reverse_sequence(dna_sequence):
    return dna_sequence[::-1]

# Function to validate the DNA sequence input
def is_valid_dna_sequence(dna_sequence):
    valid_bases = {'A', 'T', 'C', 'G'}
    return all(base in valid_bases for base in dna_sequence)

# Menu-driven program
def genomic_data_menu():
    while True:
        dna_sequence_input = input("Enter the DNA sequence (A, T, C, G): ").upper()
        if is_valid_dna_sequence(dna_sequence_input):
            dna_sequence = np.array(list(dna_sequence_input))
            break
        else:
            print("Invalid sequence. Please enter only A, T, C, G.")

    while True:
        print("\nMenu:")
        print("1. Count the frequency of each base (A, T, C, G)")
        print("2. Find the most common base")
        print("3. Find base pair sequences longer than a specified threshold")
        print("4. Reverse the entire DNA sequence")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            frequencies = count_bases(dna_sequence)
            print("Base frequencies:", frequencies)
        elif choice == 2:
            common_base = most_common_base(dna_sequence)
            print("Most common base:", common_base)
        elif choice == 3:
            threshold = int(input("Enter the sequence length threshold: "))
            long_sequences = find_long_sequences(dna_sequence, threshold)
            print("Sequences longer than", threshold, "bases:", long_sequences)
        elif choice == 4:
            reversed_sequence = reverse_sequence(dna_sequence)
            print("Reversed DNA sequence:", ''.join(reversed_sequence))
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
genomic_data_menu()