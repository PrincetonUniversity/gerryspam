library(ggplot2)
library(tidyverse)

### 
#  Load data
###
base_path <- file.path("projects", "gerryspam", "MO", "res")

raw_baseline = read_csv(file.path(base_path, "sthouse_05_data.csv"))
raw_03 = read_csv(file.path(base_path, "sthouse_03_data.csv"))

### 
# Data transformations
###
# filter out EG > 0.07, EG < -0.07 for "baseline"
df_baseline <- raw_baseline %>%
  filter(eg < 0.07) %>%
  filter(eg > -0.07) %>%
  mutate(runtype = "Baseline")

df_03 <- raw_03 %>%
  mutate(runtype = "Amendment 3")

df_baseline_long <- gather(df_baseline, "district", "Dem_Voteshare", 
                           -c("X1", "eg", "election", "total_districts", "epsilon", "D_seats", "MM", "runtype"))


df_03_long <- gather(df_03, "district", "Dem_Voteshare", 
                      -c("X1", "eg", "election", "total_districts", "epsilon", "D_seats", "MM", "runtype"))

df_long <- bind_rows(df_baseline_long, df_03_long)

# create election-specific DFs for plotting
df_long_PRES <- df_long %>%
  filter(election == "PRES16")

df_long_SEN <- df_long %>%
  filter(election == "USSEN16")

### 
# Plotting
###

### 
# Plot 1: Density of vote share
###

density_PRES <- ggplot(df_long_PRES, aes(x=Dem_Voteshare, color=runtype)) +
  geom_density()
density_PRES 

density_SEN <- ggplot(df_long_SEN, aes(x=Dem_Voteshare, color=runtype)) +
  geom_density()
density_SEN

### 
# Plot 2: Side-by-side bar chart of seat share
###
test_df <- sample_n(df_long_PRES, size=5000)

ggplot(test_df, aes(factor(D_seats), fill=runtype)) +
  geom_bar(position="dodge")


bars_PRES <- ggplot(df_long_PRES, aes(factor(D_seats), fill=runtype)) +
  geom_bar(position="dodge")
bars_PRES

bars_SEN <- ggplot(df_long_SEN, aes(x=factor(D_seats), fill=runtype)) +
  geom_bar(position="dodge")
bars_SEN

### 
# Plot 3: Mean-median score
###

MM_density_PRES <- ggplot(df_long_PRES, aes(x=MM, color=runtype)) +
  geom_density()
MM_density_PRES 

MM_density_SEN <- ggplot(df_long_SEN, aes(x=MM, color=runtype)) +
  geom_density()
MM_density_SEN

