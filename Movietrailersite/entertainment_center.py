from Movietrailersite import media2, fresh_tomatoes


toy_story = media2.Movie("Toy Story",
                         'A story about a boy and his toys that come to life.',
                         'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                         'http://www.youtube.com/watch?v=vwyZH85NQC4')

avatar = media2.Movie('Avatar',
                      'Blue Grown-up smurfs horde valuable minerals',
                      'http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg',
                      'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

fightclub = media2.Movie('Fight Club',
                         'Something fierce is happening all around',
                         'http://api.ning.com/files/eUrPno3TQ7XYJ6AOpoykz2Sm2aeanh6xyLLwFqB1bd*dvpJ2k5rh36TNt2DRjSE1SiNT*GnD5mtDP1bqHlJvesfbdfzlWG7Q/MoviePosterFightClub.jpg',
                         'https://www.youtube.com/watch?v=SUXWAEX2jlg')


movies = [toy_story, avatar, fightclub]

fresh_tomatoes.open_movies_page(movies)

print(toy_story.storyline, avatar.trailer_youtube_url)
print(media2.Movie.valid_ratings)
print(media2)
# avatar.show_trailer()