"""
This is the program that takes in both the freshTomatoes and media programs instantiates array of movie objects and passes them to create the html page to render movie trailers.
"""

import freshTomatoes
import media

# The Matrix
matrix = media.Movie("The Matrix",
					 "Neo searches for the truth about the Matrix and discovers his place in it.",
					 "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					 "https://www.youtube.com/watch?v=_Ls19O-9p3s")

# Point Break
point_break = media.Movie("Point Break",
					     "Reeves stars as rookie FBI agent Johnny Utah, who is investigating a string of bank robberies possibly being committed by surfers. Johnny goes undercover to infiltrate the surfing community and develops a complex friendship with Bodhi (Swayze), the charismatic leader of a gang of surfers.",
					     "http://upload.wikimedia.org/wikipedia/en/7/7e/Pointbreaktheatrical.jpg",
					     "https://www.youtube.com/watch?v=AVk3mR2UhgI")

# Fight Club
fight_club = media.Movie("Fight Club",
					     "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...",
					     "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
					     "www.youtube.com/watch?v=SUXWAEX2jlg")

# The Usual Suspects
usual_suspects = media.Movie("The Usual Suspects",
						     "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.",
						     "http://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
						     "https://www.youtube.com/watch?v=oiXdPolca5w")

# Apollo 13
apollo = media.Movie("Apollo 13",
					 "The film depicts astronauts Lovell, Jack Swigert and Fred Haise aboard Apollo 13 for America's third Moon landing mission. En route, an on-board explosion deprives their spacecraft of most of its oxygen supply and electric power, forcing NASA's flight controllers to abort the Moon landing, and turning the mission into a struggle to get the three men home safely.",
					 "http://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
					 "https://www.youtube.com/watch?v=nEl0NsYn1fU")

# Contact
contact = media.Movie("Contact",
					  "A SETI scientist who finds strong evidence of extraterrestrial life and is chosen to make first contact.",
					  "http://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
					  "https://www.youtube.com/watch?v=d9C2cF3KvP8")

# Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# School of Rock
school_of_rock = media.Movie("School of Rock",
                             "About School of Rock",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Ratatouille
ratatouille = media.Movie("Ratatouille",
                          "About a rat that can cook!",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Midnight in Paris
midnight_in_paris = media.Movie("Mightnight in Paris",
                                "About a mightnight in Paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# Hunger Game
hunger_game = media.Movie("Hunger Game",
                          "About Hunger Game",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=SMGRhAEn6K0")

# Build website
movies = [matrix, point_break, fight_club, usual_suspects, apollo, contact, toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_game]
# call function
freshTomatoes.open_movies_page(movies)
