import numpy as np
#import model
from flask import Flask, request, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    
    '''
    suggest movies based on input
    '''
    user_input = [x for x in request.form.values()]
    movie = user_input[0]
    df_transformed = pd.read_excel("df_transformed.xlsx", index_col = "titles")
    #print(df_transformed.head())
    #df_transformed.set_index("titles", inplace = True)
    key = df_transformed.loc[movie]
    
    scores = df_transformed.dot(key)
    recommendation_list = list(scores.nlargest(11).index)
        
    return render_template('recommend.html', recommendation_text=recommendation_list[1:])

if __name__ == "__main__":
    app.run(debug=True)
