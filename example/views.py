

from django.http import HttpResponse
import yt_dlp
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

DEEPGRAM_API_KEY = '3116ad35b1e7af0328546108be8a6c903aea8f26'

def get_audio_url(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extract_flat': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        return info_dict['url']
    

def transcribe_youtube_audio(youtube_url):
    audio_url = get_audio_url(youtube_url)

    response = requests.post(
        'https://api.deepgram.com/v1/listen',
        headers={
            'Authorization': f'Token {DEEPGRAM_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'url': audio_url
        }
    )

    if response.ok:
        transcript = response.json()
        return transcript['results']['channels'][0]['alternatives'][0]['transcript']
    else:
        raise Exception(f"Deepgram API error: {response.status_code} - {response.text}")

def index(request):
    html = f'''
    <html>
        <body>
            <p>Welcome to the API</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

@csrf_exempt  # Only use this in development/testing
def AudioTranscript(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            audio_link = data.get('link_audio')
            if not audio_link:
                return JsonResponse({'error': 'Missing "link_audio" field'}, status=400)
            
            trans_data = transcribe_youtube_audio(str(audio_link))
            return JsonResponse({'message': 'Received audio link', 'link_audio': audio_link, 'transcribed_text': str(trans_data)})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)