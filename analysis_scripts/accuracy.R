#load libraries
library(dplyr)
library(readr)

#list all of the participant numbers and session numbers
participant <- c('103')

#specify results file
results_file <- '/Volumes/shares/Cabi/exp/joplin/joplin1/analysis_scripts/accuracy_results.csv'

# specify file path to the data files 
csv_path <- '/Volumes/shares/Cabi/exp/joplin/joplin1/data/'
csv_file_end <- '_joplin1.csv'

#make a list of the file paths for the participant data
data_sess1 <- paste0(csv_path, participant, '_001', csv_file_end)
list_of_files <- list(data_sess1)
data_sess2 <- paste0(csv_path, participant, '_002', csv_file_end)
if (file.exists(data_sess2) == TRUE){
  list_of_files <- append(list_of_files, data_sess2)
}


for (file in list_of_files){
  runs <- c('1', '2', '3', '4', '5', '6', '7', '8')
  data <- read_csv(file)
  session <- data$session[1]
  participant <- data$participant[1]
  if (session == '001'){
    session_name <- 's1'
  }
  if (session == '002') {
    session_name <- 's2'
  }
  ### Overall Accuracy By Block - returned as 'session_overall_blkN' where S is the session and N is the run
  var_name = '_overall_blk'
  
  for (val in runs) {
    name <- paste0(session_name, var_name, val, sep = '')
    block <- (strtoi(val)) -1
    accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block)]))/
      length(which(data$train_runs.thisN == block))
    assign(name, accuracy)
  }
  
  ### D2 Train Accuracy By Block - returned as 'session_d2_blkN' where N is the run
  var_name = '_d2_blk'
  for (val in runs) {
    name <- paste0(session_name, var_name, val, sep = '')
    block <- (strtoi(val)) -1
    accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 2 | data$train_runs.thisN == block & data$sums_feat == 8)]))/
      length(which(data$train_runs.thisN == block & data$sums_feat == 2 | data$train_runs.thisN == block & data$sums_feat == 8))
    assign(name, accuracy)
  }
  
  
  ### D4 Accuracy By Block - returned as 'session_d4_blkN' where N is the run
  var_name = '_d4_blk'
  for (val in runs) {
    name <- paste0(session_name, var_name, val, sep = '')
    block <- (strtoi(val)) -1
    accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 4 | data$train_runs.thisN == block & data$sums_feat == 6)]))/
      length(which(data$train_runs.thisN == block & data$sums_feat == 4 | data$train_runs.thisN == block & data$sums_feat == 6))
    assign(name, accuracy)
  }
  
  ### Overall Generalization Accuracy - returned as 'session_overall_gen'
  var_name = '_overall_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 | data$test_runs.thisN == 1)]))/
    length(which(data$test_runs.thisN == 0 | data$test_runs.thisN == 1))
  assign(name, accuracy)
  
  
  ### D2 Old Generalization Accuracy - returned as 'session_d2_old_gen'
  
  var_name = '_d2_old_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 1)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 1 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 1 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 1 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 1))
  assign(name, accuracy)
  
  
  ### D4 Old Generalization Accuracy - returned as 'session_d4_old_gen'
  var_name = '_d4_old_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 1)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 1 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 1| 
                                              data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 1 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 1))
  assign(name, accuracy)
  
  
  ### D0 New Generalization Accuracy - returned as 'session_d0_new_gen'
  var_name = '_d0_new_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 0 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 10 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 0 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 10 & data$train_item == 0)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 0 & data$train_item == 0 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 10 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 0 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 10 & data$train_item == 0))
  assign(name, accuracy)
  
  ### D1 New Generalization Accuracy - returned as 'session_d1_new_gen'
  var_name = '_d1_new_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 1 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 9 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 1 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 9 & data$train_item == 0)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 1 & data$train_item == 0 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 9 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 1 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 9 & data$train_item == 0))
  assign(name, accuracy)
  
  
  ### D2 New Generalization Accuracy - returned as 'session_d2_new_gen'
  var_name = '_d2_new_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 0| 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 0)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 0 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 0))
  assign(name, accuracy)
  
  
  ### D3 New Generalization Accuracy - returned as 'session_d3_new_gen'
  var_name = '_d3_new_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 3 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 7 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 3 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 7 & data$train_item == 0)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 3 & data$train_item == 0 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 7 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 3 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 7 & data$train_item == 0))
  assign(name, accuracy)
  
  
  ### D4 New Generalization Accuracy - returned as 'session_d4_new_gen'
  var_name = '_d4_new_gen'
  name <- name <- paste0(session_name, var_name, sep = '')
  accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 0| 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 0)]))/
    length(which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 0 | 
                                              data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 0 | 
                                              data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 0))
  assign(name, accuracy)
}

