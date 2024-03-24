# Project: Deploying a ML Model to Cloud Application Platform with FastAPI

### Link to Repository:

https://github.com/onalv/udacity-mlops-project-3-bis

### Link to deployed application

https://udacity-mlops-project-3-bis.onrender.com/

Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up

- Download and install conda if you don’t have it already.
  - Use the supplied requirements file to create a new environment, or
  - conda create -n [envname] "python=3.8" scikit-learn dvc pandas numpy pytest jupyter jupyterlab fastapi uvicorn -c conda-forge
  - Install git either through conda (“conda install git”) or through your CLI, e.g. sudo apt-get git.

## Repositories

- Create a directory for the project and initialize git and dvc.
  - As you work on the code, continually commit changes. Generated models you want to keep must be committed to dvc.
- Connect your local git repo to GitHub.
- Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
  - Make sure you set up the GitHub Action to have the same version of Python as you used in development.
- Set up a remote repository for dvc.

# Data

- Download census.csv and commit it to dvc.
- This data is messy, try to open it in pandas and see what you get.
- To clean it, use your favorite text editor to remove all spaces.
- Commit this modified data to dvc (we often want to keep the raw data untouched but then can keep updating the cooked version).

# Model

- Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
- Write unit tests for at least 3 functions in the model code.
- Write a function that outputs the performance of the model on slices of the data.
  - Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
- Write a model card using the provided template.

# API Creation

- Create a RESTful API using FastAPI this must implement:
  - GET on the root giving a welcome message.
  - POST that does model inference.
  - Type hinting must be used.
  - Use a Pydantic model to ingest the body from POST. This model should contain an example.
    - Hint: the data has names with hyphens and Python does not allow those as variable names. Do not modify the column names in the csv and instead use the functionality of FastAPI/Pydantic/etc to deal with this.
- Write 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction).
