import os 
import glob
import re 
from collections import defaultdict

outDir = "urinary_bacteria_out2" 
resDir = "Predicted_viral_sequences"
 
fDirs = os.listdir(outDir)
cats = defaultdict(list)
for f in fDirs: 
	path = os.path.join(outDir,f,resDir,"*.fasta")
	resFiles =glob.glob(path)
	for j in resFiles: 
		with open(j,'r') as fastaFile:
			content = fastaFile.read()
		cat = re.findall(r'\d+',j)[-1]
		if content!="" and content!='\n':
			cats[cat].append(content) 

for i in range(1,7):
	outFile = "virsorter_cat_"+str(i)+".fa"
	out = open(outFile, 'w') 
	for l in cats[str(i)]:
		out.write("%s\n" %l) 
	out.close() 
	
