library(ggplot2)

### 
#  Load data
###
set.seed(1234)
df <- data.frame(
  sex=factor(rep(c("F", "M"), each=200)),
  weight=round(c(rnorm(200, mean=55, sd=5),
                 rnorm(200, mean=65, sd=5)))
)
head(df)

### 
# Data transformations
###


### 
# Plot 1: Density of vote share
###
# Change density plot line colors by groups
ggplot(df, aes(x=weight, color=sex)) +
  geom_density()

### 
# Plot 2: Side-by-side bar chart of seat share
###


### 
# Plot 3: Mean-median score
###

