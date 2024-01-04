<h1>Spam Classification Project</h1>

<pre>In this project, we have the data of some messages and their corresponding labels. The dataset (CSV) is been given in the data folder.
    
The primary goal is to build a UI where the user can put his message and then he will get if the message is spam or ham.
As this is textual data we are going to use some NLP concepts.
    
There are two ways to solve the problem: first to use a Machine learning-based approach and second of course to use a Deep learning-based approach.   
This project contains both methods,
    
To clean the data we are using some basic concepts as well as taking the help of the regular expressions and NLTK library.
Cleaning the data involves removing punctuations, lowering, removing HTML tags and lemmatizing.
You can also use stemming instead of lemmatizing as our goal is not to transfer the text again to the user.
After clearing the data we are going to convert the text into numbers as it is a necessary step.
    
Machine learning approach:
    We are converting the text in numbers by two frequency-based embedding techniques: Bag of Words and Tfidf.
    With this, we trained multiple models like Logistic Regression, Random Forest, SVM, KNN etc.
    The best was the Random Forest with Bag of Words approach.
    
Deep learning approach:
    The clean text is tokenized with the help of the class Tokenizer present in Keras.
    After that we need to make the length of all sentences equal, so we are using pad_sequences which is again present in Keras.
    Finally, we are building the sequential model. We are using the Embedding layer to capture the semantic meaning in the data.
    For this project we have used Bidirectional LSTM, you can use LSTM, RNN anything and check with it.
    Finally, we are training the model and testing it.

For the UI purpose we have taken a Deep learning-based model but you can also take the Machine learning model like Random Forest which performed the best

</pre>





