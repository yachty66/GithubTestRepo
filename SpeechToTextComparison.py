#converted video https://drive.google.com/file/d/1x7UaU69TRhDT00wrKMgwOK00YPHy1m3U/view?usp=sharing
from google.cloud import storage
from google.cloud import speech
import os
import io
import whisper

def sttGoogle():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/maxhager/Projects2022/GithubTestRepo/speechtotext-364309-ba2aa4e39f86.json'
    speech_client = speech.SpeechClient()

    config_wav = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US',
        audio_channel_count=2
    )

    media_uri = 'gs://videof35/freedom35.wav'
    long_audi_wav = speech.RecognitionAudio(uri=media_uri)

    config_wav_enhanced = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US',
        use_enhanced=True,
        model='video',
        audio_channel_count=2,
    )

    operation = speech_client.long_running_recognize(
        config=config_wav,
        audio=long_audi_wav,
    )
    response = operation.result(timeout=90)

    for result in response.results:
        with open ('transcriptGoogle.txt', 'w') as f:

            f.write(result.alternatives[0].transcript)
        
def sttWhisper():
    model = whisper.load_model("medium")
    result = model.transcribe("freedom35.mp4")
    with open('transcriptWhsiperLarge.txt', 'w') as f:
        f.write(result["text"])
        
if __name__ == "__main__":
    sttGoogle()
    #sttWhisper()