if (length(list_of_files) == 2){
  results <- data.frame(participant = participant,
                        s1_overall_blk1 = s1_overall_blk1,
                        s1_overall_blk2 = s1_overall_blk2,
                        s1_overall_blk3 = s1_overall_blk3,
                        s1_overall_blk4 = s1_overall_blk4,
                        s1_overall_blk5 = s1_overall_blk5,
                        s1_overall_blk6 = s1_overall_blk6,
                        s1_overall_blk7 = s1_overall_blk7,
                        s1_overall_blk8 = s1_overall_blk8,
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
                        s1_overall_gen = s1_overall_gen,
                        s1_d2_old_gen = s1_d2_old_gen,
                        s1_d4_old_gen = s1_d4_old_gen,
                        s1_d0_new_gen = s1_d0_new_gen,
                        s1_d1_new_gen = s1_d1_new_gen,
                        s1_d2_new_gen = s1_d2_new_gen,
                        s1_d3_new_gen = s1_d3_new_gen,
                        s1_d4_new_gen = s1_d4_new_gen,
                        s2_overall_blk1 = s2_overall_blk1,
                        s2_overall_blk2 = s2_overall_blk2,
                        s2_overall_blk3 = s2_overall_blk3,
                        s2_overall_blk4 = s2_overall_blk4,
                        s2_overall_blk5 = s2_overall_blk5,
                        s2_overall_blk6 = s2_overall_blk6,
                        s2_overall_blk7 = s2_overall_blk7,
                        s2_overall_blk8 = s2_overall_blk8,
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
                        s2_overall_gen = s2_overall_gen,
                        s2_d2_old_gen = s2_d2_old_gen,
                        s2_d4_old_gen = s2_d4_old_gen,
                        s2_d0_new_gen = s2_d0_new_gen,
                        s2_d1_new_gen = s2_d1_new_gen,
                        s2_d2_new_gen = s2_d2_new_gen,
                        s2_d3_new_gen = s2_d3_new_gen,
                        s2_d4_new_gen = s2_d4_new_gen
  )
}
if (length(list_of_files) == 1){
  results <- data.frame(participant = participant,
                        s1_overall_blk1 = s1_overall_blk1,
                        s1_overall_blk2 = s1_overall_blk2,
                        s1_overall_blk3 = s1_overall_blk3,
                        s1_overall_blk4 = s1_overall_blk4,
                        s1_overall_blk5 = s1_overall_blk5,
                        s1_overall_blk6 = s1_overall_blk6,
                        s1_overall_blk7 = s1_overall_blk7,
                        s1_overall_blk8 = s1_overall_blk8,
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
                        s1_overall_gen = s1_overall_gen,
                        s1_d2_old_gen = s1_d2_old_gen,
                        s1_d4_old_gen = s1_d4_old_gen,
                        s1_d0_new_gen = s1_d0_new_gen,
                        s1_d1_new_gen = s1_d1_new_gen,
                        s1_d2_new_gen = s1_d2_new_gen,
                        s1_d3_new_gen = s1_d3_new_gen,
                        s1_d4_new_gen = s1_d4_new_gen
  )
}

write.table(results, 
            file = results_file,
            append = T,
            sep = ',',
            col.names = F,
            row.names = F,
            quote = F,
            eol = '\n')

