# Figure8Recommender
Recommender Engine using Figure Eight Disaster Recovery data

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Execution](#execution)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The following libraries were installed as part of this project:
 - process_data.py
   - SQLite3
        
- train_classifier.py 
  - NLTK tokenize (word_tokenize, punkt) , wordnet (WordNetLemmatizer) , stopwords 
  - XGBClassifier  
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
  The objective is to load disaster call messages and build a recommender engine to correctly categorize each message based on the 36 categories provided by FigureEight.
  The output is a website that can be used to enter a new disaster message and see which categories it would be assigned to.  Graphs are also generated showing the distribution of ..... 
  
  
  
  ....
  TBC


## File Descriptions <a name="files"></a>
**-Data ETL Pipeline**
 - data/process_data.py -- this script will merge the category & message files list below and load to the SQLite database.
 - data/disaster_categories.csv  -- list of disaster categories (provided by Figure Eight)
 - data/disaster_messages.csv  -- disaster messages (provided by Figure Eight)
 
**-ML Pipeline**
- models/train_classifier.py -- this script will retrieve data from the database; tokenize/normalize the text data; optimize and fit the data using XGBoost algorithm. 
- classifier.pkl -- pickle file generated to store the XGBoost model


**-Web IDE**
 - app/run.py -- this script is used to generate the graphs and input text for the model
 

## Execution <a name = "execution"></a>
**-Merge and Load data:**

python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

**-Process/Prepare Data and Train model:**

python train_classifier.py ../data/DisasterResponse.db classifier.pkl

**-Lauch website:**

python run.py

**-Web page can be accessed on local system at:**

http://127.0.0.1:3001/


## Project Results <a name="results"></a>

Because this is largely an acedemic exercise there is plenty of room to improve the accuracy of the model.  Several algorithms were tried including CatBoost, SVC and XGboost.  XGBoost had the best performance time and was used for the final model. 





## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
All data was provide by Figure Eight via Udacity.

Other acknowledgements of code leveraged via Stackoverflow are documented within the code itself. 


