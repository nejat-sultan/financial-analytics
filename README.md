This project is designed to perform Exploratory Data Analysis (EDA) on news articles related to financial markets. It aims to extract insights from textual data, including sentiment analysis, topic modeling, and trends over time, which can be valuable for traders and analysts.

# Project Overview

The project analyzes financial news headlines and articles, with the following goals:
- Descriptive Statistics: Analyze article length, publisher activity, and publication dates.
- Sentiment Analysis: Assess the sentiment of news headlines (positive, negative, neutral).
- Topic Modeling: Identify common topics and keywords in news articles.
- Time Series Analysis: Investigate trends in publication frequency over time.
- Publisher Analysis: Identify which publishers contribute the most articles and their impact on sentiment.

The analysis is conducted using Python and relevant libraries for natural language processing (NLP) and data analysis.

# Features

- Descriptive Statistics: Summarizes headline lengths, articles per publisher, and publication dates.
- Sentiment Analysis : Detects positive, negative, or neutral sentiment in news headlines.
- Topic Modeling : Extracts common topics from articles using NLP techniques.
- Time Series Analysis : Analyzes trends in publication dates over time.
- Publisher Analysis : Determines the most active publishers and their focus areas.

# Requirements

Before running the project, make sure you have the following dependencies installed:
pandas
numpy
matplotlib
seaborn
scikit-learn
nltk
spacy
gensim
jupyterlab
pytest
These dependencies are listed in the requirements.txt file and can be installed easily using pip install -r requirements.txt

# Installation

Clone the repository:
git clone https://github.com/nejat-sultan/financial-analytics.git
cd financial-analytics

# Set up a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  

# Open the Jupyter notebook for analysis:

jupyter notebook notebooks/eda.ipynb
Once the dependencies are installed, you can start exploring the data through the provided Jupyter notebooks or by running the analysis scripts.

# Testing

To ensure the correctness of the code, you can run the unit tests provided in the tests/ folder. Run the tests with: pytest
