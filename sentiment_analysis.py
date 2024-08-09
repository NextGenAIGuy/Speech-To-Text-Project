import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
#nltk.download('vader_lexicon')
class SentimentAnalysis:
    def __init__(self, df):
        self.df = df
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        try:
            return self.sia.polarity_scores(text)
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return None

    def add_sentiment_analysis(self):
        try:
            self.df['sentiment'] = self.df['text'].apply(self.analyze_sentiment)
            sentiment_df = pd.json_normalize(self.df['sentiment'])
            self.result_df = pd.concat([self.df, sentiment_df], axis=1).drop(columns=['sentiment'])
        except Exception as e:
            print(f"Error adding sentiment analysis: {e}")
            self.result_df = None

    def categorize_sentiment(self, compound):
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def add_sentiment_category(self):
        if self.result_df is not None:
            try:
                self.result_df['sentiment_category'] = self.result_df['compound'].apply(self.categorize_sentiment)
            except Exception as e:
                print(f"Error categorizing sentiment: {e}")

    def save_to_csv(self, output_file_path):
        if self.result_df is not None:
            try:
                self.result_df.to_csv(output_file_path, index=False)
                print(f"Sentiment analysis saved to {output_file_path}")
                return self.result_df
            except Exception as e:
                print(f"Error saving to CSV: {e}")
        else:
            print("No result to save.")


