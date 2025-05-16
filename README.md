
# Alanine Scanning Mutagenesis Script

This Python script (`Alanine_Replacement.py`) automates alanine scanning mutagenesis on a given protein sequence. It systematically replaces each amino acid residue in the sequence with alanine (Glycine if naturally occurring Alanine), one at a time, generating a series of mutant sequences from the input. The output is a FASTA file containing all the generated variants, which can be used for downstream analysis or synthesis, such as identifying critical residues for binding or structure.

---

## 🧬 Purpose

Alanine scanning is a common method in structural and functional biology to identify the importance of specific amino acids in a protein. This script facilitates the rapid generation of all possible alanine substitution variants from a given protein input for use with peptide/gene synthesis

---

## 🔧 Usage

```bash
positional arguments:
  input_file            Input protein file in FASTA format

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name for mutated sequences in FASTA format

```

After processing, the script will output a FASTA file in the same directory with the format:

```
<Provided Name>_mutated.fasta
```

Each entry in the FASTA file will represent one substitution, with 3 duplicate entrys for each of the single, double, and triple Alanine replacements.

---

## 🗂 Example

If your input sequence is:
```
>Test
MAKTISVVTLLCVLPAVVYST
```

The output will include entries like:
```
>Test_mut1
AAKTISVVTLLCVLPAVVYST
>Test_mut1_2
AGKTISVVTLLCVLPAVVYST
>Test_mut1_2_3
AGATISVVTLLCVLPAVVYST
>Test_mut2
MGKTISVVTLLCVLPAVVYST
>Test_mut2_3
MGATISVVTLLCVLPAVVYST
>Test_mut2_3_4
MGAAISVVTLLCVLPAVVYST
...
```

Naturally occuring Alanine's are replace with Glycine (G) instead.

Note - this does not factor in any other existing amino acid residues, therefore residues habrouring disulfide bonds (e.g., cystines) will be altered.

---


## ✅ Features

- Alanine (and Cystine) amino acid replacements - single, double, and triple replacement options
- Clean FASTA output with informative headers
- Fast and lightweight — no external dependencies

---

## 📄 License

MIT License

---

## ✍️ Author

Ashley Otter  
[GitHub: @asherichia](https://github.com/asherichia)

---

## 💡 Future Enhancements

- Support batch processing of multiple sequences
