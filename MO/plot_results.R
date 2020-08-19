library(ggplot2)
library(tidyverse)
library(skimr)

### 
#  Load data
###
base_path <- file.path("projects", "gerryspam", "MO", "res")
plot_path <- file.path("projects", "gerryspam", "MO", "plots")

raw_baseline = read_csv(file.path(base_path, "stsenate_05_data.csv"))
raw_03 = read_csv(file.path(base_path, "stsenate_01_data.csv"))

### 
# Data transformations
###
# filter out EG > 0.07, EG < -0.07 for "baseline"
# NB: 186,115/600000 left (~30%)
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
# Tables
###
group_counts <- df_long %>% group_by(election, runtype) %>% summarize(n())
group_counts

df_long_PRES_sampling = sample_n(subset(df_long_PRES, df_long_PRES$runtype=="Baseline"), 3400000)
df_long_PRES_Amendment <- df_long_PRES %>% filter(runtype == "Amendment 3")
df_long_PRES_sampled <- bind_rows(df_long_PRES_sampling, df_long_PRES_Amendment)

summary_table <- df_long %>% group_by(election, runtype) %>% skim(eg, MM, D_seats, Dem_Voteshare)
small_table <- df_long %>% group_by(election, runtype) %>% skim(eg, MM, D_seats, Dem_Voteshare) %>% focus(election, runtype, numeric.mean, numeric.sd, numeric.hist)
knitr::kable(small_table)

### 
# Plotting
###

### 
# Plot 1: Density of vote share
###

density_PRES <- ggplot(df_long_PRES aes(x=Dem_Voteshare, color=runtype)) +
  geom_density()
density_PRES 
ggsave(file.path(plot_path, "voteshare_dens_pres.png"), density_PRES, width=10)

density_SEN <- ggplot(df_long_SEN, aes(x=Dem_Voteshare, y=..scaled.., color=runtype)) +
  geom_density()
density_SEN
ggsave(file.path(plot_path, "voteshare_dens_sen.png"), density_SEN, width=10)


### 
# Plot 2: Side-by-side bar chart of seat share
###

bars_PRES <- ggplot(df_long_PRES_sampled, aes(factor(D_seats), fill=runtype)) +
  geom_bar(position="dodge")
bars_PRES
ggsave(file.path(plot_path, "seatshare_bars_pres.png"), bars_PRES, width=8)

bars_SEN <- ggplot(df_long_SEN, aes(x=factor(D_seats), fill=runtype)) +
  geom_bar(position="dodge")
bars_SEN
ggsave(file.path(plot_path, "seatshare_bars_sen.png"), bars_SEN, width=8)

# Same but density plot
seats_density_PRES <- ggplot(df_long_PRES, aes(x=D_seats, color=runtype)) +
  geom_density()
seats_density_PRES 
ggsave(file.path(plot_path, "meanmedian_dens_pres.png"), MM_density_PRES, width=8)



### 
# Plot 3: Mean-median score
###

MM_density_PRES <- ggplot(df_long_PRES, aes(x=MM, color=runtype)) +
  geom_density()
MM_density_PRES 
ggsave(file.path(plot_path, "meanmedian_dens_pres.png"), MM_density_PRES, width=8)


MM_density_SEN <- ggplot(df_long_SEN, aes(x=MM, color=runtype)) +
  geom_density()
MM_density_SEN
ggsave(file.path(plot_path, "meanmedian_dens_sen.png"), MM_density_SEN, width=8)


