import media
import fresh_tomatoes

pretty_woman = media.Movie("Pretty Woman",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/Pretty_woman_movie.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=Wzii8IuL8lk")

love_actually = media.Movie("Love actually",
                            "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=fOS-HMiVejo")

amelie = media.Movie("Amelie",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=LM0sZZ1xFDs")

the_millers = media.Movie("We're the Millers",
                          "https://upload.wikimedia.org/wikipedia/en/4/44/We%27re_the_Millers_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=0Vsy5KzsieQ")

aristocats = media.Movie("The Aristocats",
                         "https://upload.wikimedia.org/wikipedia/en/8/8d/Aristoposter.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=scZSFUwgeIM")


hunger_games_part_1 = media.Movie("The Hunger Games: Mockingjay Part 1",
                                  "https://upload.wikimedia.org/wikipedia/en/6/63/MockingjayPart1Poster3.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=3PkkHsuMrho")  # NOQA

# Creates a list of all the movie instances
movies = [pretty_woman, love_actually, amelie, the_millers,
          aristocats, hunger_games_part_1]

# Calls the open_movies_page function in order to create the website
fresh_tomatoes.open_movies_page(movies)
