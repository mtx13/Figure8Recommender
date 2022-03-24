# import libraries
import sys
import pandas as pd
import numpy as np
import re
import sqlite3
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize, punkt
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')



def load_data(database_filepath):
	'''
	Load data from the SQLite database into a dataframe.

	Create X & y values for prediction.
	'''

	conn = sqlite3.connect(database_filepath)

	df = pd.read_sql("SELECT * FROM merged" , con = conn)

	conn.close()
	#df = df.head(1000)

	X =  df['message']
	y = df.drop(['index','message','original','genre'], axis=1)
	category_names = y.columns.tolist()
  
	return(X,y, category_names)


def tokenize(text):
	'''
	Process data to remove stop words, puncuation, normalize text (lower case) & tokenize data.

	Return the cleaned texted.
	'''
	lemmatizer = WordNetLemmatizer()
	stop_words = stopwords.words("english")
    
	tokens = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
	tokens = word_tokenize(tokens)
    
	clean_tokens = []
	for tok in tokens:

        	#clean_tok =  [lemmatizer.lemmatize(word).lower().strip() for word in clean_tok if word not in stop_words]
	        clean_tok =  [lemmatizer.lemmatize(word) for word in tok if word not in stop_words]
	        clean_tokens.append(tok)


	return(clean_tokens)



def build_model():
    '''
    Pipeline to apply tokenizer, transform data, grid search hyperparameters and build optimized model.
    
    '''  
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            
        ])),

        
        ('clf', MultiOutputClassifier(XGBClassifier(use_label_encoder=False)))
    ])

    parameters = {
        
        'clf__estimator__learning_rate' : [ 0.001, 0.01, 0.1 ],
        'clf__estimator__n_estimators' : [ 10, 25],
	'clf__estimator__eval_metric' : ['logloss','rmse']
        
                
    }
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose = 3)

    return cv


def evaluate_model(model, X_test, y_test, category_names):
    	'''
	Display f1, precision and accuracy for each category prediction. 
	'''
    	from sklearn.metrics import multilabel_confusion_matrix

    	y_pred = model.predict(X_test)


    	print(classification_report(y_test, y_pred, target_names = category_names ))

    	pass


def save_model(model, model_filepath):
	'''
	Save the model to a local working directory.
    
	Example used to export to pickle found:
	https://ianlondon.github.io/blog/pickling-basics/
	'''

	import pickle
	# open a file, where you ant to store the model
	file = open(model_filepath, 'wb')

	# dump model to that file
	pickle.dump(model, file)
	pass


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()