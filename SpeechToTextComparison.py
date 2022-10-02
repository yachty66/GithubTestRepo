


# Imports the Google Cloud client library
from google.cloud import storage
from google.cloud import speech
import os
import io
import whisper

def sttGoogle():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/maxhager/Projects2022/GithubTestRepo/speechtotext-364309-ba2aa4e39f86.json'
    speech_client = speech.SpeechClient()
    ## Step 2. Configure Media Files Output
    config_wav = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    # Example 3: Transcribing a long media file
    media_uri = 'gs://videof35/freedom35.wav'
    long_audi_wav = speech.RecognitionAudio(uri=media_uri)

    config_wav_enhanced = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US',
        use_enhanced=True,
        model='video'
    )

    operation = speech_client.long_running_recognize(
        config=config_wav,
        audio=long_audi_wav,
    )
    response = operation.result(timeout=90)

    for result in response.results:
        with open ('transcriptGoogle.txt', 'w') as f:
            f.write(result.alternatives[0].transcript)
            f.write(result.alternatives[0].confidence)
            f.write()
        
        
def sttWhisper():
    model = whisper.load_model("medium")
    result = model.transcribe("freedom35.mp4")
    with open('transcriptWhsiperLarge.txt', 'w') as f:
        f.write(result["text"])
    #print(result["text"])
    


def test():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= '/Users/maxhager/Projects2022/GithubTestRepo/speechtotext-364309-ba2aa4e39f86.json'
    client = storage.Client()

    bucket = client.get_bucket('videof35')
    print(bucket.name)
    #gs://videof35/freedom35.mp4

    #blob = bucket.get_blob('temp_files_folder/test.txt')

    #print(blob.download_as_string)
    


if __name__ == "__main__":
    sttGoogle()
    #sttWhisper()