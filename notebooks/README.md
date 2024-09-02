This folder contains Jupyter notebooks used for data analysis and EDA. On this page, I performed the following:
- Descriptive Statistics on news data:
    * Done Basic statistics such as mean, median, and mode of textual lengths.
    * Count of articles per publisher to determine which publishers are most active.
    * Analyze the publication dates for trends over time.

- Text Analysis:
    * Determine the sentiment of news headlines (positive, negative, neutral).
    * Used NLP to extract common keywords and phrases from headlines.
- Time Series Analysis:
    * Explore the frequency of publications over time and identify spikes that may correlate with specific events.
- Publisher Analysis:
    * Identified which publishers contribute the most news and whether their content differs from others.
- Quantitative Analysis using Pynance and TA-Lib:
    * Integrated additional financial data for analysis.
    * Loaded and prepared stock price data into a pandas DataFrame with columns such as Open, High, Low, Close, and Volume.
    * Applied Financial Indicators:
        - Used TA-Lib to calculate various technical indicators like Moving Averages, RSI (Relative Strength Index), MACD (Moving Average Convergence Divergence)
        - visualize them using line chart
- Correlation Between News Sentiment and Stock Movements:
    * Sentiment Scores: Quantified the tone of news headlines (positive, negative, neutral) using sentiment analysis tools.
    * Daily Stock Returns: Calculated daily stock returns based on the percentage change in stock prices.
    * Correlation Analysis: Conducted correlation analysis to assess the relationship between the average daily sentiment scores and stock daily returns.
