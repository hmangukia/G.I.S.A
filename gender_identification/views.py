from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Data, Info
import nltk
from nltk.corpus import stopwords
#import random
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import NaiveBayesClassifier
import string
import pandas as pd

# Create your views here.

def home(request):

	#if request.method == 'POST':

	print("sentimental analysis starts")
	def word_feats(words):
		return dict([(word, True) for word in words])

	if request.method == 'POST':
		df = pd.read_csv('Path of SE.csv', encoding = 'latin1')
		df.head(10)
		positive_vocab = df['positive_vocab']
		negative_vocab = df['negative_vocab']
		neutral_vocab = df['neutral_vocab']

		positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
		negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
		neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

		train_set = negative_features + positive_features + neutral_features

		classifier = NaiveBayesClassifier.train(train_set)

        # Predict
		neg = 0
		pos = 0
		neu = 0
		sentence = request.POST['text'].strip()
		print("Value of sentence is " + sentence)
		sentence = sentence.lower()
		words = sentence.split(' ')
		for word in words:
			classResult = classifier.classify( word_feats(word))
			if classResult == 'neg':
				neg = neg + 1
			if classResult == 'pos':
				pos = pos + 1
			if classResult == 'neu':
				neu = neu + 1

		response = 'Text is: ' + sentence + 'Positive: ' + str(float(pos)/len(words)) + \
        'Negative: ' + str(float(neg)/len(words)) + \
        'Neutral:  '+ str(float(neu)/len(words))

		pos1 = str(float(pos)/len(words))
		neg1 = str(float(neg)/len(words))
		neu1 = str(float(neu)/len(words))
		print(response)

		print("Gender identification starts")
		#text = Data.objects.get(pk=pk)
		df = pd.read_csv('Path of gender-classifier-DFE-791531.csv', encoding = 'latin1')
		#df = shuffle(shuffle(shuffle(df)))
		df.head(10)

		def find_features(top_words, text):
		    feature = {}
		    for word in top_words:
		        feature[word] = word in text.lower()
		    return feature	


		all_descriptions = df['description']
		all_tweets = df['text']
		all_genders = df['gender']
		all_gender_confidence = df['gender:confidence']
		description_tweet_gender = []
		# Creation of bag of words for the description
		bag_of_words = []
		c = 0  # for the index of the row
		stop = stopwords.words('english')
		for tweet in all_tweets:
		    description = all_descriptions[c]
		    gender = all_genders[c]
		    gender_confidence = all_gender_confidence[c]
		    
		    # remove the rows which has an empty tweet and description
		    # remove the rows with unknown or empty gender
		    # remove the rows which have gender:confidence < 80%
		    if (str(tweet) == 'nan' and str(description) == 'nan') or str(gender) == 'nan' or str(gender) == 'unknown' or float(gender_confidence) < 0.8:
		        c+=1
		        continue
		    
		    if str(tweet) == 'nan':
		        tweet = ''
		    if str(description) == 'nan':
        		description = ''
		    
		    # removal of punctuations
		    for punct in string.punctuation:
		        if punct in tweet:
		            tweet = tweet.replace(punct, " ")
		        if punct in description:
		        	description = description.replace(punct, " ")
		            
		    # adding the word to the bag except stopwords
		    for word in tweet.split():
		        if word.isalpha() and word.lower() not in stop:
		            bag_of_words.append(word.lower())
		    for word in description.split():
        		if word.isalpha() and word.lower() not in stop:
        			bag_of_words.append(word.lower())
		    
		    # using tweet and description for classification
		    description_tweet_gender.append((tweet+" "+description , gender))
		    c += 1

		#print(len(bag_of_words))
		#print(len(description_tweet_gender))

		# get top 4000 words which will act as our features of each sentence
		bag_of_words = nltk.FreqDist(bag_of_words) #FreqDist records the number of times each outcome of an experiment has occurred
		top_words = []
		for word in bag_of_words.most_common(3000):
		    top_words.append(word[0])

		print("Second for loop completed")
		top_words[:10]

		# creating the feature set, training set and the testing set
		feature_set = [(find_features(top_words, text), gender) for (text, gender) in description_tweet_gender]
		training_set = feature_set[:int(len(feature_set)*4/5)]
		testing_set = feature_set[int(len(feature_set)*4/5):]

		#print("Length of feature set", len(feature_set))
		#print("Length of training set", len(training_set))
		#print("Length of testing set", len(testing_set))

		# creating a naive bayes classifier
		NB_classifier = nltk.NaiveBayesClassifier.train(training_set)
		a_nb = nltk.classify.accuracy(NB_classifier, testing_set)*100
		print("Naive Bayes Classifier accuracy =", a_nb)
		#NB_classifier.show_most_informative_features(20)

		# creating a multinomial naive bayes classifier
		"""MNB_classifier = SklearnClassifier(MultinomialNB())
		MNB_classifier.train(training_set)
		a_mnb = nltk.classify.accuracy(MNB_classifier, testing_set)*100
		print("Multinomial Naive Bayes Classifier accuracy =", (a_mnb))

		# creating a logistic regression classifier
		LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
		LogisticRegression_classifier.train(training_set)
		a_lr = nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100
		print("Logistic Regression classifier accuracy =", a_lr)"""

		text = request.POST['text'].strip()
		features = find_features(top_words, text)
		r_nb = NB_classifier.classify(features)
		print(r_nb)
		r_mnb = MNB_classifier.classify(features)
		r_lr = LogisticRegression_classifier.classify(features)

		print("Gender identification ends")

		return render(request, 'result.html', {'result': result, 'neg1': neg1, 'pos1': pos1, 'neu1': neu1, 'text': text, 'a_nb': a_nb, 'a_mnb': a_mnb, 'a_lr': a_lr, 'r_nb': r_nb, 'r_mnb': r_mnb, 'r_lr': r_lr})	
	else:
		print("GET method")
		return render(request, "home.html", {})
