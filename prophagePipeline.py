from os import listdir, makedirs, rename, system 
from os.path import join, exists   
import subprocess as sub 

#Launch this script in sudo so it wont ask again when it reaches the docker command each time!!! 
#specify path to input and output dirs (relative or absolute) *NOTE ~/ for the path to home dir does not seem to work 
inPath = '../urinary_bacteria2/sanger_contigs'
outPath = 'urinary_bacteria_out2' 

inFiles = listdir(inPath) 
if not exists(outPath):
	makedirs(outPath) 
for f in inFiles:
	print "# Processing " + f + "..."   
	#turn . in filename to _ and combine w output dir path 
	fDir = join(outPath, f.replace('.', '_'))  
	makedirs(fDir)
	#move input file to new output dir 
	rename(join(inPath, f) , join(fDir, f))
 	fPath = join(fDir, f)
	print "# Starting virfinder..."  
	p = sub.Popen(['Rscript', 'virfinder.R', fPath, fDir],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	print errors 
	print output
	print "# Starting virsorter..."  
	#*NOTE subprocess.Popen doesnt work as it requires pswd for sudo each time
	vsCommand =("sudo docker run "
				    "-v ~/prophagePipeline/virsorter-data:/data "   
				    "-v ~/prophagePipeline/"+fDir+":/wdir "
				    "-w /wdir " 
				    "--rm discoenv/virsorter:v1.0.3 "  
				    "--db 2 " 
				    "--fna /wdir/" + f ) 
	system(vsCommand) 
	print "# Results in " + fDir 
#sudo docker run -v ~/virsorter-master/virsorter-data:/data -v ~/virsorter-master/3:/wdir -w /wdir --rm discoenv/virsorter:v1.0.3 --db 2 --fna /wdir/16933_8#30.contigs_velvet.fa
print "Done" , len(inFiles) , "files analyzed. " 



