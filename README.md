# Twitter Cyberbullying Classifier

This project creates a machine learning model that can classify text into 6 categories: religion, age, ethnicity, gender, other cyberbullying, and not cyberbullying. It uses the following libraries:

- pandas
- numpy
- seaborn
- matplotlib
- plotly
- sklearn
- emoji
- string
- nltk

Dataset Used : Cyberbullying Classification data from Kaggle (https://tinyurl.com/twitter-dataset)

The text data is cleaned and preprocessed using various techniques, including the removal of emojis, contractions, hashtags, special characters, and extra spaces. The words are then stemmed and lemmatized using the nltk library.

Wordclouds were created for the top 20 words in each category, and a bar plot was generated to visualize the results.

The model uses the tf-idf vectorizer to vectorize the words in the text and implements several classification models, including linear SVC, decision trees, logistic regression, and naive Bayes. In the end, the linear SVC model was chosen for its generalizability. The model was fine-tuned, and a classification report was provided. The model and vectorizer were saved for future use.

## Methodology

The dataset was first preprocessed and cleaned using various techniques, including the removal of emojis, contractions, hashtags, special characters, and extra spaces. The words were then stemmed and lemmatized using the nltk library.

The preprocessed data was then fed into the tf-idf vectorizer to create a feature matrix. Several classification models were implemented, including linear SVC, decision trees, logistic regression, and naive Bayes. The models were evaluated using cross-validation and the F1-score metric.

The linear SVC model was chosen for its generalizability and fine-tuned using grid search. The final model achieved an accuracy of 82% in predicting the right category of cyberbullying.

## Results

The linear SVC model achieved an average accuracy of 82% in predicting the right category of cyberbullying. The classification report showed that the model performed well in predicting all categories, with the highest F1-score of 0.97 for the "ethnicity" category.

Wordclouds and bar plots were generated to visualize the top 20 words in each category, providing insights into the most common words used in each type of cyberbullying.

## Conclusion

In conclusion, this project has successfully created a machine learning model that can classify text into 6 categories of cyberbullying. The linear SVC model achieved an accuracy of 82% and performed well in predicting all categories. The wordclouds and bar plots provide insights into the most common words used in each type of cyberbullying, which could be useful for further research and intervention efforts.
