library(ggplot2)

png('experiment2b.png', width=2000, height=1000)

breaksX <- factor(c(1791,2584,4791,5584,7791,8140,8584,11140,14140))
# historic 10ka: 4955 (KS), 5775 (NWI), 11521 (wI)
vLines <- c(12.56,15.92,33.76)
colors <- c("#F8766D", "#00BA38", "lightcyan3")

ggplot(data = values, aes(x = parameter, y =values$step18000)) + geom_vline(xintercept=vLines, linetype="longdash", size=1, colour=colors) + scale_fill_manual(values=colors, name="Scale") + ggtitle('AYP variation') + scale_x_discrete('AYP (mm)', breaks=breaksX) + scale_y_continuous('Number of agents') + geom_boxplot(aes(fill = scale), width = 0.8) + theme_bw() + theme(axis.title.y = element_text(size = 18)) + theme(axis.title.x = element_text(size = 18)) + theme(plot.title = element_text(size=24)) + theme(legend.title = element_text(size=20)) + theme(legend.text = element_text(size=18))

dev.off()

