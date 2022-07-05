import praw
import requests
import os
from pathlib import Path

with open('subs.txt') as subs:
    subs = subs.read().split(",")

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    password="",
    username="", )


class Scraper:
    def __init__(self):
        for i, post in enumerate(subs):
            self.limit = self.limit
            self.output_directory = f"./images/{post}/"
            if not os.path.exists(self.output_directory):
                os.mkdir(self.output_directory)

            i += 1



    def get_subreddit(self):

        for i, post in enumerate(subs):
            self.subreddit = reddit.subreddit(post)
            for submission in self.subreddit.hot(limit=self.limit):
                filename = Path(submission.url).name
                if not filename.endswith((".png", ".jpg", ".gif", "gifv")):
                    print(f"{submission.url} is not an image")
                    continue
                else:
                    dirname_plus_filename = f"./images/{post}/" + filename
                    with open(dirname_plus_filename, "wb") as file:
                        response = requests.get(submission.url)
                        file.write(response.content)
                        print(f"<- image downloaded:  {submission.url} from {post}")
                        i += 1

        return


def main():
    print("Scraping the following subs:" + str(subs))
    Scraper.limit = int(input("Please enter a number: "))
    Scraper().get_subreddit()
    print("Scraping complete... for now")
    return


if __name__ == "__main__":
    main()
