def stim_build(prototype_file, stim_file):

#Import all relevant packages
	import pandas as pd
	import numpy as np

### Open prototype file and randomly select a prototype
	proto_file = pd.read_csv(prototype_file, header = None)

#define possible prototypes as numpy arrays for later comparison
	all1proto = np.array([[1,1,1,1,1,1,1,1,1,1]])

#select a random prototype from the file
	randpro = np.array(proto_file.sample())


### Open the training stimuli set
	train_file = pd.read_csv(stim_file, header = None)

#count the number of rows in the training file
	count = len(list(train_file.index))

#make a variable that contains a list of the total number of rows in the training file

	num_rows = []
	for i in range(count):
		num_rows.append(i)


# make for loop that selects base stimulus set if randomly selected prototype = All 1's and recodes the stimulus if not

	if np.array_equal(randpro, all1proto) == True:
		sum_feat = []
		stim_id = []
		for n in train_file:
			#convert the pandas series to numpy array for easier manipulation 
			pd2np = np.array((train_file.iloc[n]).to_numpy())
		
			#need to sum across all arrays to make a variable for categorization
			sums = np.sum(pd2np)
			sum_feat.append(sums)

			#convert all elements in array from integers to strings to use in psychopy
			int2str = np.array2string(pd2np)
			stim_id.append(int2str)

		#convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
		sum_feat = np.asarray(sum_feat)
		stim_id = np.asarray(stim_id)

		#clean up array to match format of stim names in stim folder
		stim_id = np.array(stim_id)
		for x in stim_id:
			stim_id = (np.char.strip(stim_id, '[]'))


	

		### create dataframe for reading into psychopy
		id_df = pd.DataFrame(data = stim_id, columns = None)
		id_df = id_df.astype(str)
		id_df['sum_feat'] = sum_feat.tolist()
		id_df['category'] = ''
		id_df['correct_key'] = ''
		id_df.columns = ['stim_id', 'sums_feat', 'category', 'correct_key']


		#specify parameters for categorization 

		id_df.loc[id_df.sums_feat > 5, 'category'] = 'batmans'
		id_df.loc[id_df.sums_feat < 5, 'category'] = 'robins'

		id_df.loc[id_df.category == 'batmans', 'correct_key'] = 'f'
		id_df.loc[id_df.category == 'robins', 'correct_key'] = 'j'
		print(id_df)

		#convert to csv
		csv_file = id_df.to_csv('_stimfile.csv', header = True, index = False)

	else:
		sums_feat = []
		recoded_id = []
	
		for i in num_rows:
			single_row = np.array(train_file.iloc[i])
		
			# convert randpro to numpy array for commparison
			randpro_arr = np.array(randpro)

			#compare each element in the randomly selected prototype to each element in the row
			compare = randpro_arr == single_row


			#convert the bool phrases into integers 
			bool2int = compare*1
		

			#sum across all arrays to make a variable for categorization
			sums = np.sum(bool2int)
			sums_feat.append(sums)
		

			#convert integers into string
			int2str = np.array2string(bool2int)
			#append each row to the last
			recoded_id.append(int2str)

		#convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
		sums_feat = np.asarray(sums_feat)
		recoded_id = np.asarray(recoded_id)

		#clean up formatting of arrays to match format of stim name
		for x in recoded_id:
			recoded_id = (np.char.strip(recoded_id, '[]'))
			recoded_id = (np.char.strip(recoded_id, ' '))
	
	
		### create dataframe for reading into psychopy
		id_df = pd.DataFrame(data = recoded_id, columns = None)
		id_df = id_df.astype(str)
		id_df['sums_feat'] = sums_feat.tolist()
		id_df['category'] = ''
		id_df['correct_key'] = ''
		id_df.columns = ['stim_id', 'sums_feat', 'category', 'correct_key']


		id_df.loc[id_df.sums_feat < 5, 'category'] = 'batmans'
		id_df.loc[id_df.sums_feat > 5, 'category'] = 'robins'

		id_df.loc[id_df.category == 'batmans', 'correct_key'] = 'f'
		id_df.loc[id_df.category == 'robins', 'correct_key'] = 'j'

		print(id_df)

		#convert to csv
		csv_file = id_df.to_csv('_stimfile.csv', header = True, index = False)
	
		return csv_file

if __name__ == '__main__':
	stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/csv_files/Prototype.csv','/Volumes/shares/Cabi/exp/joplin/joplin1/csv_files/dev_train.csv')
