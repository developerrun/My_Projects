This is a Python-based Reddit 
scraping tool that uses the PRAW (Python Reddit API Wrapper) library to fetch data from Reddit. It allows you to scrape post submissions from specific subreddits and comments from individual posts.  


- Features
Scrape Posts: Fetch posts from a specified subreddit, filtering by type (e.g., top, new, hot, controversial), limit, minimum score, and a keyword in the title.

Scrape Comments: Retrieve comments from a specific Reddit post using its permalink URL, filtering by type (e.g., top, new, hot), limit, and a keyword in the comment body.

Data Export: Save scraped comments directly to a CSV file for easy data analysis.

Visualization: Generate a bar graph of post titles and their scores, saved as Results.png, to visually represent the popularity of posts.

_____________________________________________________________

Prerequisites:

    Python 3.x

______________________________________________________________

Required Python Libraries:

    praw

    csv

    validators

    argparse

    matplotlib

_________________________________________________________________

Method of installation: pip install praw validators matplotlib 

# Go to App Preferences of reddit and create a script application copy your client and secret id and paste it here alogn with you reddit username and password with a user agent to scrape reddit using praw 

# Example: (reddit_API = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    username="YOUR_REDDIT_USERNAME",
    password="YOUR_REDDIT_PASSWORD",
    user_agent="linux:APIBASEDSCRAPER:1.0 (by u/YOUR_REDDIT_USERNAME)"
)) 

_________________________________________________________________

Scarping options for CLI usage: 

--subreddit: (required) The name of the subreddit (e.g., AskReddit).

--type: The type of posts to scrape. Accepted values: top, hot, new, controversial. Default: top.

--limit: The maximum number of posts to fetch. Default: 10.

--min_score: The minimum score a post must have to be included.

--keyword: A keyword to filter posts by, based on the title.

--graph: Use this flag to generate a bar graph of post scores. The graph will be saved as Results.png.

______________________________________________________________________

Example usage:
 (python3 reddit_scraper.py posts --subreddit AskReddit --type top --limit 15 --graph)



