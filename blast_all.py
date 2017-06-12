from Bio import SeqIO
import subprocess

seqs = SeqIO.parse('sequence.fasta', 'fasta')
hits = []
for seq in seqs:
    blast_cmd = subprocess.run([
                    'blastn',
                    '-query', 'sequence.fasta',
                    '-db', 'Viral',
                    '-outfmt', '10 stitle length pident bitscore',
                    '-max_target_seqs', '1'
                   ],
                   stdout=subprocess.PIPE)

    hits.append(blast_cmd.stdout.decode('utf-8').strip()) # Clean output and append
print(str(hits[0]))
