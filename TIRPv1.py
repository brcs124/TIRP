import os
import time
from TikTokApi import TikTokApi
from instabot import Bot

# TikTok API Credentials
api = TikTokApi()
username = 'your_tiktok_username'
password = 'your_tiktok_password'

# Instagram API Credentials
bot = Bot()
bot.login(username='your_instagram_username', password='your_instagram_password')

# Get the top 50 videos from TikTok
videos = api.trending(count=50)

# Repost the videos on Instagram
for video in videos:
    # Download the video
    video_url = video['video']['downloadAddr']
    os.system(f"wget {video_url} -O video.mp4")
    
    # Post the video on Instagram
    bot.upload_video("video.mp4", caption="Check out this video from TikTok!")
    
    # Wait for 30 seconds before reposting the next video
    time.sleep(30)

# Exit the script after all videos have been reposted
exit()
