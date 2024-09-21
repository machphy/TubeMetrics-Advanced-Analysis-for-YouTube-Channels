from flask import Flask, render_template, request, redirect, url_for, flash
from modules.youtube_api import (
    get_channel_details,
    get_recent_uploads,
    get_top_performing_video,
    get_most_commented_video,
    get_most_used_tags,
    get_audience_retention_rate,
    get_channel_milestones,
    get_channel_playlists,
    analyze_trending_videos,
    get_video_sentiment_analysis,
    get_channel_recommendations,
    get_channel_id_from_url
)
from modules.error_handling import handle_invalid_url
from modules.engagement_metrics import calculate_engagement_rate
from modules.visualizations import visualize_engagement_metrics, track_subscriber_view_growth

app = Flask(__name__)
app.secret_key = 'AIzaSyDpKjHACH_igJ5susIvePXITCNOJWqo4Po'

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/channel', methods=['POST'])
def channel():
    """Handle the form submission for channel analysis."""
    channel_url = request.form.get('channel_url')
    try:
        # Extract Channel ID from URL
        channel_id = get_channel_id_from_url(channel_url)
        
        # Get Channel Details
        details = get_channel_details(channel_id)
        
        # Get Recent Uploads
        recent_uploads = get_recent_uploads(channel_id)
        
        # Get Top Performing Video
        top_video = get_top_performing_video(channel_id)
        if top_video:
            engagement_rate = calculate_engagement_rate(
                int(top_video['likeCount']),
                int(top_video['commentCount']),
                int(top_video['viewCount'])
            )
            top_video['engagementRate'] = engagement_rate
        
        # Get Most Commented Video
        most_commented_video = get_most_commented_video(channel_id)
        
        # Get Most Used Tags
        most_used_tags = get_most_used_tags(channel_id)
        
        # Get Audience Retention Rate
        audience_retention_rate = get_audience_retention_rate(channel_id)
        
        # Get Channel Milestones
        milestones = get_channel_milestones(channel_id)
        
        # Get Channel Playlists
        playlists = get_channel_playlists(channel_id)
        
        # Analyze Trending Videos
        trending_videos = analyze_trending_videos(channel_id)
        
        # Video Sentiment Analysis
        sentiment_analysis = get_video_sentiment_analysis(channel_id)
        
        # Get Channel Recommendations
        recommendations = get_channel_recommendations(channel_id)
        
        # Track Subscriber and View Growth
        growth_metrics = track_subscriber_view_growth(channel_id)
        
        # Visualize Engagement Metrics
        visualize_engagement_metrics(channel_id)
        
        return render_template(
            'channel_details.html',
            details=details,
            recent_uploads=recent_uploads,
            top_video=top_video,
            most_commented_video=most_commented_video,
            most_used_tags=most_used_tags,
            audience_retention_rate=audience_retention_rate,
            milestones=milestones,
            playlists=playlists,
            trending_videos=trending_videos,
            sentiment_analysis=sentiment_analysis,
            recommendations=recommendations,
            growth_metrics=growth_metrics
        )
    except ValueError as e:
        # Handle invalid URL errors
        flash(handle_invalid_url(str(e)))
        return redirect(url_for('index'))
    except Exception as e:
        # Handle other errors
        flash(f"An unexpected error occurred: {str(e)}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
