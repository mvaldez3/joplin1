#load libraries
library(dplyr)
library(readr)

#list all of the participant numbers and session numbers
participant <- c('888', '999')
session <- c('001', '002')

# specify file path to the data files 
csv_path <- '/Volumes/shares/Cabi/exp/joplin/joplin1/data/'
csv_file_end <- '_joplin1.csv'

#specify results file
results_file <- '/Volumes/shares/Cabi/exp/joplin/joplin1/analysis_scripts/accuracy_results.csv'

#set working directory
setwd('/Volumes/shares/Cabi/exp/joplin/joplin1/data')
list_of_files <- list()

#make a list of the file paths for the partcipant data
for (sub in participant){
  for (sess in session){
    data <- paste0('data/', sub, '_', sess)
    filepath <- paste0(csv_path, sub, '_', sess, csv_file_end)
    if (file.exists(filepath) == TRUE) {
      data <- paste0(csv_path, sub, '_', sess, csv_file_end, sep ='')
      list_of_files <- append(list_of_files, filepath)
    if (file.exists(filepath) == FALSE) {
      next
    }
    }
  }
}
data <- read_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/999_002_joplin1.csv')

runs = c('1', '2', '3', '4', '5', '6', '7', '8')

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
  name <- paste(session_name, var_name, val, sep = '')
  block <- (strtoi(val)) -1
  accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block)]))/
    length(na.omit(data$train_key.corr[which(data$train_runs.thisN == block)]))
  assign(name, accuracy)
}

### D2 Train Accuracy By Block - returned as 'session_d2_blkN' where N is the run
var_name = '_d2_blk'
for (val in runs) {
  name <- paste(session_name, var_name, val, sep = '')
  block <- (strtoi(val)) -1
  accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 2 | data$train_runs.thisN == block & data$sums_feat == 8)]))/
    length(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 2 | data$train_runs.thisN == block & data$sums_feat == 8)]))
  assign(name, accuracy)
}


### D4 Accuracy By Block - returned as 'session_d4_blkN' where N is the run
var_name = '_d4_blk'
for (val in runs) {
  name <- paste(session_name, var_name, val, sep = '')
  block <- (strtoi(val)) -1
  accuracy <- sum(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 4 | data$train_runs.thisN == block & data$sums_feat == 6)]))/
    length(na.omit(data$train_key.corr[which(data$train_runs.thisN == block & data$sums_feat == 4 | data$train_runs.thisN == block & data$sums_feat == 6)]))
  assign(name, accuracy)
}

### Overall Generalization Accuracy - returned as 'session_overall_gen'
var_name = '_overall_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 | data$test_runs.thisN == 1)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 | data$test_runs.thisN == 1)]))
assign(name, accuracy)


### D2 Old Generalization Accuracy - returned as 'session_d2_old_gen'

var_name = '_d2_old_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 1 | 
                                       data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 1 | 
                                       data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 1 | 
                                       data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 1)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 1 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 1 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 1 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 1)]))
assign(name, accuracy)


### D4 Old Generalization Accuracy - returned as 'session_d4_old_gen'
var_name = '_d4_old_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 1 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 1)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 1 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 1| 
                                            data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 1 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 1)]))
assign(name, accuracy)


### D0 New Generalization Accuracy - returned as 'session_d0_new_gen'
var_name = '_d0_new_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 0 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 10 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 0 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 10 & data$train_item == 0)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 0 & data$train_item == 0 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 10 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 0 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 10 & data$train_item == 0)]))
assign(name, accuracy)

### D1 New Generalization Accuracy - returned as 'session_d1_new_gen'
var_name = '_d1_new_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 1 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 9 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 1 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 9 & data$train_item == 0)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 1 & data$train_item == 0 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 9 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 1 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 9 & data$train_item == 0)]))
assign(name, accuracy)

       
### D2 New Generalization Accuracy - returned as 'session_d2_new_gen'
var_name = '_d2_new_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 0| 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 0)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 2 & data$train_item == 0 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 8 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 2 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 8 & data$train_item == 0)]))
assign(name, accuracy)


### D3 New Generalization Accuracy - returned as 'session_d3_new_gen'
var_name = '_d3_new_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 3 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 7 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 3 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 7 & data$train_item == 0)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 3 & data$train_item == 0 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 7 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 3 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 7 & data$train_item == 0)]))
assign(name, accuracy)


### D4 New Generalization Accuracy - returned as 'session_d4_new_gen'
var_name = '_d4_new_gen'
name <- name <- paste(session_name, var_name, sep = '')
accuracy <- sum(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 0 | 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 0| 
                                                     data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 0)]))/
  length(na.omit(data$test_key.corr[which(data$test_runs.thisN == 0 & data$sums_feat == 4 & data$train_item == 0 | 
                                            data$test_runs.thisN == 0 & data$sums_feat == 6 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 4 & data$train_item == 0 | 
                                            data$test_runs.thisN == 1 & data$sums_feat == 6 & data$train_item == 0)]))
assign(name, accuracy)


# write the results to a data frame and append to the end of the csv file 
#results <- data.frame(participant = participant, list_of_var = list_of_var)
                   
#write.table(results, 
          #file = results_file,
          #sep = ',',
         #append = TRUE,
         #col.names = FALSE,
         #quote = FALSE,
         #row.names = FALSE)