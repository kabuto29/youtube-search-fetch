# youtube-search-fetch
Steps to run server and apis.

1. Run following to start django webserver.

  python manage.py runserver
  
2. Api to use youtube search api and add data to db.

http://127.0.0.1:8000/dumpData

3. Api to get videos in decreasing order of publishedDate from db. 
   (paginated with 7 videos per page)

http://127.0.0.1:8000/videoList

4. Api to get videos as per search keywords.

http://127.0.0.1:8000/videoList?search=parmish

# Work-In-Progress
1. Using celery to call youtube data api in background async.
2. Dockeriztion of this project. 

