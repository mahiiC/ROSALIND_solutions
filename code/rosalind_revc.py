"""
Problem 3: Bioinformatics Stronghold
Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind URL: https://rosalind.info/problems/revc/

"""
def revc(dna):
  rev_dna = dna[::-1]
  revc_dna = rev_dna.replace('A', 't')
  revc_dna = revc_dna.replace('T', 'a')
  revc_dna = revc_dna.replace('C', 'g')
  revc_dna = revc_dna.replace('G', 'c')
  rev_dna = revc_dna.upper()
  return rev_dna

if __name__ == '__main__':
  with open('rosalind_revc.txt', 'r') as s:
    dna = s.read()
    revc_dna = revc(dna)
    print(revc_dna)
