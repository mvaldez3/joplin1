#import packages 
import pandas as pd
import numpy as np
import random
import csv

#this function randomly selects a random prototype from the prototype file
def randpro_select(prototype_file, random_seed):
	random.seed(random_seed)
	with open(prototype_file, encoding='utf-8-sig') as proto_file:
		read = csv.reader(proto_file)
		chosen_row = random.choice(list(read))
	#turns the chosen row into a list of integers to make comparisons easier in the future.
	randpro = []
	for n in chosen_row:
		item = int(n)
		randpro.append(item)
	randpro = np.array(randpro)
	return randpro

#this function creates a csv file whose format is identical to the original file with training stimuli except it is recoded with respect to the stimuli
def create_train_set(stim_file, random_prototype_selection):
	#define prototype 1 for comparison later
	all1proto = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

	#open the training stimuli set with pandas
	stim_file = pd.read_csv(stim_file, header=None)

	#count the number of rows in the training file
	count = len(list(stim_file.index))

	#create a list of the range of number of rows for future comparison
	num_rows = []
	for i in range(count):
		num_rows.append(i)

	#if the random prototype is all 1, take the stimulus file as is
	if np.array_equal(random_prototype_selection, all1proto) is True:
		t_file = []
		for i in num_rows:
			single_row = np.array(stim_file.iloc[i])
			row = single_row.tolist()
			t_file.append(row)
		
		training_stim_file = open('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', 'w+', newline = '')
		write = csv.writer(training_stim_file)
		write.writerows(t_file)
	
	#if the random prototype is not all 1, recode the stimulus file and return as csv in same format
	else:
		t_file = []
		for i in num_rows:
			single_row = np.array(stim_file.iloc[i])

			# convert randpro to numpy array for commparison
			randpro_arr = np.array(random_prototype_selection)

			# compare each element in the randomly selected prototype to each element in the row
			compare = randpro_arr == single_row

			# convert the bool phrases into integers to get the new code
			new_code = compare * 1
			new_code = new_code.tolist()
			t_file.append(new_code)
		
		training_stim_file = open('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', 'w+', newline = '')
		write = csv.writer(training_stim_file)
		write.writerows(t_file)

#this function takes a csv file and formats it as a conditions file to feed into psychopy. Includes the category and correct key.
def train_cond_file(training_stim, random_prototype_selection, random_seed):
	random.seed(random_seed)
	# Open the training stimuli set
	train_stim = pd.read_csv(training_stim, header=None)
	
	#make an array of the possible stimuli
	all1proto = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	all0proto = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	#count the number of rows in the file
	count = len(list(train_stim.index))

	num_rows = []
	for i in range(count):
		num_rows.append(i)

	#make new lists to add as rows to the pandas df
	sum_feat = []
	stim_id = []
	for i in num_rows:
		# convert the pandas series to numpy array for easier manipulation
		pd2np = np.array((train_stim.iloc[i]).to_numpy())

		# need to sum across all arrays to make a variable for categorization
		if np.array_equal(random_prototype_selection, all1proto) is True:
			sums = np.sum(pd2np)
		if np.array_equal(random_prototype_selection, all0proto) is True:
			sums = (10 - np.sum(pd2np))
		sum_feat.append(sums)

		# convert all elements in array from integers to strings to use in psychopy
		int2str = np.array2string(pd2np)
		stim_id.append(int2str)
	# convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
	sum_feat = np.asarray(sum_feat)
	stim_id = np.asarray(stim_id)

	# clean up array to match format of stim names in stim folder
	stim_id = np.array(stim_id)
	stim_id = (np.char.strip(stim_id, '[]'))

	# create dataframe for reading into psychopy
	id_df = pd.DataFrame(data=stim_id, columns=None)
	id_df = id_df.astype(str)
	id_df['sum_feat'] = sum_feat.tolist()
	id_df['category'] = ''
	id_df['correct_key'] = ''
	id_df.columns = ['stim_id', 'sums_feat', 'category', 'correct_key']

	# specify parameters for categorization

	id_df.loc[id_df.sums_feat > 5, 'category'] = 'categoryA'
	id_df.loc[id_df.sums_feat < 5, 'category'] = 'categoryB'

	id_df.loc[id_df.category == 'categoryA', 'correct_key'] = 'f'
	id_df.loc[id_df.category == 'categoryB', 'correct_key'] = 'j'
	
	
	#convert to csv so psychopy can read
	csv_file = id_df.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/cond_file.csv', header=True, index=False)


