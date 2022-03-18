# import libraries
import numpy as np
import pandas as pd
import sys


def load_data(messages_filepath, categories_filepath):
	#Read files 
	file1 = pd.read_csv(messages_filepath)
	file2 = pd.read_csv(categories_filepath)
	#Merge files into datasets
	df = pd.merge(file1,file2, on='id')
	return(df)


def clean_data(df):

	# create a dataframe of the 36 individual category columns
	categories = pd.Series(df['categories']).str.split(";", expand=True)
	
	# select the first row of the categories dataframe and remove last 2 char on each row
	row = categories.iloc[0]
	category_colnames =  row.apply( lambda x: (x[:-2]))
	
	# rename the columns of `categories`
	categories.columns = category_colnames

	#Iterate through the category columns in df to keep only the last character of each string 
	for column in categories:
		# set each value to be the last character of the string
		categories[column] = categories[column].str[-1]
		# convert column from string to numeric    
		categories[column] = (categories[column]).astype(int)
    		#Drop invalid values - values greater than 1 are not valid.
		categories.drop(categories.index[categories[column].astype(int) > 1 ], inplace=True)
	
	# drop the original categories column & id from `df` 
	df.drop(['categories','id'] ,axis=1,inplace=True)

	# concatenate the original dataframe with the new `categories` dataframe using inner join.
	df = pd.concat([df,categories],axis=1,join='inner')

	# drop duplicates
	df = df.drop_duplicates()
    
	return(df)


def save_data(df, database_filename):
	import sqlite3
	# connect to the database

	conn = sqlite3.connect('DisasterResponse.db')
	conn.execute("DROP TABLE IF EXISTS merged")

	# TODO: output the df_merged dataframe to a SQL table called 'merged'.
	df.to_sql('merged',con=conn, schema='DisasterResponse.db' ,if_exists='replace')

	conn.close()

	pass  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()