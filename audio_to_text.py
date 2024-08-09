import whisperx
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
load_dotenv()
import os
hf_token = os.getenv('HF_TOKEN')

class AudioTranscription:
    def __init__(self, device="cpu", batch_size=16, compute_type="int8"):
        self.device = device
        self.batch_size = batch_size
        self.compute_type = compute_type
        try:
            self.model = whisperx.load_model("large-v2", self.device, compute_type=self.compute_type)
            self.diarize_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=self.device)
        except Exception as e:
            print(f"Error loading models: {e}")
            raise

    def transcribe_audio(self, audio_file):
        try:
            audio = whisperx.load_audio(audio_file)
        except Exception as e:
            print(f"Error loading audio file: {e}")
            return None
        
        try:
            result = self.model.transcribe(audio, batch_size=self.batch_size)
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None

        try:
            model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
            result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)
        except Exception as e:
            print(f"Error aligning audio: {e}")
            return None

        try:
            diarize_segments = self.diarize_model(audio)
            result = whisperx.assign_word_speakers(diarize_segments, result)
        except Exception as e:
            print(f"Error during diarization: {e}")
            return None

        return result

    def convert_to_df(self, result):
        if result is None:
            print("No result to save.")
            return

        try:
            df = pd.DataFrame(result["segments"])
            df = df[["start", "end", "text", "speaker"]]
            return df
        except Exception as e:
            print(f"Error Converting into Dataframe from segments: {e}")