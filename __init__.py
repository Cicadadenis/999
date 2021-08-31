git init

git add .

git commit -m 'first relise'

heroku create 'cicada'

git remote -v

git push heroku main

heroku ps:scale worker=1
