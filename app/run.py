import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar

#from sklearn.externals import joblib
import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('merged', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():

    # extract data needed for visuals


    category_counts = df.drop(['message','original','genre','index'], axis=1).sum()	
    category_columns = list(category_counts.index)

    #Method to create stacked/side-by-side graph provided by TowardsDataScience.com
    #https://towardsdatascience.com/step-by-step-bar-charts-using-plotly-express-bb13a1264a8b

    pivot = df.drop(['message','original'], axis=1).groupby(['genre']).sum().reset_index()
    cat1 = Bar(x=pivot['genre'], y=pivot[('related')], name='Related')
    cat2 = Bar(x=pivot['genre'], y=pivot[('request')], name='Request')
    cat3 = Bar(x=pivot['genre'], y=pivot[('offer')], name='Offer')
    cat4 = Bar(x=pivot['genre'], y=pivot[('aid_related')], name='Aid Related')
    cat5 = Bar(x=pivot['genre'], y=pivot[('medical_help')], name='Medical Help')


   
    # create visuals
    #Create a bar graph with the count of messages by category.
    graphs = [
        {
            'data': [
                Bar(
		    x = category_columns,
		    y = category_counts



		    
                )
            ],

            'layout': {
                'title': 'Distribution of Category Messages',
          	'template' : 'plotly_dark',
		
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Categories"
                },
		
		    


            }
        },
{
           #Create a side-by-side bar graph showing the count of messages by category and genre.
   	   'data': [
		
		cat1, cat2, cat3, cat4, cat5
	    
            ],

            'layout': {
                'title': 'Distribution of Category Messages by Genre',
          	'template' : 'plotly_dark',
		
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                },
		'barmode' : 'group'



            }
        }






    ]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON, data_set=df)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='127.0.0.1', port=3001, debug=True)


if __name__ == '__main__':
    main()