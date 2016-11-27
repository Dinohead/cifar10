library(gdata)
setwd("C:/Users/derek/Desktop")
results <- read.csv("results")
results$id <- as.numeric(results$id)

results$num = 0
results$num[results$class == " airplane"] <- 1
results$num[results$class == " automobile"] <- 2
results$num[results$class == " bird"] <- 3
results$num[results$class == " cat"] <- 4
results$num[results$class == " deer"] <- 5
results$num[results$class == " dog"] <- 6
results$num[results$class == " frog"] <- 7
results$num[results$class == " horse"] <- 8
results$num[results$class == " ship"] <- 9
results$num[results$class == " truck"] <- 10

results$class <- results$num
results$num = NULL

write.table(results, file = 'results.csv', row.names = FALSE, col.names = TRUE, sep = ",")
