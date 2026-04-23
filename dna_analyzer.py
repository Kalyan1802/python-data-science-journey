# =========================================
# Project: DNA Analyzer
# Description: Full bioinformatics tool with translation
# =========================================

VALID_BASES = set("ATGC")

# ---------- FULL CODON TABLE ----------
codon_table = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",

    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",

    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",

    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

# ---------- HELPERS ----------
def validate_dna(seq):
    return len(seq) > 0 and all(base in VALID_BASES for base in seq)

def get_dna_input():
    while True:
        seq = input("Enter DNA sequence (A/T/G/C only): ").strip().upper()
        if validate_dna(seq):
            return seq
        print("❌ Invalid DNA. Use only A, T, G, C.\n")

# ---------- FUNCTIONS ----------
def get_length(seq):
    return len(seq)

def reverse_complement(seq):
    comp_map = {"A":"T","T":"A","G":"C","C":"G"}
    return "".join(comp_map[b] for b in seq)[::-1]

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def codons(seq):
    return [seq[i:i+3] for i in range(0, len(seq), 3) if len(seq[i:i+3]) == 3]

def motif_positions(seq, motif):
    motif = motif.upper()
    return [i for i in range(len(seq) - len(motif) + 1) if seq[i:i+len(motif)] == motif]

def transcribe_to_rna(seq):
    return seq.replace("T", "U")

def translate_dna(seq):
    protein = ""
    for codon in codons(seq):
        amino = codon_table.get(codon, "X")
        if amino == "*":   # STOP codon
            break
        protein += amino
    return protein

def base_frequencies(seq):
    return {b: seq.count(b) for b in "ATGC"}

# ---------- MENU ----------
def show_menu():
    print("\n====== DNA ANALYZER v3 ======")
    print("1. Length")
    print("2. Reverse Complement")
    print("3. GC Content")
    print("4. Codons")
    print("5. Motif Search")
    print("6. RNA Transcription")
    print("7. Protein Translation (Full Table)")
    print("8. Base Frequencies")
    print("9. Exit")

# ---------- MAIN ----------
def main():
    dna = get_dna_input()

    while True:
        show_menu()

        choice = input("Choose option (1-9 or name): ").strip().lower()

        if not choice:
            print("⚠️ Enter a valid option")
            continue

        if choice in ["1", "length"]:
            print("Length:", get_length(dna))

        elif choice in ["2", "reverse"]:
            print("Reverse Complement:", reverse_complement(dna))

        elif choice in ["3", "gc"]:
            print(f"GC Content: {gc_content(dna):.2f}%")

        elif choice in ["4", "codons"]:
            print("Codons:")
            for c in codons(dna):
                print(c)

        elif choice in ["5", "motif"]:
            motif = input("Enter motif: ").upper()
            pos = motif_positions(dna, motif)
            print("Positions:", pos if pos else "Not found")

        elif choice in ["6", "rna"]:
            print("RNA:", transcribe_to_rna(dna))

        elif choice in ["7", "protein"]:
            print("Protein:", translate_dna(dna))

        elif choice in ["8", "freq"]:
            print("Frequencies:", base_frequencies(dna))

        elif choice in ["9", "exit"]:
            print("Exiting... 👋")
            break

        else:
            print("❌ Invalid choice")

# ---------- RUN ----------
if __name__ == "__main__":
    main()