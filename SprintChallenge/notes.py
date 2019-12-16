""" Flask """
# run the web app.
FLASK_APP=airquality:APP FLASK_ENV=development flask run
# use a created pipfile.
Pipenv install 
# get into virtual environment.
Pipenv shell 

""" Gunicorn """
# install gunicorn.
pipenv install gunicorn psycopg2
# create Profile with 'web: gunicorn twitoff:APP -t 120'.
'Procfile' = web: gunicorn twitoff:APP -t 120

""" Heroku """
# create a remote project repo on heroku.
heroku git:remote -a cvanchieri-airquality
# push content to heroku master.
git push heroku master
# connect 'postgress' with heroku.
heroku addons:create heroku-postgresql:hobby-dev