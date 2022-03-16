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
   - [sqlalchemy create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html) --- to connect to SQLite database 
        
        
        
## Project Motivation <a name="motivation"></a>
  This project was built as part of the Udacity Data Science nanodegree.
  The objective is to load disaster call messages and build a recommender engine to correctly categorize each message based on the 36 categories provided by FigureEight. 
  ....
  TBC


## File Descriptions <a name="files"></a>
**-Data ETL Pipeline**
 - data/process_data.py -- this script will merge the category & message files list below and load to the SQLite database.
 - data/disaster_categories.csv  -- list of disaster categories (provided by Figure Eight)
 - data/disaster_messages.csv  -- disaster messages (provided by Figure Eight)
 
**-ML Pipeline**
- models/train_classifier.py -- this script will build a pipeline to transform, scale and fit the data using a CatBoost algorithm


**-Web IDE**
 - app/run.py
 - app/templates/go.html
 - app/templates/master.html


## Execution <a name = "execution"></a>
**-Merge and Load data**
python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

**-Process/Prepare Data and Train model**
python train_classifier.py ../data/DisasterResponse.db classifier.pkl

## Project Results <a name="results"></a>




## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
All data was provide by Figure Eight via Udacity.

Other acknowledgements of code leveraged via Stackoverflow are documented within the code itself. 


