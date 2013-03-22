
library(ggplot2)

png('experiment3.png', width=2000, height=1000)

vLines <- c(10.67, 7.825, 6.055)
colors <- c("#F8766D", "#00BA38", "lightcyan3")
ggplot(data = values, aes(x = parameter, y =values$step18000)) + geom_vline(xintercept=vLines, linetype="longdash", size=1, colour=colors) + scale_fill_manual(values=colors, name="Scale") + ggtitle('VYP variation') + scale_x_discrete('VYP (mm)') + scale_y_continuous('Number of agents') + geom_boxplot(aes(fill = scale), width = 0.8) + theme_bw() + theme(axis.title.y = element_text(size = 18)) + theme(axis.title.x = element_text(size = 18)) + theme(plot.title = element_text(size=24)) + theme(legend.title = element_text(size=20)) + theme(legend.text = element_text(size=18))
dev.off()


