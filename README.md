# cafeteria

This app demonstrates a simple cafeteria application for various customers from different companies.
Developed for HackerEarth 2021 hackathon




# Information about the develop branch
1. Created develop branch and the flow of the deployment is as follwing:
   * Create seprate branches for each of the features and make commits in the respective commits for the branch.
   * Once the code is commited and pushed to the repository, then make the pull requests accordingly into the develop branch
   * Once the prs are reviewed, they will be merged into the develop branch which will be mergerd into the master branch.
2. Django is used as backend, sqllite for dev, Postgres for prod.
3. App hosting will be on heroku or any third party free hosting sites.


Recent changes:
1. Model has been designed and migrated.
To run the, clone the repo and run 
      python manage.py migrate and then run server.
2. In admin site as well the models are registered.
