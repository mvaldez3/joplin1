#load libraries
library(dplyr)
library(readr)

#list all of the participant numbers and session numbers
participant <- list('105')
runs <- c('1', '2', '3', '4', '5', '6', '7', '8')

#specify results file
results_file <- '/Volumes/shares/Cabi/exp/joplin/joplin1/analysis_scripts/acc_results.csv'

# specify file path to the data files 
csv_path <- '/Volumes/shares/Cabi/exp/joplin/joplin1/data/'
csv_file_end <- '_joplin1.csv'

for (part in participant){
  # make paths to data file
  data1 <- read_csv(paste0(csv_path, participant, '_001', csv_file_end))
  data2 <- read_csv(paste0(csv_path, participant, '_002', csv_file_end))
  
  ### SESSION 1 ###
  
  # overall accuracy for blk 1
  block = 0
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk1 <- total_corr/length
  
  # overall accuracy for blk 2
  block = 1
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk2 <- total_corr/length
  
  # overall accuracy for blk 3
  block = 2
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk3 <- total_corr/length
  
  # overall accuracy for blk 4
  block = 3
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk4 <- total_corr/length
  
  # overall accuracy for blk 5
  block = 4
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk5 <- total_corr/length
  
  # overall accuracy for blk 6
  block = 5
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk6 <- total_corr/length
  
  # overall accuracy for blk 7
  block = 6
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk7 <- total_corr/length
  
  # overall accuracy for blk 8
  block = 7
  rows <- which(data1$train_runs.thisN == block)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows) - 1
  s1_all_blk8 <- total_corr/length
  
  # distance 2 blk 1
  block = 0
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk1 <- total_corr/length
  
  # distance 2 blk 2
  block = 1
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk2 <- total_corr/length
  
  # distance 2 blk 3
  block = 2
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk3 <- total_corr/length
  
  # distance 2 blk 4
  block = 3
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk4 <- total_corr/length
  
  # distance 2 blk 5
  block = 4
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk5 <- total_corr/length
  
  # distance 2 blk 6
  block = 5
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk6 <- total_corr/length
  
  # distance 2 blk 7
  block = 6
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk7 <- total_corr/length
  
  # distance 2 blk 8
  block = 7
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 2 | data1$train_runs.thisN == block & data1$sums_feat == 8)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d2_blk8 <- total_corr/length
  
  # distance 4 blk 1
  block = 0
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk1 <- total_corr/length
  
  # distance 4 blk 2
  block = 1
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk2 <- total_corr/length
  
  # distance 4 blk 3
  block = 2
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk3 <- total_corr/length
  
  # distance 4 blk 4
  block = 3
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk4 <- total_corr/length
  
  # distance 4 blk 5
  block = 4
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk5 <- total_corr/length
  
  # distance 4 blk 6
  block = 5
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk6 <- total_corr/length
  
  # distance 4 blk 7
  block = 6
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk7 <- total_corr/length
  
  # distance 4 blk 8
  block = 7
  rows <- which(data1$train_runs.thisN == block & data1$sums_feat == 4 | data1$train_runs.thisN == block & data1$sums_feat == 6)
  total_corr <- sum(na.omit(data1$train_key.corr[rows]))
  length <- length(rows)
  s1_d4_blk8 <- total_corr/length
  #######
  # overall generalization accuracy
  rows <- which(data1$test_runs.thisN == 0 | data1$test_runs.thisN == 1)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows) -2
  s1_all_gen <- total_corr/length
  
  # distance 2 old generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 2 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 8 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 2 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 8 & data1$train_item == 1)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d2_old <- total_corr/length
  
  # distance 2 new generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 2 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 8 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 2 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 8 & data1$train_item == 0)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d2_new <- total_corr/length
  
  
  # distance 4 old generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 4 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 6 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 4 & data1$train_item == 1 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 6 & data1$train_item == 1)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d4_old <- total_corr/length
  
  # distance 4 new generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 4 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 6 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 4 & data1$train_item == 0 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 6 & data1$train_item == 0)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d4_new <- total_corr/length
  
  # distance 0 generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 0 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 10 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 0 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 10)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d0_gen <- total_corr/length
  
  # distance 1 generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 1 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 9 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 1 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 9)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d1_gen <- total_corr/length
  
  # distance 3 generalization
  rows <- which(data1$test_runs.thisN == 0 & data1$sums_feat == 3 | 
                  data1$test_runs.thisN == 0 & data1$sums_feat == 7 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 3 | 
                  data1$test_runs.thisN == 1 & data1$sums_feat == 7)
  total_corr <- sum(na.omit(data1$test_key.corr[rows]))
  length <- length(rows)
  s1_d3_gen <- total_corr/length
  
  ### SESSION 2 ###
  
  # overall accuracy for blk 1
  block = 0
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk1 <- total_corr/length
  
  # overall accuracy for blk 2
  block = 1
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk2 <- total_corr/length
  
  # overall accuracy for blk 3
  block = 2
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk3 <- total_corr/length
  
  # overall accuracy for blk 4
  block = 3
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk4 <- total_corr/length
  
  # overall accuracy for blk 5
  block = 4
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk5 <- total_corr/length
  
  # overall accuracy for blk 6
  block = 5
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk6 <- total_corr/length
  
  # overall accuracy for blk 7
  block = 6
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk7 <- total_corr/length
  
  # overall accuracy for blk 8
  block = 7
  rows <- which(data2$train_runs.thisN == block)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows) - 1
  s2_all_blk8 <- total_corr/length
  
  # distance 2 blk 1
  block = 0
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk1 <- total_corr/length
  
  # distance 2 blk 2
  block = 1
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk2 <- total_corr/length
  
  # distance 2 blk 3
  block = 2
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk3 <- total_corr/length
  
  # distance 2 blk 4
  block = 3
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk4 <- total_corr/length
  
  # distance 2 blk 5
  block = 4
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk5 <- total_corr/length
  
  # distance 2 blk 6
  block = 5
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk6 <- total_corr/length
  
  # distance 2 blk 7
  block = 6
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk7 <- total_corr/length
  
  # distance 2 blk 8
  block = 7
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 2 | data2$train_runs.thisN == block & data2$sums_feat == 8)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d2_blk8 <- total_corr/length
  
  # distance 4 blk 1
  block = 0
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk1 <- total_corr/length
  
  # distance 4 blk 2
  block = 1
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk2 <- total_corr/length
  
  # distance 4 blk 3
  block = 2
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk3 <- total_corr/length
  
  # distance 4 blk 4
  block = 3
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk4 <- total_corr/length
  
  # distance 4 blk 5
  block = 4
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk5 <- total_corr/length
  
  # distance 4 blk 6
  block = 5
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk6 <- total_corr/length
  
  # distance 4 blk 7
  block = 6
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk7 <- total_corr/length
  
  # distance 4 blk 8
  block = 7
  rows <- which(data2$train_runs.thisN == block & data2$sums_feat == 4 | data2$train_runs.thisN == block & data2$sums_feat == 6)
  total_corr <- sum(na.omit(data2$train_key.corr[rows]))
  length <- length(rows)
  s2_d4_blk8 <- total_corr/length
  
  # overall generalization accuracy
  rows <- which(data2$test_runs.thisN == 0 | data2$test_runs.thisN == 1)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows) -2
  s2_all_gen <- total_corr/length
  
  # distance 2 old generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 2 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 8 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 2 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 8 & data2$train_item == 1)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d2_old <- total_corr/length
  
  # distance 2 new generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 2 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 8 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 2 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 8 & data2$train_item == 0)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d2_new <- total_corr/length
  
  
  # distance 4 old generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 4 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 6 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 4 & data2$train_item == 1 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 6 & data2$train_item == 1)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d4_old <- total_corr/length
  
  # distance 4 new generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 4 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 6 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 4 & data2$train_item == 0 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 6 & data2$train_item == 0)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d4_new <- total_corr/length
  
  # distance 0 generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 0 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 10 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 0 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 10)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d0_gen <- total_corr/length
  
  # distance 1 generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 1 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 9 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 1 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 9)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d1_gen <- total_corr/length
  
  # distance 3 generalization
  rows <- which(data2$test_runs.thisN == 0 & data2$sums_feat == 3 | 
                  data2$test_runs.thisN == 0 & data2$sums_feat == 7 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 3 | 
                  data2$test_runs.thisN == 1 & data2$sums_feat == 7)
  total_corr <- sum(na.omit(data2$test_key.corr[rows]))
  length <- length(rows)
  s2_d3_gen <- total_corr/length
  
  results <- data.frame(participant = part,
                        s1_all_blk1 = s1_all_blk1,
                        s1_all_blk2 = s1_all_blk2,
                        s1_all_blk3 = s1_all_blk3,
                        s1_all_blk4 = s1_all_blk4,
                        s1_all_blk5 = s1_all_blk5,
                        s1_all_blk6 = s1_all_blk6,
                        s1_all_blk7 = s1_all_blk7,
                        s1_all_blk8 = s1_all_blk8,
                        s1_d2_blk1 = s1_d2_blk1,
                        s1_d2_blk2 = s1_d2_blk2,
                        s1_d2_blk3 = s1_d2_blk3,
                        s1_d2_blk4 = s1_d2_blk4,
                        s1_d2_blk5 = s1_d2_blk5,
                        s1_d2_blk6 = s1_d2_blk6,
                        s1_d2_blk7 = s1_d2_blk7,
                        s1_d2_blk8 = s1_d2_blk8,
                        s1_d4_blk1 = s1_d4_blk1,
                        s1_d4_blk2 = s1_d4_blk2,
                        s1_d4_blk3 = s1_d4_blk3,
                        s1_d4_blk4 = s1_d4_blk4,
                        s1_d4_blk5 = s1_d4_blk5,
                        s1_d4_blk6 = s1_d4_blk6,
                        s1_d4_blk7 = s1_d4_blk7,
                        s1_d4_blk8 = s1_d4_blk8,
                        s1_all_gen = s1_all_gen,
                        s1_d0_gen = s1_d0_gen,
                        s1_d1_gen = s1_d1_gen,
                        s1_d2_old = s1_d2_old,
                        s1_d2_new = s1_d2_new,
                        s1_d3_gen = s1_d3_gen,
                        s1_d4_old = s1_d4_old,
                        s1_d4_new = s1_d4_new,
                        s2_all_blk1 = s2_all_blk1,
                        s2_all_blk2 = s2_all_blk2,
                        s2_all_blk3 = s2_all_blk3,
                        s2_all_blk4 = s2_all_blk4,
                        s2_all_blk5 = s2_all_blk5,
                        s2_all_blk6 = s2_all_blk6,
                        s2_all_blk7 = s2_all_blk7,
                        s2_all_blk8 = s2_all_blk8,
                        s2_d2_blk1 = s2_d2_blk1,
                        s2_d2_blk2 = s2_d2_blk2,
                        s2_d2_blk3 = s2_d2_blk3,
                        s2_d2_blk4 = s2_d2_blk4,
                        s2_d2_blk5 = s2_d2_blk5,
                        s2_d2_blk6 = s2_d2_blk6,
                        s2_d2_blk7 = s2_d2_blk7,
                        s2_d2_blk8 = s2_d2_blk8,
                        s2_d4_blk1 = s2_d4_blk1,
                        s2_d4_blk2 = s2_d4_blk2,
                        s2_d4_blk3 = s2_d4_blk3,
                        s2_d4_blk4 = s2_d4_blk4,
                        s2_d4_blk5 = s2_d4_blk5,
                        s2_d4_blk6 = s2_d4_blk6,
                        s2_d4_blk7 = s2_d4_blk7,
                        s2_d4_blk8 = s2_d4_blk8,
                        s2_all_gen = s2_all_gen,
                        s2_d0_gen = s2_d0_gen,
                        s2_d1_gen = s2_d1_gen,
                        s2_d2_old = s2_d2_old,
                        s2_d2_new = s2_d2_new,
                        s2_d3_gen = s2_d3_gen,
                        s2_d4_old = s2_d4_old,
                        s2_d4_new = s2_d4_new)
  write.table(results, 
              file = results_file,
              append = T,
              sep = ',',
              col.names = F,
              row.names = F,
              quote = F,
              eol = '\n')
}
