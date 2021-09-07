library(dplyr)
library(ggplot2)
library(tidyverse)
library(GGally)

federal <- read_csv("~/declaranet/data/states/r_fed.csv")
state <- read_csv("~/declaranet/data/states/r_state.csv")
mun <- read_csv("~/declaranet/data/states/r_mun.csv")

some_cols <- c(
               "prop_window",
               "contract_duration",
               "amount",
               "buyer_dispersion",
               "supplier_dispersion",
               "single_bid",
               "e_exp_r",
               "very_high_r",
               "c_very_high_r")

new_cols <- c(
              "PropWindow",
              "Duration",
              "Amount",
              "BuyerDisp.",
              "SupplierDisp.",
              "SingleBid",
              "CE",
              "CP",
              "CPC")

federal %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.6, size = 2, color = "grey50") +
  labs(title="Federal Contracts Correlation Matrix") +
  ggsave('declaranet/figures/federal_state.pdf')

state %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.6, size = 2, color = "grey50") +
  labs(title="State Contracts") +
  ggsave('declaranet/figures/state_state.pdf')


mun %>%
  dplyr::select(all_of(some_cols)) %>%
  rename_at(vars(some_cols), ~ new_cols) %>%
  ggcorr(nbreaks = 5, method=c("pairwise", "pearson"),
         geom="circle", hjust = 0.60, size = 2, color = "grey50") +
  labs(title="Municipal Contracts") +
  ggsave('declaranet/figures/mun_state.pdf')


