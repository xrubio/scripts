library(ggplot2)
library(gridExtra)

png('experiment2a.png', width=1500, height=3000)

breaksLocal <- factor(c(4682,4782,4957))
labelsLocal <- c('0 ka', '4 ka', '10 ka')
AYP_KS <- endLocal$var
localPlot <- ggplot(data = endLocal, aes(x = localParameter, y =endLocal$step18000)) + ggtitle('AYP variation - KS') + scale_x_discrete('k years before present', breaks=breaksLocal, labels=labelsLocal) + scale_y_continuous('Number of agents') + geom_boxplot(aes(fill=AYP_KS)) + geom_jitter() + theme_bw() + scale_fill_continuous(name="AYP (mm)", guide = guide_legend(reverse=TRUE)) + theme(axis.title.y = element_text(size = 18)) + theme(axis.title.x = element_text(size = 18)) + theme(plot.title = element_text(size=24)) + theme(legend.title = element_text(size=20)) + theme(legend.text = element_text(size=18))

breaksRegional <- factor(c(5457,5577,5787))
labelsRegional <- c('0 ka', '4 ka', '10 ka')
AYP_NWI <- endRegional$var
regionalPlot <- ggplot(data = endRegional, aes(x = regionalParameter, y =endRegional$step18000)) + ggtitle('AYP variation - NWI') + scale_x_discrete('k years before present', breaks=breaksRegional, labels=labelsRegional) + scale_y_continuous('Number of agents') + geom_boxplot(aes(fill=AYP_NWI)) + geom_jitter() + theme_bw() + scale_fill_continuous(name="AYP (mm)", guide = guide_legend(reverse=TRUE)) + theme(axis.title.y = element_text(size = 18)) + theme(axis.title.x = element_text(size = 18)) + theme(plot.title = element_text(size=24)) + theme(legend.title = element_text(size=20)) + theme(legend.text = element_text(size=18))

breaksGlobal <- factor(c(10886,11126,11546))
labelsGlobal <- c('0 ka', '4 ka', '10 ka')
AYP_wI <- endGlobal$var
globalPlot <- ggplot(data = endGlobal, aes(x = globalParameter, y =endGlobal$step18000)) + ggtitle('AYP variation - wI') + scale_x_discrete('k years before present', breaks=breaksGlobal, labels=labelsGlobal) + scale_y_continuous('Number of agents') + geom_boxplot(aes(fill=AYP_wI)) + geom_jitter() + theme_bw() + scale_fill_continuous(name="AYP (mm)", guide = guide_legend(reverse=TRUE)) + theme(axis.title.y = element_text(size = 18)) + theme(axis.title.x = element_text(size = 18)) + theme(plot.title = element_text(size=24)) + theme(legend.title = element_text(size=20)) + theme(legend.text = element_text(size=18))

grid.arrange(localPlot, regionalPlot, globalPlot, nrow=3)
dev.off()

