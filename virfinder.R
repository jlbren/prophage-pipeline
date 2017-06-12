library(VirFinder)
args <- commandArgs(trailingOnly = TRUE)
inFile<-args[1]
outPath<- args[2] 
##prediction
predResult <- VF.pred(inFile)
##sort by ascending p-val
PredResult<-predResult[order(predResult$pvalue),]
PredResult
##false discovery rate
#predResult$qvalue <- VF.qvalue(predResult$pvalue)
predFile<- paste(outPath, "/","virfinder_predictions", ".csv", sep = "")
write.table(predResult, predFile, sep=",",
		quote = FALSE, col.names=TRUE,row.names=FALSE) 

