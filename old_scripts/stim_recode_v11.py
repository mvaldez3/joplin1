# have to import pandas and np into program before running 
import pandas as pd
import numpy as np
import csv

def randpro_select(prototype_file, random_seed = None):
	"""Selects a random prototype from a prototype file.

		Inputs:
		prototype_file - .csv file containing a list of prototypes. Each prototype should be its own row and each feature
		should be its own column.

		Output:
		Numpy array of randomly selected prototype"""

	# Open prototype file and randomly select a prototype
	proto_file = pd.read_csv(prototype_file, header=None)

	# Select a random prototype from the file
	randpro = np.array(proto_file.sample(n=1, random_state=random_seed))
	print(randpro)
	return randpro

'''This function creates a file containing the training stimuli. So, it either returns the training file we gave it originall (if the prototype is all 1's),
or it recodes the training set with respect to the prototype and returns a csv file that we can then feed into other functions.'''

def create_train_set(stim_file, random_prototype_selection):
	#define prototype 1 for comparison later
	all1proto = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

	#open the training stimuli set through pandas
	stim_file = pd.read_csv(stim_file, header=None)

	# count the number of rows in the training file
	count = len(list(stim_file.index))

	#create a list of the range of number of rows for future comparison
	num_rows = []
	for i in range(count):
		num_rows.append(i)

	# if the random prototype is all 1, take the stimulus file as is
	if np.array_equal(random_prototype_selection, all1proto) is True:
		t_file = []
		for i in num_rows:
			single_row = np.array(stim_file.iloc[i])
			row = single_row.tolist()
			t_file.append(row)

		training_stim_file = open('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', 'w+', newline = '')
		write = csv.writer(training_stim_file)
		write.writerows(t_file)
	
	# if the random prototype is not all 1, recode the stimulus file and return as csv in same format
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
		
		training_stim_file = open('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_file.csv', 'w+', newline = '')
		with training_stim_file:
			for n in t_file:
				write = csv.writer(training_stim_file)
				write.writerows(n)


def cond_file_build(training_stim):
	# Open the training stimuli set
	train_stim = pd.read_csv(training_stim, header=None)
	
	count = len(list(train_stim.index))

	num_rows = []
	for i in range(count):
		num_rows.append(i)

	sum_feat = []
	stim_id = []
	for i in num_rows:
		# convert the pandas series to numpy array for easier manipulation
		pd2np = np.array((train_stim.iloc[i]).to_numpy())

		# need to sum across all arrays to make a variable for categorization
		sums = np.sum(pd2np)
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

	id_df.loc[id_df.sums_feat > 5, 'category'] = 'Batmans'
	id_df.loc[id_df.sums_feat < 5, 'category'] = 'Robins'

	id_df.loc[id_df.category == 'Batmans', 'correct_key'] = 'f'
	id_df.loc[id_df.category == 'Robins', 'correct_key'] = 'j'
	
	
	# convert to csv so psychopy can read
	csv_file = id_df.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_cond_file.csv', header=True, index=False)

	return csv_file