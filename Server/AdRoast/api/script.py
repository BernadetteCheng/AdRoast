import pickle

adroast_model = pickle.load(open('adroast_model.sav', 'rb'))
result = adroast_model.predict("")
