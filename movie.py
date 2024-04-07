from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
movie = pickle.load(open('df.pkl','rb'))
sim = pickle.load(open('similarity.pkl','rb'))

movie_names = movie['original_title'].values

def reccomend(new_movie):
    index = movie[movie['original_title'] == new_movie].index[0]
    distance = sorted(list(enumerate(sim[index])),reverse = True,key = lambda x: x[1])
    recommendations = []
    for i in distance[0:5]:
        recommendations.append(movie.iloc[i[0]].original_title)
        
    return recommendations

@app.route('/')
def homepage():
    return render_template('movie.html',movie_names = movie_names)

@app.route('/recommend',methods=['POST'])
def predict():
    title_of_movie = request.form.get('movie')
    recomm = reccomend(title_of_movie)
    return render_template('movie.html',recommendations = recomm,movie_names = movie_names,org_title = title_of_movie)


if __name__ == '__main__':
    app.run(debug=True)
    
