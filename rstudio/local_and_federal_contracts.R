# This script is made to compare local and federal networks at a
# statistical level.


library(dplyr)
library(ggplot2)
library(tidyverse)
library(GGally)

local <- read_csv("~/declaranet/data/states/local.csv")
federal <- read_csv("~/declaranet/data/states/federal.csv")



some_cols <- c("file_size",
               "contract_duration",
               "daily_price",
               "same_state",
             "person",
             "amount",
             "variation",
             "variation_s",
             "single_bid",
             "e_exp_r",
             "very_high_r",
             "c_very_high_r")

new_cols <- c("FSz",
              "Dur",
              "DPr",
              "SSt",
              "HSp",
              "Amnt",
              "VBy",
              "VSp",
              "SBd",
              "CE",
              "CP",
              "CPC")



federal %>%
  select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
 ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
        geom="circle", hjust = 0.50, size = 3, color = "grey50") +
  labs(title="Federal level")


federal %>%
  ggplot(aes(variation, very_high_r)) +
  geom_point() +
  geom_smooth(method="lm") +
  labs(x="Buyer Variability", y="CP", title="Federal level") +
  geom_text(aes(label=code),hjust=0, vjust=0, alpha=.6, size=3)


local %>%
  ggplot(aes(variation_s, very_high_r)) +
  geom_point() +
  geom_smooth(method="lm") +
  labs(x="Supplier Variability", y="CP", title="Local level") +
  geom_text(aes(label=code),hjust=0, vjust=0, alpha=.6, size=3)

local %>%
  select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.50, size = 3, color = "grey50") +
  labs(title="Local level")

