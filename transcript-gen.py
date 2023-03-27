import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
        
curr_folder = os.path.dirname(os.path.realpath(__file__))
print(curr_folder)
directory = "transcripts"
path = os.path.join(curr_folder, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)

def gen_trans(video_id, i):
    video_id_str = str(video_id)
    print("Getting transcript for video:" + video_id_str)
    transcript = YouTubeTranscriptApi.get_transcript(video_id_str, languages=['en-US', 'en'])
    
    # create unique folder inside the transcripts folder, for each video
    os.mkdir('transcripts/%s' %i)
    
    #start writing to files, within their own folder for each video id
    print("Writing transcript to text file")
    txt_formatter = TextFormatter()
    txt_formatted = txt_formatter.format_transcript(transcript)
    with open('transcripts/%s/' %i + '%s__transcript.txt' % i, 'w') as txt_file:
        txt_file.write(txt_formatted)

    print("done with video")
    print("----------------------------------")


with open('videos.txt') as file:
    for i, line in enumerate(file):
        print("Processing url:")
        print(line, i)
        print(i)
        gen_trans(line, i)