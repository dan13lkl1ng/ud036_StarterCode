# ud036_StarterCode
Shows the box arts with titles of a list of movies and opens a trailer from youtube when clicked.

## Getting started
1. Install Python
2. Install modules `webbrowser`, `os`, `re`
3. Run
```
$ python entertainment_center.py
```

## Built with
* Bootstrap
* JQuery

## Issues
In Linux it is possible that the created site will open in another browser (e.g. elinks). To determine the browser you can modify the line 168 in `fresh_tomatoes.py`

```python
webbrowser.open('file://' + url, new=2)
```
to 
```python 
webbrowser.get('chromium').open('file://' + url, new=2)
```
by adding `.get('chromium')` or another browser.
