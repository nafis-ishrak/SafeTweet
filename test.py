import sklearn
import pickle
import numpy as np

vect = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

arr = []

text = input()
arr.append(text)

words = vect.transform(arr)
result = model.predict(words)

if result == np.array([1]):
    print("Our model predicts the tweet to be RELIGION based cyberbullying")
elif result == np.array([2]):
    print("Our model predicts the tweet to be AGE based cyberbullying")
elif result == np.array([3]):
    print("Our model predicts the tweet to be ETHNICITY based cyberbullying")
elif result == np.array([4]):
    print("Our model predicts the tweet to be GENDER based cyberbullying")
elif result == np.array([5]):
    print("Our model predicts the tweet to be OTHER CYBERBULLYING TYPE")
elif result == np.array([6]):
    print("Our model predicts the tweet to be NOT CYBERBULLYING")
