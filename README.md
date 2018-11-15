# Bluzelle CLI

[![N|Solid](https://bluzelle.com/assets/img/Bluzelle%20-%20Screen%20-%20Logo%20-%20Big%20-%20Blue.png)](https://bluzelle.com/)



The Bluzelle CLI is an interactive console tool written in Python for loading sample data into your UUID.  Some of the features include:

  - Loading random sample data and specifying how many records you'd like
  - Loading data from a CSV file
  - Dropping keys from a specified UUID


# Instructions

1) Insall dependencies:
```sh
$ pip install .
$ pip install -r requirements.txt
```
2) Run Bluzelle CLI

```sh
$ cd BluzelleCLI
$ python console.py
```

3) Select the prompt depending on your needs

# Things to note

  - For the second option, loading a csv file, you can add the relative path. (For example, if you run console.py, the relative path for the csv file would be "csv/example.csv")

# Creating a binary file

- Run:
```sh
$ pyinstaller --clean --distpath dist --name console --additional-hooks-dir pyinstaller/ --onefile console.py
```

- The binary executable will be in the created "dist" folder