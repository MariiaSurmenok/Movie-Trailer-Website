# Movie-Trailer-Website
Program that allows to create html page with your favorite movies.
## Quick start
You need Python 2.7 installed on your computer.
* clone the repo `git clone https://github.com/MariiaSurmenok/Movie-Trailer-Website.git`
* execute `python entertainment_center.py`

To run the code:
* in terminal (command line): 
    * run the command `python entertainment_center.py` 
* in IDLE: 
    * open file **entertainment_center.py**
    * open _run_ menu and click _run module_

To change content:
* open file **entertainment_center.py** in editor
* create instances of your favorite movies with their titles, urls of poster, and urls of trailer on youtube:
```
avatar = media.Movie("Avatar", 
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246", 
                     "https://youtu.be/d1_JBMrrYw8")
```
* add them to a list and pass the list to **open_movies_page** function
```
movies = [avatar, ...]
fresh_tomatoes.open_movies_page(movies)
```

## License
Code released under the [MIT License](https://github.com/MariiaSurmenok/Movie-Trailer-Website/blob/master/LICENSE). 