import wget
import os
import time
import shutil
import praw

class Download:
    def download(self, url):
        """ Download files from web and puts them in a 
            folder called images. """
        if not os.path.exists("images"):
            os.mkdir("images", 777)
            time.sleep(2) # Sleep to give system time to create folder
        self.url = url
        filename = wget.download(self.url)
        print(filename)
        os.rename(filename, "images/{}".format(filename))
         
    def delete_folder(self):
        shutil.rmtree("images")
  
class Reddit:
    def reddit(self):
        """ Returns a list of urls from top submissions
            on reddit."""
        user_agent = ("loolY 0.2")
        r = praw.Reddit(user_agent = user_agent)
        subreddit = r.get_subreddit('earthporn')
        linkList = list()
        for submission in subreddit.get_hot(limit=10):
            if "imgur" not in submission.url : continue
            if ".jpg" not in submission.url:
                submission.url = submission.url + ".jpg"
            linkList.append(str(submission.url))
        return linkList

  