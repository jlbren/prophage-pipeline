import os 
import glob
import re 
from collections import defaultdict

outDir = "urinary_bacteria_out2" 
outFile = "contig_stats_"+outDir+".csv"
out = open(outFile, 'w')
out.write("file_name,num_contigs,total_seq_length\n")  
fDirs = os.listdir(outDir)
for f in fDirs:
	numContigs = totLen = 0   
	if f == "all_results":
		continue # move to next f
	path = os.path.join(outDir,f,"*.fa")
	contigFile =glob.glob(path)
	for j in contigFile: #should only do this once but meh
		with open(j,'r') as fastaFile:
			content = fastaFile.read().split('\n')
			
		for c in content: 
			if c!="" and c!='\n':
				if len(re.findall('>',c))!=0: # headers 
					numContigs+=1 
				else:
					totLen += len(c) # sequence 
	out.write("{},{},{}\n".format(f,numContigs,totLen))

out.close()