def gen_build(train_file, prototype_file, random_prototype_selection, num_rows2add, num_proto, num_trainingstim, random_seed):

	random.seed(random_seed)
	all1proto = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	#read in the training file.
	train_file = pd.read_csv(train_file, header=None)
	
	#Rename file because we will want to use the original training file to refer back to. gen_file_starting will be used as the base number of rows we started with, but will change with each iteration of the loop
	gen_file_starting = train_file

	#gen_file will be the file we append the new rows two during each iteration of the loop. At the end of every loop, gen_file will become the new gen_file_starting. 
	gen_file = gen_file_starting


	#create an example of each of the possible distances, specify the number of rows to add for each distance, create an array to loop through
	if np.array_equal(random_prototype_selection, all1proto) is True:
		dist_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
		dist_2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
		dist_3 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
		dist_4 = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
		dist_6 = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
		dist_7 = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
		dist_8 = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
		dist_9 = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	else:
		dist_1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
		dist_2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
		dist_3 = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])
		dist_4 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
		dist_6 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
		dist_7 = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
		dist_8 = np.array([0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
		dist_9 = np.array([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])

	#specify the number of rows to add in total for each distance.
	rows_to_add = num_rows2add

	#create a varible that counts the number of training stimuli we have in the training file
	num_of_stim = len(train_file.index)


	#read in the prototype file
	prototypes = pd.read_csv(prototype_file, header = None)

	#make a file that includes the prototypes and the traiing stimuli. This will be the base of both generalization files.

	#append the training file to the prototype file
	gf_base = prototypes.append(train_file, ignore_index = True)
	gf1_base = gf_base
	gf2_base = gf_base

	# make a list of all the distances to loop through 
	distances = [dist_1, dist_2, dist_3, dist_4, dist_6, dist_7, dist_8, dist_9]

	for dist in distances:
		isokay = True
		while isokay:
			#randomly shuffle the distance array to generate a possible new stimulus
			random.shuffle(dist)
			curr_arr = np.array(dist)
			#compare the generated possible stimulus with all the already added stimuli. This will return a boolean phrase for the comparison to each row.
			all_comparison = []
			for i in list(range(len(gen_file.index))):
				single_row = np.array(gen_file.iloc[i])
				compare = np.array_equal(curr_arr, single_row, equal_nan = False) * 1
				all_comparison.append(compare)
			#convert boolean phrases to integers to make it easier to compare. 1 = True = duplicate = don't add
			duplicate = 1
			if duplicate in all_comparison:
				continue
			#if there it is not a dupicate, add it to the file
			else: 
				data_to_append =  {}
				for i in list(range(len(gen_file.columns))):
					data_to_append[gen_file.columns[i]] = dist[i]
				gen_file = gen_file.append(data_to_append, ignore_index = True)
				#calculate the number of added rows by subtracting the current number of rows by the starting number of rows (starting # changes each iteration of the loop)
				added_rows = (len(gen_file.index) - len(gen_file_starting))
				#recalculate isokay variable. 
				isokay = added_rows < rows_to_add
		#set gen_file_starting equal to the gen_file we just created because we want this to be the new number of rows for when we calculate added_rows in the next iteration
		gen_file_starting = gen_file

	#separate the whole dataframe into 2 separate gen_files that each contain all stimuli, prototypes, and a random 5 rows of each distance

	#calculate which row the gen stim actually start 
	gen_stim_start = num_of_stim

	#index the rows for each distance
	d1_index = list(range(gen_stim_start, gen_stim_start+rows_to_add))
	d2_index = list(range(d1_index[-1]+1, d1_index[-1]+1+rows_to_add))
	d3_index = list(range(d2_index[-1]+1, d2_index[-1]+1+rows_to_add))
	d4_index = list(range(d3_index[-1]+1, d3_index[-1]+1+rows_to_add))
	d6_index = list(range(d4_index[-1]+1, d4_index[-1]+1+rows_to_add))
	d7_index = list(range(d6_index[-1]+1, d6_index[-1]+1+rows_to_add))
	d8_index = list(range(d7_index[-1]+1, d7_index[-1]+1+rows_to_add))
	d9_index = list(range(d8_index[-1]+1, d8_index[-1]+1+rows_to_add))

	#randomly shuffle all of lists to get random rows of each distance
	random.shuffle(d1_index)
	random.shuffle(d2_index)
	random.shuffle(d3_index)
	random.shuffle(d4_index)
	random.shuffle(d6_index)
	random.shuffle(d7_index)
	random.shuffle(d8_index)
	random.shuffle(d9_index)

	#split the shuffled list in half so that half of the rows for each distance go in each file
	half = int(rows_to_add/2)
	d1_1 = d1_index[0:half]
	d1_2 = d1_index[half:rows_to_add]
	d2_1 = d2_index[0:half]
	d2_2 = d2_index[half:rows_to_add]
	d3_1 = d3_index[0:half]
	d3_2 = d3_index[half:rows_to_add]
	d4_1 = d4_index[0:half]
	d4_2 = d4_index[half:rows_to_add]
	d6_1 = d6_index[0:half]
	d6_2 = d6_index[half:rows_to_add]
	d7_1 = d7_index[0:half]
	d7_2 = d7_index[half:rows_to_add]
	d8_1 = d8_index[0:half]
	d8_2 = d8_index[half:rows_to_add]
	d9_1 = d9_index[0:half]
	d9_2 = d9_index[half:rows_to_add]

	# create a list of which rows go in the 1st gen file.
	gf1_data2add = [d1_1, d2_1, d3_1, d4_1, d6_1, d7_1, d8_1, d9_1]


	#create the first data set
	for distance in gf1_data2add:
		for row in distance:
			row = list(gen_file.iloc[row])
			data_to_append =  {}
			for i in list(range(len(gf1_base.columns))):
				data_to_append[gen_file.columns[i]] = row[i]
			gf1_base = gf1_base.append(data_to_append, ignore_index = True)
	gf1 = gf1_base
	#gen_file1 = gf1.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv', header = None, index = False)

	#create the second data set
	gf2_data2add = [d1_2, d2_2, d3_2, d4_2, d6_2, d7_2, d8_2, d9_2]
	for distance in gf2_data2add:
		for row in distance:
			row = list(gen_file.iloc[row])
			data_to_append =  {}
			for i in list(range(len(gf2_base.columns))):
				data_to_append[gen_file.columns[i]] = row[i]
			gf2_base = gf2_base.append(data_to_append, ignore_index = True)
	gf2 = gf2_base
	
	#make genfile 1 csv
	count = len(list(gf1.index))

	#make an array of the possible stimuli
	all1proto = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	all0proto = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	num_rows = []
	for i in range(count):
		num_rows.append(i)

	#make new lists to add as rows to the pandas df
	sum_feat = []
	stim_id = []
	for i in num_rows:
		# convert the pandas series to numpy array for easier manipulation
		pd2np = np.array((gf1.iloc[i]).to_numpy())

		# need to sum across all arrays to make a variable for categorization
		if np.array_equal(random_prototype_selection, all1proto) is True:
			sums = np.sum(pd2np)
		if np.array_equal(random_prototype_selection, all0proto) is True:
			sums = (10 - np.sum(pd2np))
		sum_feat.append(sums)

		# convert all elements in array from integers to strings to use in psychopy
		int2str = np.array2string(pd2np)
		stim_id.append(int2str)
	
	# convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
	sum_feat = np.asarray(sum_feat)
	stim_id = np.asarray(stim_id)

	# clean up array to match format of stim names in stim folder
	stim_id = np.array(stim_id)
	stim_id = (np.char.strip(stim_id, '[]'))
	
	# create dataframe for reading into psychopy
	id_df = pd.DataFrame(data=stim_id, columns=None)
	id_df = id_df.astype(str)
	id_df['train_item'] = ''
	id_df['sum_feat'] = sum_feat.tolist()
	id_df['category'] = ''
	id_df['correct_key'] = ''
	id_df.columns = ['stim_id', 'train_item','sums_feat', 'category', 'correct_key']

	df_row_count = list(range(len(id_df.index)))
	train_item = []
	for n in df_row_count:
		if n < 2:
			train_item.append('0')
		elif num_proto <= n < (num_proto+num_trainingstim):
			train_item.append('1')
		elif (num_proto+num_trainingstim) <= n <= df_row_count[-1]:
			train_item.append('0')
	id_df['train_item'] = train_item

	# specify parameters for categorization

	id_df.loc[id_df.sums_feat > 5, 'category'] = 'categoryA'
	id_df.loc[id_df.sums_feat < 5, 'category'] = 'categoryB'

	id_df.loc[id_df.category == 'categoryA', 'correct_key'] = 'f'
	id_df.loc[id_df.category == 'categoryB', 'correct_key'] = 'j'
	
	
	#convert to csv so psychopy can read
	csv_file = id_df.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv', header=True, index=False)
	
	#make genfile 2 csv
	count = len(list(gf2.index))

	num_rows = []
	for i in range(count):
		num_rows.append(i)

	#make new lists to add as rows to the pandas df
	sum_feat = []
	stim_id = []
	for i in num_rows:
		# convert the pandas series to numpy array for easier manipulation
		pd2np = np.array((gf2.iloc[i]).to_numpy())

		# need to sum across all arrays to make a variable for categorization
		if np.array_equal(random_prototype_selection, all1proto) is True:
			sums = np.sum(pd2np)
		if np.array_equal(random_prototype_selection, all0proto) is True:
			sums = (10 - np.sum(pd2np))
		
		sum_feat.append(sums)

		# convert all elements in array from integers to strings to use in psychopy
		int2str = np.array2string(pd2np)
		stim_id.append(int2str)
	
	# convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
	sum_feat = np.asarray(sum_feat)
	stim_id = np.asarray(stim_id)

	# clean up array to match format of stim names in stim folder
	stim_id = np.array(stim_id)
	stim_id = (np.char.strip(stim_id, '[]'))
	
	# create dataframe for reading into psychopy
	id_df = pd.DataFrame(data=stim_id, columns=None)
	id_df = id_df.astype(str)
	id_df['train_item'] = ''
	id_df['sum_feat'] = sum_feat.tolist()
	id_df['category'] = ''
	id_df['correct_key'] = ''
	id_df.columns = ['stim_id', 'train_item','sums_feat', 'category', 'correct_key']

	df_row_count = list(range(len(id_df.index)))
	train_item = []
	for n in df_row_count:
		if n < 2:
			train_item.append('0')
		elif num_proto <= n < (num_proto+num_trainingstim):
			train_item.append('1')
		elif (num_proto+num_trainingstim) <= n <= df_row_count[-1]:
			train_item.append('0')
	id_df['train_item'] = train_item

	# specify parameters for categorization

	id_df.loc[id_df.sums_feat > 5, 'category'] = 'categoryA'
	id_df.loc[id_df.sums_feat < 5, 'category'] = 'categoryB'

	id_df.loc[id_df.category == 'categoryA', 'correct_key'] = 'f'
	id_df.loc[id_df.category == 'categoryB', 'correct_key'] = 'j'
	
	
	#convert to csv so psychopy can read
	csv_file = id_df.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv', header=True, index=False)

'''randpro = randpro_select('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv', random_seed = 1)
print(randpro)
create_train_set('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/train_file.csv', randpro)
train_cond_file('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', randpro, random_seed = 1)
gen_build('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', '/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv', randpro, 10, 2, 14, random_seed = 1)'''



