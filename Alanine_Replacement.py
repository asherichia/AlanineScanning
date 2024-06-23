from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse

def mutate_protein(input_file, output_file):
    records = list(SeqIO.parse(input_file, "fasta"))
    mutated_records = []

    for record in records:
        sequence = record.seq
        for i in range(len(sequence)):
            original_aa = sequence[i]
            if original_aa == 'A':
                mutated_aa = 'G'  # Change Alanines to Glycines
            else:
                mutated_aa = 'A'  # Change all other amino acids to Alanine

            # Single mutation at current position
            mutated_sequence_single = sequence[:i] + Seq(mutated_aa) + sequence[i+1:]
            mutated_record_single = SeqRecord(mutated_sequence_single, id=f"{record.id}_mut{i+1}", description="")
            mutated_records.append(mutated_record_single)

            # Double mutation at current position and next position
            if i + 1 < len(sequence):
                next_aa = sequence[i+1]
                if next_aa == 'A':
                    next_mutated_aa = 'G'  # Change Alanines to Glycines
                else:
                    next_mutated_aa = 'A'  # Change all other amino acids to Alanine

                mutated_sequence_double = sequence[:i] + Seq(mutated_aa) + Seq(next_mutated_aa) + sequence[i+2:]
                mutated_record_double = SeqRecord(mutated_sequence_double, id=f"{record.id}_mut{i+1}_{i+2}", description="")
                mutated_records.append(mutated_record_double)

                # Triple mutation at current, next, and next-next position
                if i + 2 < len(sequence):
                    next_next_aa = sequence[i+2]
                    if next_next_aa == 'A':
                        next_next_mutated_aa = 'G'  # Change Alanines to Glycines
                    else:
                        next_next_mutated_aa = 'A'  # Change all other amino acids to Alanine

                    mutated_sequence_triple = sequence[:i] + Seq(mutated_aa) + Seq(next_mutated_aa) + Seq(next_next_mutated_aa) + sequence[i+3:]
                    mutated_record_triple = SeqRecord(mutated_sequence_triple, id=f"{record.id}_mut{i+1}_{i+2}_{i+3}", description="")
                    mutated_records.append(mutated_record_triple)

    return mutated_records

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mutate protein sequence.')
    parser.add_argument('input_file', help='Input protein file in FASTA format')
    parser.add_argument('-o', '--output', help='Output file name for mutated sequences in FASTA format')
    args = parser.parse_args()

    if args.output:
        output_file = args.output
    else:
        output_file = "output_mutated.fasta"

    mutated_records = mutate_protein(args.input_file, output_file)

    with open(output_file, "w") as output_handle:
        SeqIO.write(mutated_records, output_handle, "fasta")
