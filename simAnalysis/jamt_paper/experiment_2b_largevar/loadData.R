
local <- read.csv('experiment2b_1local.csv', sep=';')
regional <- read.csv('experiment2b_2regional.csv', sep=';')
global <- read.csv('experiment2b_3global.csv', sep=';')

endLocal = local[,c(1,52)]
endLocal[c("scale")] <- "K-S"
endRegional <- regional[,c(1,52)]
endRegional[c("scale")] <- "NWI"
endGlobal <- global[,c(1,52)]
endGlobal[c("scale")] <- "wI"

values <- merge(x=endLocal, y=endRegional, all=TRUE)
values <- merge(x=values, y=endGlobal, all=TRUE)
parameter <- factor(values$var)
scales <- factor(values$scale)
parameter2 <- as.numeric(as.character(values$var))
