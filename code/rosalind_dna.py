"""
Problem 1: Bioinformatics Stronghold
Counting the number of each nucleotide present in a DNA sequence
Rosalind ID: DNA
Rosalind URL: http://rosalind.info/problems/dna/

"""
def count_nt(dna):
  count_A = dna.count('A')
  count_C = dna.count('C')
  count_G = dna.count('G')
  count_T = dna.count('T')
  return count_A, count_C, count_G, count_T

if __name__ == '__main__':
  with open('rosalind_dna.txt', 'r') as s:
    dna = s.readline().strip()
    count_A, count_C, count_G, count_T = count_nt(dna)
    print(count_A, count_C, count_G, count_T)
