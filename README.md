# GIT LEAKS TO JSON

### INTRODUCTION

This code is an ETL that gets all the leaks in a Git repository and loads them into a json file

### 1. Libraries used
- 'signal': used for the handler signal Ctrl + C
- 're': used for ignoring capital letters
- 'sys': used for a tidied exit
- 'json': loading and dumping
- 'git': used to get to the git repository
- 'pprint': pretty printing

#### 1) Compiled_p
We return the patterns from the leaks that we want to search for. In this case: 'key', 'password' and 'credentials'

### 2. ETL
#### 1) Extract
We extract the data with the 'Repo' function and the url of the repository

#### 2) Transform
We iterate through the commits and search for the different leaks, saving them in a dictionary 'commit_dict'

#### 3) Load
We load the data into a json file using the json 'dump' and 'load' functions. We also print the results using the PrettyPrint library
