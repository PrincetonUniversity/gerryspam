library(ggplot2)
library(tidyverse)
library(skimr)

### 
#  Load data
###
base_path <- file.path("projects", "gerryspam", "MO", "res")
plot_path <- file.path("projects", "gerryspam", "MO", "plots")

raw_baseline = read_csv(file.path(base_path, "stsenate_05_data_update.csv"))
raw_03 = read_csv(file.path(base_path, "stsenate_01_data_update.csv"))

### 
# Data transformations
###
# filter out EG > 0.07, EG < -0.07 for "baseline"
# NB: 186,115/600000 left (~30%)
df_baseline <- raw_baseline %>%
  filter(eg < 0.07) %>%
  filter(eg > -0.07) %>%
  mutate(runtype = "Baseline",
         seat_share = D_seats/34)

df_03 <- raw_03 %>%
  filter(eg < 0.15) %>%
  filter(eg > -0.15) %>%
  mutate(runtype = "Amendment 3",
         seat_share = D_seats/34)

df_baseline_long <- gather(df_baseline, "district", "Dem_Voteshare", 
                           -c("X1", "eg", "election", "total_districts", "epsilon", 
                              "D_seats", "MM", "runtype", "voteshare_mean", "seat_share"))

df_03_long <- gather(df_03, "district", "Dem_Voteshare", 
                      -c("X1", "eg", "election", "total_districts", "epsilon", 
                         "D_seats", "MM", "runtype", "voteshare_mean", "seat_share"))

df_long <- bind_rows(df_baseline_long, df_03_long)

df_short <- bind_rows(df_03, df_baseline)
df_short %>% group_by(election, runtype) %>% skim()

# look at competitiveness range
competitiveness_dist <- function(x, probs) {
  tibble(x = quantile(x, probs), probs = probs)
}

df_long %>% 
  group_by(election, runtype) %>%
  summarize(
    n_total = n(), 
    gr_45 = length(Dem_Voteshare[Dem_Voteshare <= .45]),
    lt_55 = length(Dem_Voteshare[Dem_Voteshare > .55])) %>%
  ungroup() %>%
  mutate(total_competitive = gr_45 + lt_55,
         prop_competitive = total_competitive/n_total)

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

density_PRES <- ggplot(df_long_PRES, aes(x=Dem_Voteshare, color=runtype)) +
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

bars_PRES <- ggplot(df_long_PRES, aes(factor(D_seats), fill=runtype)) +
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

### 
# Plot 4: Seats/votes curve with line of best fit
###

# both presidential and senate
ggplot(df_short, aes(x = voteshare_mean, y = seat_share)) + 
  geom_jitter() +
  geom_smooth(method = lm) + 
  facet_grid(vars(runtype), vars(election), scales = "free")
ggsave(file.path(plot_path, "votes-seats.png"), width=15, height=15)

df_short_SEN <- df_short %>%
  filter(election == "USSEN16")

df_short_PRES <- df_short %>%
  filter(election == "PRES16")

# only senate
ggplot(df_short_SEN, aes(x = voteshare_mean, y = seat_share)) + 
  geom_jitter(alpha=0.05) +
  geom_smooth(method = lm) + 
  facet_grid(cols=vars(runtype)) + 
  scale_y_continuous(labels = scales::percent) + 
  scale_x_continuous(labels = scales::percent) + 
  labs(title="Votes-Seats Curve: Amendment 3 vs. Baseline",
        x ="Vote Share (D)", y = "Seat Share (D)",
       subtitle = "Based on 2016 U.S. Senate election results")
ggsave(file.path(plot_path, "votes-seats_sen.png"), width=15, height=10)

# only presidential
ggplot(df_short_PRES, aes(x = voteshare_mean, y = seat_share)) + 
  geom_jitter(alpha=0.05) +
  geom_smooth(method = lm) + 
  facet_grid(cols=vars(runtype)) + 
  scale_y_continuous(labels = scales::percent) + 
  scale_x_continuous(labels = scales::percent) + 
  labs(title="Votes-Seats Curve: Amendment 3 vs. Baseline",
       x ="Vote Share (D)", y = "Seat Share (D)",
       subtitle = "Based on 2016 Presidential election results")
ggsave(file.path(plot_path, "votes-seats_pres.png"), width=15, height=10)

# by district - only senate
ggplot(df_long_SEN, aes(x = Dem_Voteshare, y = seat_share)) + 
  geom_jitter() +
  geom_smooth(method = lm) + 
  facet_grid(vars(runtype), vars(district), scales = "free")

### 
# LM: Seats/votes curve 
###

# senate data only
model <- lm(seat_share ~ voteshare_mean*runtype, data=df_short_SEN)
summary(model)

amendment_3_slope <- -5.23373
baseline_slope <- -5.23373 + -2.38977 + 5.04077