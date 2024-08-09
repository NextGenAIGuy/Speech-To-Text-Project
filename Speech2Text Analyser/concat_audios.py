from pydub import AudioSegment

audio1 = AudioSegment.from_wav("audio_file\AI Advancement.wav")
audio2 = AudioSegment.from_wav("audio_file\\record_out.wav")


combined_audio = audio2 + audio1 

combined_audio.export("audio_file/combined_audio.wav", format="wav")
