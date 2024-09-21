# modules/engagement_metrics.py

def calculate_engagement_rate(like_count, comment_count, view_count):
    """
    Calculates the engagement rate of a video.
    
    Parameters:
        like_count (int): Number of likes on the video.
        comment_count (int): Number of comments on the video.
        view_count (int): Number of views on the video.

    Returns:
        float: Engagement rate calculated as a percentage.
    """
    try:
        if view_count == 0:
            return 0
        engagement = (like_count + comment_count) / view_count * 100
        return round(engagement, 2)
    except Exception as e:
        print(f"Error calculating engagement rate: {e}")
        return 0
