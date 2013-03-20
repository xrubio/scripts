
png('experiment1.png', width=1500, height=3000)
par(mfrow=c(3,1), mar=c(7,7,7,7)) 
source('generatePlotsLocal.R')
source('generatePlotsRegional.R')
source('generatePlotsGlobal.R')

dev.off()

