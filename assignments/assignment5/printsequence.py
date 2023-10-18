#!/usr/bin/env python

import numpy as np
import random
import sys
import argparse

# Load the PFM matrix from a file
def load_pfm(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Skip any comment lines starting with '#' and parse the matrix data
    pfm_data = []
    for line in lines:
        if not line.startswith('>'):
            row = list(map(float, line.strip().split()))
            pfm_data.append(row)

    return np.array(pfm_data).transpose()

# Generate a random sequence based on the PFM
def generate_sequence_from_pfm(pfm_matrix):
    sequence = ""
    for position in pfm_matrix:
        total_probability = sum(position)
        random_value = random.uniform(0, total_probability)
        cumulative_probability = 0

        #print(f"total_probability: {total_probability} | random_value: {random_value}")

        for i, probability in enumerate(position):
            cumulative_probability += probability
            if random_value <= cumulative_probability:
                sequence += "ACGT"[i]
                break

    return sequence

# Main function to generate sequences
def main():
    parser = argparse.ArgumentParser(description="Generate sequences based on a PFM.")
    parser.add_argument("pfm_file", help="Path to the PFM file")
    parser.add_argument("num_sequences", type=int, help="Number of sequences to generate")
    parser.add_argument("label", help="Label for the sequences")
    parser.add_argument("-verbose", default=False, action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    pfm_file = args.pfm_file
    num_sequences = args.num_sequences
    label = args.label
    verbose = args.verbose

    motif_pfm = load_pfm(pfm_file)

    if (verbose):
        print(motif_pfm)

    sequences = []

    for i in range(num_sequences):
        sequence = generate_sequence_from_pfm(motif_pfm)
        print(f"{sequence}\t{label}")


if __name__ == "__main__":
    main()

