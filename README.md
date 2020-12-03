# django-xkcd
django, urls, views

<img src="https://imgs.xkcd.com/comics/tasks_2x.png>

## Set up
- Fork and clone this repository

## Objective
- Practice setting up the Django Framework with an API

## Task
- Generate a simple page that when a user clicks a button, a random XKCD comic will be generated

Check the documentation for the XKCD Json Interface (this works like an API)
https://xkcd.com/json.html

Hint:

```
import requests
data = requests.get("http://xkcd.com/614/info.0.json")
print(page.json())
```

## Submission
- Submit a pull request once complete
