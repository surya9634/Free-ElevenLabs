import requests

# URL of the audio file to download
audio_url = "https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/samples/HEARME.wav"
audio_file_path = "HEARME.wav"

# Step 1: Download the audio file
response = requests.get(audio_url)

# Step 2: Define the URL for the Eleven Labs API endpoint
api_url = "https://api.elevenlabs.io/v1/speech-to-text?allow_unauthenticated=1"

# Prepare the payload for the request
files = {
    'file': response.content,
    'model_id': (None, 'scribe_v1'),
    'tag_audio_events': (None, 'true'),
    'diarize': (None, 'true')
}

# Make the POST request to the Eleven Labs API
response = requests.post(api_url, files=files)

# Check the response status code
if response.status_code == 200:
    # Print the response JSON if the request was successful
    print("Response JSON:", response.json())
else:
    # Print the error message if the request failed
    print("Error:", response.status_code, response.text)
