import media
import fresh_tomatoes

# Create instances of class media.Movie(title, poster, trailer)
rock_n_rolla = media.Movie("RocknRolla",
                         "https://miguelvaca.files.wordpress.com/2009/11/rocknrolla.jpg",  # NOQA
                         "https://youtu.be/WEIykbkkq6I")

the_martian = media.Movie("The Martian",
                          "http://filmotatnik.blox.pl/resource/martian.jpg",
                          "https://youtu.be/ej3ioOneTy8")

ex_machina = media.Movie("Ex Machina",
                         "http://cfile28.uf.tistory.com/image/221E454F575D908E22FD90",  # NOQA
                         "https://youtu.be/45SUqUXpwgY")

pacific_rim = media.Movie("Pacific Rim",
                          "http://www.impawards.com/2013/posters/pacific_rim_ver12_xlg.jpg",  # NOQA
                          "https://youtu.be/5guMumPFBag")

the_man = media.Movie("The Man from U.N.C.L.E.",
                      "http://www.movieplayhit.com/wp-content/uploads/2015/07/The-Man-from-U.N.C.L.E..jpg",  # NOQA
                      "https://youtu.be/w_Ky4KPzKwY")

guardians = media.Movie("Guardians of the Galaxy",
                        "http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg",  # NOQA
                        "https://youtu.be/d96cjJhvlMA")

# Add instances of Movie to the list
movies = [rock_n_rolla, the_martian, ex_machina,
          pacific_rim, the_man, guardians]

# Pass list of movies to the function to generate HTML
fresh_tomatoes.open_movies_page(movies)
