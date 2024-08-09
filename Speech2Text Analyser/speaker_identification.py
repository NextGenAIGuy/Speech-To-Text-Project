import pandas as pd

class SpeakerNameMapper:
    def __init__(self, df):
        self.df = df
        self.names = ["Sam", "Alice", "Bob"]

    def find_name_in_text(self, text):
        for name in self.names:
            if name.lower() in text.lower():
                return name
        return None

    def map_speakers(self):
        speaker_map = {}
        for index, row in self.df.iterrows():
            found_name = self.find_name_in_text(row['text'])
            if found_name:
                speaker_map[row['speaker']] = found_name
        self.df['speaker'] = self.df['speaker'].apply(lambda x: speaker_map.get(x, x))
        return self.df
    
