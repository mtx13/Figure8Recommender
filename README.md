# Figure8Recommender
Recommender Engine using Figure Eight Disaster Recovery data

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Execution](#execution)
5. [Methodology](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The following libraries were installed as part of this project:
 - process_data.py
   - SQLite3
        
- train_classifier.py 
  - NLTK tokenize (word_tokenize, punkt) , wordnet (WordNetLemmatizer) , stopwords 
  - XGBClassifier  
  - TfidfVectorizer
  - MultiOutputClassifier
  - GridSearchCV
  - make_pipeline
  - classification_report 
  - SQLite3
  - Pickle

- run.py
  -  json
  -  NLTK WordNetLemmatizer , word_tokenize
  -  Flask
  -  Plotly
  -  Sqlalchemy


        
## Project Motivation <a name="motivation"></a>
  This project was built as part of the Udacity Data Science nanodegree.
  
  The objective is to merge and load actual disaster messages provided by Figure Eight Inc. to a database. The next step is to build a recommender engine to correctly categorize each message based on the 36 categories provided by FigureEight. The web app developed as part of othe project can be used to enter new messages and see which agencies should be notified of the disaster.  The web app also graphs some of the data using Plotly.
  
  Details to run python scripts and load the web page can be found in the [Execution](#execution) section. 
  
  
## File Descriptions <a name="files"></a>
**-Data ETL Pipeline**
 - data/process_data.py -- this script will merge the category & message files list below and load to the SQLite database.
 - data/disaster_categories.csv  -- list of disaster categories (provided by Figure Eight)
 - data/disaster_messages.csv  -- disaster messages (provided by Figure Eight)
 
**-ML Pipeline**
- models/train_classifier.py -- this script will retrieve data from the database; tokenize/normalize the text data; optimize and fit the data using XGBoost algorithm. 
- classifier.pkl -- pickle file generated to store the XGBoost model


**-Web IDE**
 - app/run.py -- Flask script to run the web app
 - app/templates/master.html  # main page of web app
 - /app/templates/go.html  # classification result page of web app

## Execution <a name = "execution"></a>
**-Merge and Load data:**

python ./data/process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

**-Process/Prepare Data and Train model:**

python ./models/train_classifier.py ../data/DisasterResponse.db classifier.pkl

**-Launch website:**

python ./app/run.py

**-Web page can be accessed on local system at:**

http://127.0.0.1:3001/


## Project Methodology <a name="results"></a>

Because this is largely an acedemic exercise there is plenty of room to improve the accuracy of the model. 

Each of the .csv file were read into a dataframe. *disaster_messages.csv* contains the unique id, messages and genre.  *disaster_categories.csv* contains the unique id and multiple strings indicating which category is associated with the message. The category strings were converted to binary values. Rows that could not be converted to binary were removed. The data was then joined to the messages dataframe via the unique id and finally loaded to the SQL database. This can be executed using *process_data.py*

Before predicting categories, the data was downloaded from the SQL database. Then the message data was cleaned by converting to lower case, removing special characters and stop words, lemmatizing the data. Data was vectorized for processing. Several predictive algorithms were tested including CatBoost, Random Forest and XGboost. Multiple grid searches were performed with each using a pipeline. XGBoost had the best performance time and accuracy and was selected for the final model. Only the XGBoost model is included. This can be executed using the *train_classifier.py*

The web app was modified from the base page provided by Udacity. The interface allows a user to type a text message.  The code then highlights the predicted categories & agencies to notify. A new graph was created which provides.... *run.py* will launch the web app. 


## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
All data was provide by Figure Eight via Udacity.  Based templates were also provided by Udacity. 

Other acknowledgements of code leveraged via Stackoverflow are documented within the code itself. 


