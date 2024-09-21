# modules/youtube_api.py

from googleapiclient.discovery import build

# Replace with your YouTube API key
API_KEY = 'AIzaSyDpKjHACH_igJ5susIvePXITCNOJWqo4Po'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Initialize the YouTube API client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

def get_channel_id_from_url(channel_url):
    """
    Extracts the channel ID from the provided YouTube channel URL.
    """
    # Logic to extract channel ID from the URL
    # Implement actual extraction logic based on URL patterns
    if "channel/" in channel_url:
        return channel_url.split("channel/")[-1].split("/")[0]
    else:
        raise ValueError("Invalid Channel URL. Please provide a valid YouTube channel URL.")

def get_channel_details(channel_id):
    """
    Retrieves details of a YouTube channel.
    """
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()
    return response['items'][0] if response['items'] else {}

def get_recent_uploads(channel_id):
    """
    Retrieves recent uploads from the YouTube channel.
    """
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=5,
        order="date"
    )
    response = request.execute()
    return response['items']

def get_top_performing_video(channel_id):
    """
    Retrieves the top-performing video of the channel.
    """
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=1,
        order="viewCount"
    )
    response = request.execute()
    return response['items'][0] if response['items'] else {}

def get_most_commented_video(channel_id):
    """
    Retrieves the most commented video of the channel.
    """
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=channel_id,
        maxResults=1,
        order="relevance"
    )
    response = request.execute()
    if response['items']:
        video_id = response['items'][0]['snippet']['videoId']
        return get_video_details(video_id)
    return {}

def get_most_used_tags(channel_id):
    """
    Retrieves the most used tags in the channel videos.
    """
    # Mock implementation, requires more logic based on video data extraction.
    return ["Sample Tag 1", "Sample Tag 2"]

def get_audience_retention_rate(channel_id):
    """
    Retrieves audience retention rate for the channel.
    """
    # Mock data, YouTube API might need paid subscription for this data.
    return 65.7

def get_channel_milestones(channel_id):
    """
    Retrieves channel milestones (like subscriber count, view count, etc.).
    """
    details = get_channel_details(channel_id)
    return {
        "Subscribers": details['statistics']['subscriberCount'],
        "Views": details['statistics']['viewCount'],
        "Videos": details['statistics']['videoCount']
    }

def get_channel_playlists(channel_id):
    """
    Retrieves playlists from the channel.
    """
    request = youtube.playlists().list(
        part="snippet",
        channelId=channel_id,
        maxResults=5
    )
    response = request.execute()
    return response['items']

def analyze_trending_videos(channel_id):
    """
    Analyzes trending videos from the channel.
    """
    # Implement the actual analysis logic based on your data needs.
    return ["Trending Video 1", "Trending Video 2"]

def get_video_sentiment_analysis(channel_id):
    """
    Performs sentiment analysis on video comments.
    """
    # Mock sentiment analysis, actual implementation requires comments extraction.
    return {"Positive": 60, "Negative": 20, "Neutral": 20}

def get_channel_recommendations(channel_id):
    """
    Fetches channel recommendations based on current channel data.
    """
    # Mock data for recommendations
    return ["Recommended Channel 1", "Recommended Channel 2"]

def get_video_details(video_id):
    """
    Retrieves details of a video by its ID.
    """
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    return response['items'][0] if response['items'] else {}
