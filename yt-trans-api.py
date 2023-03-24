import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
        
curr_folder = os.path.dirname(os.path.realpath(__file__))
print(curr_folder)
directory = "transcripts"
path = os.path.join(curr_folder, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)

def gen_trans(video_id):
    print("Getting transcript for video: " + video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US', 'en'])
    
    # create unique folder inside the transcripts folder, for each video
    os.mkdir('transcripts/%s' %video_id)
    
    #start writing to files, within their own folder for each video id
    print("Writing transcript to text file")
    txt_formatter = TextFormatter()
    txt_formatted = txt_formatter.format_transcript(transcript)
    with open('transcripts/%s/' %video_id + '%s__transcript.txt' % video_id, 'w') as txt_file:
        txt_file.write(txt_formatted)

    print("done with video: " + video_id)
    print("----------------------------------")


with open('videos.txt') as file:
    for line in file:
        print("Processing url:" + line)
        gen_trans(line)