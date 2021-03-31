library(dplyr)
library(ggplot2)
library(tidyverse)
library(GGally)

federal <- read_csv("~/declaranet/data/states/r_fed.csv")
state <- read_csv("~/declaranet/data/states/r_state.csv")
mun <- read_csv("~/declaranet/data/states/r_mun.csv")

some_cols <- c("file_size",
               "prop_window",
               "contract_duration",
               "daily_price",
               "person",
               "amount",
               "buyer_dispersion",
               "supplier_dispersion",
               "single_bid",
               "atom",
               "single_interaction",
               "interaction",
               "s_interaction",
               "e_exp_r",
               "very_high_r",
               "c_very_high_r")

new_cols <- c("FileSize",
              "PropWin.",
              "Duration",
              "DailyPrice",
              "Hsupplier",
              "Amount",
              "BuyerDisp.",
              "SupplierDisp.",
              "SingleBid",
              "Atom.",
              "SSingleInt.",
              "BMeanCnts.",
              "SMeanCnts.",
              "ExpCorruption",
              "CorruptionPub.",
              "CorruptionPri.")

federal %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.6, size = 2, color = "grey50") +
  labs(title="Federal Contracts") +
  ggsave('declaranet/')

state %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.6, size = 2, color = "grey50") +
  labs(title="State Contracts")

mun %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.60, size = 2, color = "grey50") +
  labs(title="Municipal Contracts")
