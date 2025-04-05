from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi

import mcp.types as types


mcp=FastMCP("TUBE-RECAP-RELOADED")

def get_transcript(url:str):
    video_id=url.split('=')[1]
    transcript=fetch_transcript_from_video(video_id)
    return transcript


# here we get the transcript from the video
def fetch_transcript_from_video(video_id):
    transcript_list=YouTubeTranscriptApi.get_transcript(video_id,languages=['en','en-GB'])
    transcript=''.join([d['text'] for d in transcript_list])
    return transcript

@mcp.resource("config://hello")
def get_config() -> str:
    """Secret configuration for the app."""
    return "the secret key is dasdasdasdasd"



    
    
@mcp.tool()
def get_youtube_video_summary(url:str):
    
    """
    Get the transcript of the youtube video from a url.

    Args:
        url (str): The url of the youtube video.
    Returns:
        str: The transcript of the youtube video.

    """
    
    ts=get_transcript(url)
    return ts




if __name__=="__main__":
    mcp.run(transport='stdio')
