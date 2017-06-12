from Bio import SeqIO
import subprocess
from glob import glob
# Input dir. Include wildcard to get all files.
in_dir = 'urinary_bacteria_out/all_results/*'
in_files = glob(in_dir)
for f in in_files:
    seqs = SeqIO.parse('sequence.fasta', 'fasta')
    hits = []
    for seq in seqs:
        blast_cmd = subprocess.Popen([
            'blastn',
            '-query', 
            'sequence.fasta',
            '-db', 'Viral',
            '-outfmt', '10 qseqid stitle length pident bitscore',
            '-max_target_seqs', '1'
	    ],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = blast_cmd.communicate()
	# Clean output and append to results list.
        hits.append(stdout)
        with open('blast-'+'/'.strip(f)[-1]) as out:
            out.write('qseqid, stitle,, length, pident, bitscore\n')
            for hit in hits:
                out.write(hit+'\n')


