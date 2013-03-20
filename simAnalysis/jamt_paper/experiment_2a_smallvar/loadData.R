
local <- read.csv('experiment2a_1local.csv', sep=';')
regional <- read.csv('experiment2a_2regional.csv', sep=';')
global <- read.csv('experiment2a_3global.csv', sep=';')

endLocal = local[,c(1,52)]
endRegional <- regional[,c(1,52)]
endGlobal <- global[,c(1,52)]

localParameter <- factor(endLocal$var)
regionalParameter <- factor(endRegional$var)
globalParameter <- factor(endGlobal$var)

