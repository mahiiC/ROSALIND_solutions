"""
Problem 2: Bioinformatics Stronghold
Transcribing DNA into RNA 
Rosalind ID: RNA
Rosalind URL: https://rosalind.info/problems/rna/

"""
def transcribe(dna):
  rna = dna.replace('T', 'U')
  return rna

if __name__ == '__main__':
  with open('rosalind_rna.txt', 'r') as s:
    dna = s.read()
    rna = transcribe(dna)
    print(rna)
