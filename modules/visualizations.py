import matplotlib.pyplot as plt

def visualize_engagement_metrics(engagement_data):
    """
    Visualizes engagement metrics such as likes, comments, and shares.
    
    Parameters:
    engagement_data (dict): A dictionary containing engagement metrics.
                            Example: {"Likes": 1200, "Comments": 300, "Shares": 150}
    """
    labels = list(engagement_data.keys())
    values = list(engagement_data.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color=['#4CAF50', '#2196F3', '#FF9800'])
    plt.title('Engagement Metrics')
    plt.xlabel('Metrics')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.show()

def track_subscriber_view_growth(subscriber_data, view_data, time_periods):
    """
    Visualizes the growth of subscribers and views over time.
    
    Parameters:
    subscriber_data (list): List of subscriber counts over time.
    view_data (list): List of view counts over time.
    time_periods (list): Corresponding time periods (e.g., months or weeks).
                         Example: ['Jan', 'Feb', 'Mar', 'Apr']
    """
    plt.figure(figsize=(12, 6))

    # Plotting Subscribers Growth
    plt.plot(time_periods, subscriber_data, marker='o', linestyle='-', color='b', label='Subscribers Growth')

    # Plotting Views Growth
    plt.plot(time_periods, view_data, marker='o', linestyle='-', color='r', label='Views Growth')

    plt.title('Subscriber and View Growth Over Time')
    plt.xlabel('Time Period')
    plt.ylabel('Counts')
    plt.legend()
    plt.grid(axis='both', linestyle='--', linewidth=0.5)
    plt.show()
