from Bio import SeqIO
import subprocess
from glob import glob
import os 
# Input dir. Include wildcard to get all files.
in_dir = 'urinary_bacteria_out/all_results/*'
in_files = glob(in_dir)
for f in in_files:
    seqs = SeqIO.parse(f, 'fasta')
    hits = []
    for s in seqs:
        with open('sequence.fasta', 'w') as out:
            out.write('>'+s.id+'\n')
            out.write(str(s.seq))
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
        #print(stderr)
        hit = stdout.decode('UTF8').strip('\n')
        #print('--------------------')
        #print(not hit)
        if hit:
            hits.append(hit)
        else:
            with open('unmapped.fa', 'a+') as unmapped:
                unmapped.write(s.id+'\n')
    outfile = 'blast-'+os.path.basename(f)
    with open(outfile, 'w') as out:
        out.write('qseqid, stitle, length, pident, bitscore\n')
        for hit in hits:
            out.write(hit+'\n')

